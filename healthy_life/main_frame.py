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

class Mainframe_App(tkinter.Tk):

    APP_NAME = "HEALTHY LIFE MAIN FRAME"
    SIZE = "550x650"

    def __init__(self, id_usuari):

        customtkinter.set_appearance_mode("Dark")

        self.root_tk = tkinter.Tk()
        self.root_tk.geometry(Mainframe_App.SIZE)
        self.root_tk.title(Mainframe_App.APP_NAME)

        """ DATABASES """
        self.envasats_db = EnvasatsDB(DATA_PATH + "productes_db.csv")
        self.usuaris_db = UsuarisDB(DATA_PATH + "usuaris_db.csv")
        self.rebost_db = RebostDB(DATA_PATH + "rebost_db.csv")
        # Afegir la resta!

        """ USER """
        self.id_usuari = id_usuari

        # ============ Main Frame ============

        self.main_frame = customtkinter.CTkFrame(master=self.root_tk,
                                        width=420,
                                        height=420,
                                        corner_radius=10)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        """ Add quantitat """
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

if __name__ == "__main__":
    app = Mainframe_App(0)
