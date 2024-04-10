import tkinter
import customtkinter
from functools import partial
from PIL import Image

class Page(customtkinter.CTk):
    frame = None
    
    def set_frame(self, f):
         self.frame = f

    def get_frame(self):
         return self.frame
    
    def create_label(self, text, parent):
         self.label = customtkinter.CTkLabel(master=parent.get_frame(), text= text)
         return self.label
          
    def get_entry(self):
         return self.entry
    
    def create_entry(self, parent):
        self.entry = customtkinter.CTkEntry(master=parent.get_frame(), placeholder_text="Name", text_color="white")
        return self.entry

    def create_button(self, t, com, parent):
         self.button = customtkinter.CTkButton(master=parent.get_frame(), text= t, command=com)
         self.button.pack(pady=12, padx=30, side=customtkinter.BOTTOM)
         return self.button
         
    
    
class User():
     id = -1
     def __init__(self, name):
          self.name = name
          User.id += 1
          self.uid = User.id
          self.active = False
          

     def get_name(self) -> str:
          return self.name
     
     def get_id(self) -> int:
          return self.uid
     
     def set_active(self):
          '''Sets whether the user is logged in or not'''
          self.active = not self.active

     def get_active(self):
          '''Returns active status'''
          return self.active

    
 

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("blue")
main_container = customtkinter.CTk()
main_container.geometry("700x600")
main_container.title("EnyiAi")


frames = [Page(), Page(), Page()]
user = []

def create_user_name():
     '''Creates a new user'''
     if User(frames[0].get_entry().get()) not in user:
          new_u =  User(frames[0].get_entry().get())
          frames[0].get_entry().delete(0, len(new_u.get_name()))
          user.append(new_u)
     return new_u.get_name()
     

def logout(u: User):
     u.set_active()


def make_frame3():
    '''Code for the third frame'''
    clear_frames()
    n = user[0].get_name()
    frames[2].set_frame(customtkinter.CTkFrame(master=main_container, fg_color="blue"))
    frames[2].get_frame().pack(pady = 20, padx=60, fill="both", expand=True)
    label = frames[2].create_label(f"Welcome to the third page {n}", frames[2])
    label.pack(pady = 20, padx=60, fill="both", expand=True)
    button1 = frames[2].create_button("button 2", print("test create"), frames[2])
    button1.pack(pady=20, padx=30)
    frames[2].create_button("button 3", main, frames[2])
    

def make_frame2():
    '''Code for the second frame'''
    clear_frames()
    n = user[0].get_name()
        
    frames[1].set_frame(customtkinter.CTkFrame(master=main_container, fg_color="blue"))
    frames[1].get_frame().pack(pady = 20, padx=60, fill="both", expand=True)
    
    
    label= frames[1].create_label(f"Welcome to the scenario trainer {n}", frames[1])
    label.pack(pady=30, padx=10)
    entry = frames[1].create_entry(frames[1])
    entry.pack(pady=12, padx=20, side=customtkinter.BOTTOM)
    button1 = frames[1].create_button("Login", make_frame3, frames[1])

    button1.pack(pady=12, padx=30)

def make_frame1():
     pass
     

def create_nav():
     left_side_panel = customtkinter.CTkFrame(main_container, width=50, corner_radius=8, fg_color="grey")
     left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=2, pady=20)
     home_button= customtkinter.CTkButton(master=left_side_panel, text="Home", command=main)
     home_button.pack(pady=12, padx=10)
     emotion_button = customtkinter.CTkButton(master=left_side_panel, text="Calibration", command=make_frame3)
     
     emotion_button.pack(pady=12, padx=10)
     scenario_button = customtkinter.CTkButton(master=left_side_panel, text="Practice Scenarios", command=make_frame2)
     scenario_button.pack(pady=12, padx=10)
     settings_button = customtkinter.CTkButton(master=left_side_panel, text="Settings", command= make_frame1)
     settings_button.pack(pady=12, padx=10)
     
def clear_frames():
     if frames[2].get_frame() != None:
          frames[2].get_frame().destroy()
     if frames[0].get_frame() != None:
         frames[0].get_frame().destroy()
     if frames[1].get_frame() != None:
         frames[1].get_frame().destroy()

def main():
     '''Makes the main frame of the app'''
     clear_frames()     
     frames[0].set_frame(customtkinter.CTkFrame(master=main_container, fg_color="#34e5eb"))
     frames[0].get_frame().pack(pady = 20, padx=10, fill="both", expand=True)
     label= frames[0].create_label("Welcome to \nEnyiAi\nPlease enter your name", frames[0])
     label.pack(pady=30, padx=10)
     entry= frames[0].create_entry(frames[0])
     entry.pack(pady=30, padx=10)
     button = frames[0].create_button("Sign In", create_user_name, frames[0])
     button.pack(pady=30, padx=10)
     
     




if __name__ == "__main__":
      create_nav()
      main()
      
      main_container.mainloop()