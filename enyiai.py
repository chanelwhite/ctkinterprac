import tkinter
import customtkinter
from functools import partial

class Page(customtkinter.CTk):
    def __init__(self):
        self.frame = None
        self.button1 = None
        self.button2 = None
        self.label = None
        self.entry = None

    def set_frame(self, f):
         self.frame = f
    def get_frame(self):
         return self.frame

    def set_label(self, f):
         self.label = f
    def get_label(self):
         return self.label

    def set_button1(self, b):
         self.button1 = b
    def get_button1(self):
         return self.button1
    
    def set_button2(self, f):
         self.button2 = f
    def get_button2(self):
         return self.button2
    
    def set_entry(self, e):
         self.entry = e
    def get_entry(self):
         return self.entry
    
    
class User():
     id = -1
     def __init__(self, name):
          self.name = name
          User.id += 1
          self.uid = User.id
          

     def get_name(self) -> str:
          return self.name
     
     def get_id(self) -> int:
          return self.uid


    
 

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("blue")
main_container = customtkinter.CTk()
main_container.geometry("700x600")
main_container.title("EnyiAi")


frames = [Page(), Page(), Page()]
users = []

def get_user_name():
        new_u =  User(frames[0].get_entry().get())
        name = new_u.get_name()
        id = new_u.get_id()
        print(name, id)
        frames[0].get_entry().delete(0, len(name))
        return name

def make_frame3():
    '''Code for the third frame'''
    clear_frames()
    frames[2].set_frame(customtkinter.CTkFrame(master=main_container, fg_color="blue")) 
    frames[2].set_label(customtkinter.CTkLabel(master=frames[2].get_frame(), text= "Welcome to the third page"))
    frames[2].get_frame().pack(pady = 20, padx=60, fill="both", expand=True)
    frames[2].get_label().pack(pady=30, padx=10)
    frames[2].set_button1(customtkinter.CTkButton(master=frames[2].get_frame(), text="Login", command=make_main))
    frames[2].get_button1().pack(pady=12, padx=30, side=customtkinter.BOTTOM)
    

def make_frame2():
    '''Code for the second frame'''
    # TODO: figure out how to get the name to stay persistent across pages
    n = get_user_name()
    clear_frames()
    
    #frames[0].get_frame().destroy()      
    frames[1].frame = customtkinter.CTkFrame(master=main_container, fg_color="blue")
    frames[1].frame.pack(pady = 20, padx=60, fill="both", expand=True)
    
    frames[1].label = customtkinter.CTkLabel(master=frames[1].frame, text= f"Welcome to the scenario trainer, {n}")
    frames[1].label.pack(pady=30, padx=10)
    frames[1].entry = customtkinter.CTkTextbox(master=frames[1].frame, height=100, width=200)
    frames[1].entry.pack(pady=12, padx=20, side=customtkinter.BOTTOM)
    frames[1].button1 = customtkinter.CTkButton(master=frames[1].frame, text="Login", command=make_frame3)        
    frames[1].button1.pack(pady=12, padx=30)
def create_nav():
     left_side_panel = customtkinter.CTkFrame(main_container, width=50, corner_radius=8, fg_color="grey")
     left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=2, pady=20)
     home_button= customtkinter.CTkButton(master=left_side_panel, text="Home", command=make_main)
     home_button.pack(pady=12, padx=10)
     emotion_button = customtkinter.CTkButton(master=left_side_panel, text="Emotion Detector", command=make_frame3)
     #button2.pack(pady=12, padx=10)
     emotion_button.pack(pady=12, padx=10)
     scenario_button = customtkinter.CTkButton(master=left_side_panel, text="Practice Scenarios", command=make_frame2)
     scenario_button.pack(pady=12, padx=10)
     
def clear_frames():
     if frames[2].get_frame() != None:
          frames[2].get_frame().destroy()
     if frames[0].get_frame() != None:
         frames[0].get_frame().destroy()
     if frames[1].get_frame() != None:
         frames[1].get_frame().destroy()

def make_main():
     clear_frames()     
     frames[0].set_frame(customtkinter.CTkFrame(master=main_container, fg_color="#34e5eb"))
     frames[0].get_frame().pack(pady = 20, padx=10, fill="both", expand=True)
     frames[0].set_label(customtkinter.CTkLabel(master=frames[0].get_frame(), font= ("Roboto", 30), text= "Welcome to \nEnyiAi\nPlease enter your name"))
     frames[0].get_label().pack(pady=30, padx=10)
     frames[0].set_entry(customtkinter.CTkEntry(master=frames[0].get_frame(), placeholder_text="Name", text_color="white"))
     frames[0].get_entry().pack(pady=12, padx=20)
     #n = get_name()
     




if __name__ == "__main__":
      create_nav()
      make_main()
      
      main_container.mainloop()