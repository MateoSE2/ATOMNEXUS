import tkinter
import tkinter.messagebox
from tkinter import filedialog
import customtkinter
from tkinter import *
from PIL import ImageTk, Image
import os

from usuaris_db import UsuarisDB
from productes_db import EnvasatsDB, GranelDB
from rebost_db import RebostDB

DATA_PATH = "./data/"
USER_PATH = "./users/"
IMAGES_PATH = "./images/"
"""
class Mainframe_App(tkinter.Tk):

    APP_NAME = "HEALTHY LIFE MAIN FRAME"
    SIZE = "550x650"

    def __init__(self, id_usuari):

        customtkinter.set_appearance_mode("Dark")

        self.root_tk = tkinter.Tk()
        self.root_tk.geometry(Mainframe_App.SIZE)
        self.root_tk.title(Mainframe_App.APP_NAME)

        """ "DATABASES" """
        self.envasats_db = EnvasatsDB(DATA_PATH + "productes_db.csv")
        self.usuaris_db = UsuarisDB(DATA_PATH + "usuaris_db.csv")
        self.rebost_db = RebostDB(DATA_PATH + "rebost_db.csv")
        # Afegir la resta!

        """ "USER" """
        self.id_usuari = id_usuari

        # ============ Main Frame ============

        self.main_frame = customtkinter.CTkFrame(master=self.root_tk,
                                        width=420,
                                        height=420,
                                        corner_radius=10)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        """ "Add quantitat" """
        self.afegir_producte = customtkinter.CTkButton(master=self.main_frame,
                                                    text="Afegir producte",
                                                    command=self.button_event_afegir_producte,
                                                    width=200,
                                                    height=25,
                                                    corner_radius=8)
        self.afegir_producte.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.root_tk.mainloop()

    def button_event_afegir_producte(self):
        self.root_tk.withdraw()
        #self.root_tk.attributes('-topmost', True)
        path_image = filedialog.askopenfilename()
        self.usuaris_db.add_product_from_codebar(self.envasats_db,
                                                 self.id_usuari,
                                                 path_image,
                                                 self.rebost_db)
"""

import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import *
from PIL import ImageTk, Image
import os

class Mainframe_App(tkinter.Tk):

    APP_NAME = "MAINFRAME"
    SIZE = "500x300"

    def __init__(self, id_usuari):

        customtkinter.set_appearance_mode("Dark")

        self.root_tk = tkinter.Tk()
        self.root_tk.geometry(Mainframe_App.SIZE)
        self.root_tk.title(Mainframe_App.APP_NAME)

        # ============ Main Frame ============

        self.frame = customtkinter.CTkFrame(master=self.root_tk,
                                            width=420,
                                            height=250,
                                            corner_radius=10)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        """ PROFILE IMAGE"""

        img = Image.open(USER_PATH+str(id_usuari)+".png").resize((50, 50))
        img = ImageTk.PhotoImage(img)

        self.image = customtkinter.CTkButton(master=self.frame,
                                            image=img,
                                            text="",
                                            width=10,
                                            height=10,
                                            corner_radius=10)

        self.image.place(relx=0.07, rely=0.15, anchor=tkinter.W)

        """ USER NAME """
        self.label_name = customtkinter.CTkLabel(master=self.frame,
                                                       text="Gerard",
                                                       width=70,
                                                       height=30,
                                                       corner_radius=8,
                                                       fg_color=("white", "gray38"),  # <- custom tuple-color
                                                       justify=tkinter.LEFT)

        self.label_name.place(relx=0.21, rely=0.15, anchor=tkinter.W)

        """ HEALTHY LIFE """
        self.label_info = customtkinter.CTkLabel(master=self.frame,
                                                       text= "HEALTHY LIFE",
                                                       width=250,
                                                       height=80,
                                                       corner_radius=8,
                                                       fg_color=("white", "#2d8c22"), # <- custom tuple-color
                                                       text_font=("Arial",25),  
                                                       justify=tkinter.LEFT)

        self.label_info.place(relx=0.4, rely=0.17, anchor=tkinter.W)

        ### CAMERA ###
        """
        self.guardar = customtkinter.CTkButton(master=self.frame,
                                                    text="Guardar",
                                                    command=lambda: print("A"),
                                                    border_width=0,
                                                    corner_radius=8)

        self.guardar.place(relx=0.5, rely=0.5, anchor=tkinter.W)

        """
        
        camera = ImageTk.PhotoImage(Image.open(IMAGES_PATH + "camera.jpg").resize((60, 60)))

        """ CAMERA """
        self.camera = customtkinter.CTkLabel(master=self.frame,
                                                       text="Escaneja el codi de barres",
                                                       image = camera,
                                                       width=60,
                                                       height=60,
                                                       corner_radius=8,
                                                       fg_color=("white", "gray38"),  # <- custom tuple-color
                                                       justify=tkinter.LEFT)

        self.camera.place(relx=0.07, rely=0.5, anchor=tkinter.W)

        self.label_camera = customtkinter.CTkLabel(master=self.frame,
                                                       text="Escaneja el codi de barres",
                                                       width=200,
                                                       height=30,
                                                       corner_radius=8,
                                                       fg_color=("white", "gray38"),  # <- custom tuple-color
                                                       justify=tkinter.LEFT)

        self.label_camera.place(relx=0.25, rely=0.5, anchor=tkinter.W)

        """ CALENDAR """

        calendar = ImageTk.PhotoImage(Image.open(IMAGES_PATH + "calendar.jpg").resize((60, 60)))

        self.calendar = customtkinter.CTkLabel(master=self.frame,
                                                       text="Escaneja el codi de barres",
                                                       image = calendar,
                                                       width=60,
                                                       height=60,
                                                       corner_radius=8,
                                                       fg_color=("white", "gray38"),  # <- custom tuple-color
                                                       justify=tkinter.LEFT)

        self.calendar.place(relx=0.07, rely=0.75, anchor=tkinter.W)

        self.label_calendar = customtkinter.CTkLabel(master=self.frame,
                                                       text="Control diari",
                                                       width=200,
                                                       height=30,
                                                       corner_radius=8,
                                                       fg_color=("white", "gray38"),  # <- custom tuple-color
                                                       justify=tkinter.LEFT)

        self.label_calendar.place(relx=0.25, rely=0.75, anchor=tkinter.W)


        self.root_tk.mainloop()

    def guardar_quantitat(self):

        self.new_quantitat = int(self.entry.get())
        self.root_tk.quit()

if __name__ == "__main__":
    app = Mainframe_App(0)
