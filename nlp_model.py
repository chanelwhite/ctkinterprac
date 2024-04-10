from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
import ast
import nltk
from nltk.stem import PorterStemmer
import os
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from gensim.models import KeyedVectors
from scipy import spatial
# had to use an older version scipy
# download these first time you run
nltk.download('punkt')
nltk.download('stopwords')

class NLP():
    def generate_function(self, input_df):
        # Load English stop words
        stop_words = set(stopwords.words('english'))

        file_path = "joy.txt"
        joy_words = []
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                joy_words.extend(line.split())

        stemmer = PorterStemmer()
        stemmed_joy_words = [stemmer.stem(word) for word in joy_words]
        # stemmed words for checking compairson words
        api_key = os.getenv("OPENAI_API_KEY")
        client = OpenAI()

        # pick a joyful word to help frame our scenario
        word1 = random.choice(joy_words)
        print(word1)
        emotion = "joy"
        # get chat gbt to generate for us a scenario
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a therapist for non neural typical high school children. "
                                            "You describe scenarios to high school children to help them identify emotions."},
                {"role": "user", "content": f"Give me a 1 sentence long scenario on {emotion} using the key word {word1}."
                                            "I want the key word to identify the emotion, limit any other hints and be subtle"
                                            "Don't use the word joy"},
            ]
        )
        my_scenario = completion.choices[0].message.content

        joy_array = []
        spare_array = []

        # determine which words contribute to the feeling of joy
        key_words = []
        words = word_tokenize(my_scenario)
        # cleaned scenario removes meaningless stopwords, punctuation and case
        cleaned_scenario = [word for word in words if not word.lower() in stop_words and word not in string.punctuation]
        # cleaned_scenario.remove(word1)
        cleaned_scenario = [word.lower() for word in cleaned_scenario]
        cleaned_scenario = [word for word in cleaned_scenario if len(word) > 2]
        # stem is a way to cut down a word so that variations of the word can be recognized
        stemmed_scenario = [stemmer.stem(word) for word in cleaned_scenario]

        # match words in our joy lexicon
        common_words = [word for word in stemmed_scenario if word in stemmed_joy_words]
        size_s = len(cleaned_scenario)

        # round about way of unstemming words that matched in the lexicon
        for i in range(size_s):
            temp_string = stemmer.stem(cleaned_scenario[i])
            if temp_string in common_words:
                joy_array.append(cleaned_scenario[i])

        # these are the words that did not contribute to joy and can be used as distractors
        for i in range(size_s):
            if cleaned_scenario[i] not in joy_array:
                spare_array.append(cleaned_scenario[i])

        # print("Keep or try again?")
        # print(my_scenario)
        # print(joy_array)
        # print(spare_array)
        # user_input = input("Y/N")
        if 1 < len(joy_array) < 6:
            # add to dataframe
            df.loc[len(df.index)] = [my_scenario, joy_array, spare_array]
        else:
            print("failed")
            self.generate_function(df)

        return


    def array_to_vec(self, array, model):
        # Filter words in array that are in the model's vocabulary
        vectors = [model[word] for word in array if word in model.key_to_index]
        # Compute the mean of the vectors, handling the case where vectors might be empty
        if vectors:
            array_vec = sum(vectors) / len(vectors)
        else:
            # Handle the case where the array has no words that are in the model's vocabulary
            # This could return zeros in the same dimension as the model's vectors
            # Adjust the dimensions (e.g., 300 for GoogleNews vectors) as necessary
            array_vec = np.zeros(model.vector_size)
        return array_vec


    def sort_array_match(self, string, array):
        # Split the string into individual words
        words = string.split()

        # Create a dictionary to map each word to its index in the string
        word_indices = {word: index for index, word in enumerate(words)}

        # Sort the array based on the indices obtained from the dictionary
        sorted_array = sorted(array, key=lambda word: word_indices.get(word, float('inf')))

        return sorted_array


    def random_choice_gen(self, input_arr, options_arr):
        my_list = []
        random_string = random.choice(options_arr)
        if random_string not in input_arr:
            input_arr.append(random_string)
            return input_arr
        else:
            return self.random_choice_gen(input_arr, options_arr)


    def confusion_function(self, df):
        array_return = []
        for i in range(1):
            row_index = random.randint(1,1000)
            scenario_string = df.iloc[row_index]['Scenario']
            joy_words = df.iloc[row_index]['joy_keywords']
            # Convert from an array looking string into an array
            joy_words = ast.literal_eval(joy_words)
            spare_words = df.iloc[row_index]['spare_words']
            # Convert from an array looking string into an array
            spare_words = ast.literal_eval(spare_words)
            test_options = []

            # let's grab two words randomly from both list
            for j in range(2):
                test_options = self.random_choice_gen(test_options, joy_words)
            for j in range(2):
                test_options = self.random_choice_gen(test_options, spare_words)

            # let's sort them so that they appear in the same order as the scenario
            test_options = self.sort_array_match(scenario_string, test_options)

            # I'm not sure how Chanel wants to implement this part so here is a quick and dirty placeholder
            print("Scenario: ", scenario_string)
            print("These four words occur in the scenario:", test_options)
            print("Two are keywords that help to identify joy. Which two?")
            user_input = input("Type 0 if it doesn't contribute and 1 if it does. Submit four numbers ex: 1001")

            for j in range(4):
                if user_input[j] == '1':
                    if test_options[j] in joy_words:
                        print(f'Correct! {test_options[j]} is a keyword!')
                    else:
                        print(f'Sorry, {test_options[j]} is not a keyword')

                if user_input[j] == '0':
                    if test_options[j] in joy_words:
                        print(f'Sorry, {test_options[j]} is a keyword')
                        array_return.append(test_options[j])
                    else:
                        print(f'correct, {test_options[j]} is not a keyword')

        return array_return


    def calibration_function(self, df, confusion_array):
        try:
            # load the model we made using gensim and scipy
            model = KeyedVectors.load("word2vec.model", mmap='r')

            # calculate the vector of our confusion array
            vec_c = self.array_to_vec(confusion_array, model)

            # Iterate through each row in the dataframe and update the score column
            for index, row in df.iterrows():
                # Grab the array of key_words for the current scenario
                key_words = row['joy_keywords']
                key_words = ast.literal_eval(key_words)
                # calculate the vector of the current scenario key_words array
                vec_d = self.array_to_vec(key_words, model)
                # Calculate the cosine similarity between the two vectors
                similarity = 1 - spatial.distance.cosine(vec_c, vec_d)
                # store the value in the database
                df.at[index, 'Similarity Score'] = similarity

            sorted_df = df.sort_values(by='Similarity Score')
            sorted_df.to_csv('calibrated.csv', index=False)
        except:
            print("This is working in the other file")
        


# generating database code -------------------------
# load hidden variables
#load_dotenv()
# Create a DataFrame
# blank_array = []
# df = pd.DataFrame({
#     'Scenario': [""],
#     'joy_keywords': [blank_array],
#     'spare_words': [blank_array]
# })
#
# for i in range(10):
#     generate_function(df)
#
# df.to_csv('test.csv', index=False)
# generating database code -------------------------

# start
# load the dataset into a dataframe
#df = pd.read_csv('joy_dataframe.csv')
#print("Starting calibration, answer a few questions:")
# function to find confusion array
#confusion_array = confusion_function(df)
#print("These were the keywords they missed that we will use to calibrate the database")
#print("confusion array: ", confusion_array)
# Lets calibrate. Callibration function
#calibration_function(df, confusion_array)
