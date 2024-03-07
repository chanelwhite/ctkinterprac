import tkinter
import customtkinter
#from functools import partial


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("650x600")
root.title("EnyiAi")


#grabs the name from the name box
def get_name():
    name = entry1.get()
    print(name)
    entry1.delete(0, len(name))
    
    return name


def make_frame2():
    '''Code for the second frame'''
    n= get_name()    
    frame2 = customtkinter.CTkFrame(master=root, fg_color="blue")
    label2 = customtkinter.CTkLabel(master=frame2, text= f"Welcome to the scenario trainer, {n}")
    t_box = customtkinter.CTkTextbox(master=frame2, height=100, width=200)
    button3 = customtkinter.CTkButton(master=frame2, text="Login", command=make_frame3)
    frame2.pack(pady = 20, padx=60, fill="both", expand=True)
    label2.pack(pady=30, padx=10)
    button3.pack(pady=12, padx=30)
    t_box.pack(pady=12, padx=20, side=customtkinter.BOTTOM)
    return frame2

def make_frame3():
    '''Code for the third frame'''
    frame3 = customtkinter.CTkFrame(master=root, fg_color="blue")
    label3 = customtkinter.CTkLabel(master=frame3, text= "Welcome to the third page")
    frame3.pack(pady = 20, padx=60, fill="both", expand=True)
    label3.pack(pady=30, padx=10)
    button = customtkinter.CTkButton(master=frame3, text="Login", command=make_frame1)
    button.pack(pady=12, padx=30, side=customtkinter.BOTTOM)
    return frame3

def make_frame1():
    '''Code for the first frame'''
   
    frame = customtkinter.CTkFrame(master=root, fg_color="#34e5eb")
    frame.pack(pady = 20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, font= ("Roboto", 30), text= "Welcome to \nEnyiAi\nPlease enter your name")
    label.pack(pady=30, padx=10)
    global entry1
    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Name", text_color="blue")
    entry1.pack(pady=12, padx=20)

    button1 = customtkinter.CTkButton(master=frame, text="Practice Scenarios", command=get_name )
    #button1.pack(pady=12, padx=10)
    button1.pack(pady=12, padx=10, side=customtkinter.LEFT)
    

    button2 = customtkinter.CTkButton(master=frame, text="Emotion Detector", command=make_frame2)
    #button2.pack(pady=12, padx=10)
    button2.pack(pady=12, padx=10, side=customtkinter.RIGHT)
    return frame
        


make_frame1()
root.mainloop()
