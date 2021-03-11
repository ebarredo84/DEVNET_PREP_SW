import tkinter as tk
from enauto.enauto_gui_class_ebo import *
#from spauto.sauto_gui_class_ebo import *
#from dcauto.sauto_gui_class_ebo import *
#from sauto.sauto_gui_class_ebo import *
#from clauto.sauto_gui_class_ebo import *

#from devnet_gui_functions_ebo import *

DEVNET_MENU="""BIENVENIDO!
1) ENAUTO 300-435
2) SPAUTO 300-535
3) DCAUTO 300-635
4) SAUTO  300-735
5) CLAUTO 300-835
¿Cual deseas practicar?"""

class DEVNET_MAIN_WINDOW:
    def __init__(self,window0):
        #VENTANA
        window0.geometry("1300x500")
        window0.title("DEVNET PREP SOFTWARE")
        #CUADRO DE TEXTO
        text_box0=tk.Text(window0,width=159,height=25)     #creo el objeto para poner texto
        text_box0.place(x=0,y=0)
        text_box0.insert("1.0",DEVNET_MENU)
        text_box0.config(state="disabled")               #solo lectura
        #CUADRO DE ENTRADA
        entry0=tk.Entry(window0,fg="blue",bg="white",
                            width=25)                   #creo el objeto de escritura
        entry0.place(x=5,y=410)
        #BOTON FW
        button_fw0=tk.Button(window0,text="Select",
                fg="black",bg="grey",
                width=5,height=1,
                command=lambda:self.SELECT(entry0))          #creo el objeto del botón
        button_fw0.place(x=5,y=435)
        #BOTON EXIT
        button_exit0=tk.Button(window0,text="Exit",
                fg="black",bg="grey",
                width=5,height=1,
                command=window0.destroy)          #creo el objeto del botón
        button_exit0.place(x=55,y=435)

    def SELECT(self,entry0):
        ans=entry0.get()
#---------------------------------------------------------
#-----------------ENAUTO PREPARATION----------------------
#---------------------------------------------------------
        if ans=="1":
            app=tk.Tk()                              #creo el objeto de la ventana
            window=ENAUTO_MAIN_WINDOW(app)
            app.mainloop() 
#---------------------------------------------------------
#-----------------SPAUTO PREPARATION----------------------
#---------------------------------------------------------
#        elif ans=="2":
#            app=tk.Tk()                              #creo el objeto de la ventana
#            window=SAUTO_MAIN_WINDOW(app)
#            app.mainloop()
#---------------------------------------------------------
#-----------------DCAUTO PREPARATION----------------------
#---------------------------------------------------------
#        elif ans=="3":
#            app=tk.Tk()                              #creo el objeto de la ventana
#            window=SAUTO_MAIN_WINDOW(app)
#            app.mainloop()
#---------------------------------------------------------
#-----------------SAUTO PREPARATION----------------------
#---------------------------------------------------------
#        elif ans=="4":
#            app=tk.Tk()                              #creo el objeto de la ventana
#            window=SAUTO_MAIN_WINDOW(app)
#            app.mainloop()
#---------------------------------------------------------
#-----------------CLAUTO PREPARATION----------------------
#---------------------------------------------------------
#        elif ans=="5":
#            app=tk.Tk()                              #creo el objeto de la ventana
#            window=SAUTO_MAIN_WINDOW(app)
#            app.mainloop()

app0=tk.Tk()                              #creo el objeto de la ventana
window0=DEVNET_MAIN_WINDOW(app0)
app0.mainloop()