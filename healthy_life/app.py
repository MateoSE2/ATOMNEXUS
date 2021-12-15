import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import *
from PIL import ImageTk, Image
import os
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

from login_interficie import Login_App
from main_frame import Mainframe_App

USERS_PATH = "./users/usuaris_app.csv"

class App:

    APP_NAME = "HEALTHY LIFE"
    SIZE = "550x650"

    def __init__(self):

        # 1. Login
        self.login = Login_App()
        self.login.start()
        print("CLOSE?")

        self.user = self.login.user
        self.password = self.login.password
        self.users_app = pd.read_csv(USERS_PATH, index_col=0)
        self.id_usuari = self.users_app[(self.users_app["nom"] == self.user) &
                                        (self.users_app["password"] == self.password)]["id_usuari"].item()
        print("User:", self.user, "Password:", self.password)
        print("User id:", self.id_usuari)
        self.mainframe = Mainframe_App(self.id_usuari)

if __name__ == "__main__":
    app = App()
