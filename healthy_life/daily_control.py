import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Dark")


class App(tkinter.Tk):

    APP_NAME = "HEALTHY LIFE DAILY CONTROL"
    WIDTH = 500
    HEIGHT = 500

    def __init__(self, *args, **kwargs):

        tkinter.Tk.__init__(self, *args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        # ============ create CTkFrame ============

        self.frame = customtkinter.CTkFrame(master=self,
                                                  width=420,
                                                  height=App.HEIGHT-40,
                                                  corner_radius=10)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # ============ frame ============
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame,
                                                   text="Indica els àpats realitzats de la dieta",
                                                   width=250,
                                                   height=50,
                                                   corner_radius=8,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.place(relx=0.5, rely=0.04, anchor=tkinter.N)


        self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame,
                                                     text="Esmorzar")
        self.check_box_1.place(relx=0.4, rely=0.25, anchor=tkinter.W)

        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame,
                                                     text="Dinar")
        self.check_box_2.place(relx=0.4, rely=0.45, anchor=tkinter.W)

        self.check_box_3 = customtkinter.CTkCheckBox(master=self.frame,
                                                     text="Sopar")
        self.check_box_3.place(relx=0.4, rely=0.65, anchor=tkinter.W)

        self.button_1 = customtkinter.CTkButton(master=self.frame,
                                                text="Guardar",
                                                command=self.button_event,
                                                border_width=0,
                                                corner_radius=8)

        self.button_1.place(relx=0.5, rely=0.85, anchor=tkinter.S)

    def button_event(self):
        esmorzar = self.check_box_1.check_state
        dinar = self.check_box_2.check_state
        sopar = self.check_box_3.check_state

        if esmorzar:
            print("esmorzar")
        if dinar:
            print("dinar")
        if sopar:
            print("sopar")
        print("\n")
        

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()