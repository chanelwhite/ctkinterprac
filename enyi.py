import tkinter
import customtkinter
from functools import partial

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("blue")

class Enyi(customtkinter.CTk):
    frames = {}
    current = None
    bg = ""
    main_container = None

    def __init__(self):
        super().__init__()
        self.bg = self.cget("fg_color")
        self.num_of_frames = 0
        # self.state('withdraw')
        self.title("EnyiAi")

        # screen size
        self.geometry("800x600")

        # root!
        main_container = customtkinter.CTkFrame(self, corner_radius=8, fg_color=self.bg)
        main_container.pack(fill=tkinter.BOTH, expand=True, padx=8, pady=8)

        self.frame = customtkinter.CTkFrame(master=main_container, fg_color="#34e5eb")
        self.frame.pack(pady = 20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, font= ("Roboto", 30), text= "Welcome to \nEnyiAi\nPlease enter your name")
        self.label.pack(pady=30, padx=10)

        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Name", text_color="blue")
        self.entry1.pack(pady=12, padx=20)

        self.button1 = customtkinter.CTkButton(master=self.frame, text="Practice Scenarios", command=self.make_frame2)
        #button1.pack(pady=12, padx=10)
        self.button1.pack(pady=12, padx=30, side=customtkinter.LEFT)

        self.button2 = customtkinter.CTkButton(master=self.frame, text="Emotion Detector", command=self.get_name)
        #button2.pack(pady=12, padx=10)
        self.button2.pack(pady=12, padx=40, side=customtkinter.RIGHT)  

  


    #grabs the name from the name box
    def get_name(self):
        name = self.entry1.get()
        print(name)
        self.entry1.delete(0, len(name))
        
        return name

    def make_frame2(self, parent=main_container):
        '''Code for the second frame'''
        n = self.get_name()
        self.frame.destroy()      
        frame2 = customtkinter.CTkFrame(master=parent, fg_color="blue")
        frame2.pack(pady = 20, padx=60, fill="both", expand=True)
        
        label2 = customtkinter.CTkLabel(master=frame2, text= f"Welcome to the scenario trainer, {n}")
        label2.pack(pady=30, padx=10)
        t_box = customtkinter.CTkTextbox(master=frame2, height=100, width=200)
        t_box.pack(pady=12, padx=20, side=customtkinter.BOTTOM)
        button3 = customtkinter.CTkButton(master=frame2, text="Login", command=self.get_name)        
        button3.pack(pady=12, padx=30)
        
        
enyi = Enyi()
enyi.mainloop()