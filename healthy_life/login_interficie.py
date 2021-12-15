import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import *
from PIL import ImageTk, Image
import os

class Login_App:

    APP_NAME = "HEALTHY LIFE LOGIN"
    SIZE = "550x650"

    def __init__(self):

        customtkinter.set_appearance_mode("Dark")

        self.root_tk = tkinter.Tk()
        self.root_tk.geometry(Login_App.SIZE)
        self.root_tk.title(Login_App.APP_NAME)

        self.user = None
        self.password = None

        # ============ Frame Project ============

        self.frame_project = customtkinter.CTkFrame(master=self.root_tk,
                                        width=420,
                                        height=100,
                                        corner_radius=10)
        self.frame_project.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.label_name = customtkinter.CTkLabel(master=self.frame_project,
                                           text= "HEALTHY LIFE" ,
                                           width=250,
                                           height=40,
                                           corner_radius=8,
                                           fg_color=("white", "gray38"),  # <- custom tuple-color
                                           justify=tkinter.LEFT)

        self.label_name.place(relx=0.5, rely=0.3, anchor=tkinter.N)

        # ============ Frame Login ============

        self.frame_login = customtkinter.CTkFrame(master=self.root_tk,
                                        width=420,
                                        height=200,
                                        corner_radius=10)
        self.frame_login.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        """ USER """
        self.user_label = customtkinter.CTkLabel(master=self.frame_login,
                                                   text="User:",
                                                   width=180,
                                                   height=20,
                                                   justify=tkinter.CENTER)
        self.user_label.place(relx=0.2, rely=0.2, anchor=tkinter.CENTER)


        self.user_entry = customtkinter.CTkEntry(master=self.frame_login,
                                                    width=200,
                                                    height=25,
                                                    corner_radius=8)
        self.user_entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        """ PASSWORD """

        self.password_label = customtkinter.CTkLabel(master=self.frame_login,
                                                   text="Password:",
                                                   width=180,
                                                   height=20,
                                                   justify=tkinter.CENTER)
        self.password_label.place(relx=0.17, rely=0.4, anchor=tkinter.CENTER)


        self.password_entry = customtkinter.CTkEntry(master=self.frame_login,
                                                    width=200,
                                                    height=25,
                                                    corner_radius=8)
        self.password_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)


        # ============ Login Button ============

        self.login_button = customtkinter.CTkButton(master=self.frame_login,
                                                height=25,
                                                text="Enter",
                                                command=self.button_event_login,
                                                border_width=0,
                                                corner_radius=8)
        self.login_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    def start(self):
        self.root_tk.mainloop()

    def button_event_login(self):
        user = self.user_entry.get()
        password = self.password_entry.get()
        self.user = user
        self.password = password
        self.root_tk.quit()

if __name__ == "__main__":
    app = Login_App()
    app.start()
    print(app.user, app.password)
