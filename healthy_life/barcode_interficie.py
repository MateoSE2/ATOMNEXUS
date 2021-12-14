import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import *
from PIL import ImageTk, Image
import os

def interficie(path,name,macros):

    customtkinter.set_appearance_mode("Dark")

    APP_NAME = "HEALTHY LIFE DAILY CONTROL"
    SIZE = "550x650"

    root_tk = tkinter.Tk() 
    root_tk.geometry(SIZE)
    root_tk.title(APP_NAME)

    def f():
        global C
        C = int(entry.get())
        root_tk.quit()        
    
    def button_event():
        pass
    
    # ============ create CTkFrame ============

    frame = customtkinter.CTkFrame(master=root_tk,
                                                width=420,
                                                height=420,
                                                corner_radius=10)
    frame.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    frame_rebost = customtkinter.CTkFrame(master=root_tk,
                                                width=500,
                                                height=100,
                                                corner_radius=10)
    frame_rebost.place(relx=0.5, rely=0.87, anchor=tkinter.CENTER)

    # ============ frame ============

    img = Image.open(path).resize((200, 200))
    img = img.transpose(Image.ROTATE_270) 

    img = ImageTk.PhotoImage(img)

    button_1 = customtkinter.CTkButton(master=frame, image=img, text="", width=60, height=60,
                                   corner_radius=10, command=button_event)
    
    button_1.place(relx=0.5, rely=0.05, anchor=tkinter.N)

    #label = Label(image = img)
    #label.pack(padx=0.5, pady=50)



    label_name = customtkinter.CTkLabel(master=frame,
                                                   text= name ,
                                                   width=250,
                                                   height=40,
                                                   corner_radius=8,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)

    label_name.place(relx=0.5, rely=0.57, anchor=tkinter.N)

    label_info = customtkinter.CTkLabel(master=frame,
                                                   text= "Macros per cada 100 g:\n\n"+
                                                        "    Carbohidrats: " + str(macros[0])+ " g\n" +
                                                        "    Proteines: " + str(macros[1])+ " g\n" +
                                                        "    Greixos: " + str(macros[2])+ " g",
                                                   width=250,
                                                   height=100,
                                                   corner_radius=8,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)

    label_info.place(relx=0.5, rely=0.70, anchor=tkinter.N)
    """
    button_guardar = customtkinter.CTkButton(master=frame,
                                                text="Guardar al rebost",
                                                command=lambda: print("a"),
                                                border_width=0,
                                                corner_radius=8)

    button_guardar.place(relx=0.3, rely=0.85, anchor=tkinter.S)

    button_no_guardar = customtkinter.CTkButton(master=frame,
                                                text="No guardar al rebost",
                                                command=lambda: print("a"),
                                                border_width=0,
                                                corner_radius=8)

    button_no_guardar.place(relx=0.7, rely=0.85, anchor=tkinter.S)
    """

    label_qtty = customtkinter.CTkLabel(master=frame_rebost,
                                                   text= "Introdueix quantitat per guardar el rebost: " ,
                                                   width=300,
                                                   height=40,
                                                   corner_radius=8,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)

    label_qtty.place(relx=0.05, rely=0.5, anchor=tkinter.W)

    entry = customtkinter.CTkEntry(master=frame_rebost,
                                            width=20,
                                            height=25,
                                            corner_radius=8)
    entry.place(relx=0.67, rely=0.5, anchor=tkinter.W)
    entry.insert(0, "1")

    button_no_guardar = customtkinter.CTkButton(master=frame_rebost,
                                                text="Guardar",
                                                command=f,
                                                border_width=0,
                                                corner_radius=8)

    button_no_guardar.place(relx=0.72, rely=0.5, anchor=tkinter.W)


    root_tk.mainloop()
    try:
        return C
    except:
        return False
    

    

"""
if __name__ == "__main__":
    c = interficie("images/barcode_formatge.jpg","Grana Padano - Hacendado",[0,33,29])
    print(c)
"""
