#------USER INTERFACE (VIEW)----------
import tkinter as tk

#------CONTROLLER--------------------
import json
import base64

#----------SECUNDARY WINDOW----------
class SECUNDARY_WINDOW:
    def __init__(self,window2,msg):
        #VENTANA
        window2.geometry("600x100")
        window2.title("ASK PARAMETER")
        #CUADRO DE TEXTO
        text_box2=tk.Text(window2,width=75,height=25)     #creo el objeto para poner texto
        text_box2.place(x=0,y=0)
        text_box2.insert("1.0",str(msg))
        text_box2.config(state="disabled")               #solo lectura
        #CUADRO DE ENTRADA
        self.entry2=tk.Entry(window2,fg="blue",bg="white",
                            width=40)                   #creo el objeto de escritura
        self.entry2.place(x=5,y=35)
        #BOTON FW
        button_fw2=tk.Button(window2,text="Send",
                fg="black",bg="grey",
                width=5,height=1,
                command=window2.quit)          #creo el objeto del botón
        button_fw2.place(x=5,y=60)
        #BOTON EXIT
        #button_exit2=tk.Button(window2,text="Exit",
        #        fg="black",bg="grey",
        #        width=5,height=1,
        #        command=window2.destroy)          #creo el objeto del botón
        #button_exit2.place(x=55,y=60)

    def SEND(self,window2):
        param=self.entry2.get()
        return param

def ASK_PARAMETER(msg):
    app2=tk.Tk()
    window2=SECUNDARY_WINDOW(app2,msg)
    app2.mainloop()
    parameter=window2.SEND(window2)
    app2.destroy()
    
    return parameter

#--------ERASE AND PRINT FUNCTIONS-------------
def PRINT_STATUS_CODE(response,text_box):
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto
    text_box.insert("1.0","Request status: "+str(response.status_code)+"\n")
    text_box.config(state="disabled")               #solo lectura

def PRINT_HEADERS(headers,text_box):
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto
    text_box.insert("1.0","Headers: "+str(headers)+"\n")
    text_box.config(state="disabled")               #solo lectura

#--------PRINT FUNCTIONS----------------------
def PRINT_RESPONSE_JSON(resp,text_box):
    response_json = resp.json()                                     
    json_formatted_str = json.dumps(response_json, indent=4)
    #IMPRIMO EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.insert(tk.END,json_formatted_str+"\n")
    text_box.config(state="disabled")               #solo lectura

def PRINT_RESPONSE(resp,text_box):
    json_formatted_str = json.dumps(resp, indent=4)
    #IMPRIMO EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.insert(tk.END,json_formatted_str+"\n")
    text_box.config(state="disabled")               #solo lectura

def PRINT_CONTENT_JSON(resp,text_box):
    json_formatted_str=json.dumps(json.loads(resp.content),indent=4)
    #IMPRIMO EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.insert(tk.END,json_formatted_str+"\n")
    text_box.config(state="disabled")               #solo lectura

def PRINT_TABLE_IN_TEXT(text_box,dictionary,**kwargs):
    num_arg=len(kwargs)

    text_box.config(state="normal")
    #----------IMPRIME 2 KEY PAIRS VALUES
    if num_arg==6:
        print_header='{0:'+kwargs['size1']+'s}{1:1}{2:'+kwargs['size2']+'s}'
        text_box.insert(tk.END,print_header.format(kwargs['name1'], "|", 
                                                    kwargs['name2'])+"\n")
        text_box.insert(tk.END,'-'*140+"\n")
        d1=kwargs['data1']
        d2=kwargs['data2']
        for ITEM in dictionary:
            text_box.insert(tk.END,print_header.format(str(ITEM[d1]),"|", 
                                                        str(ITEM[d2]))+"\n")
    #----------IMPRIME 3 KEY PAIRS VALUES---------------
    elif num_arg==9:
        print_header='{0:'+kwargs['size1']+'s}{1:1}{2:'+kwargs['size2']+'s}{3:1}{4:'+kwargs['size3']+'s}'
        text_box.insert(tk.END,print_header.format(kwargs['name1'], "|",
                                                    kwargs['name2'], "|", 
                                                    kwargs['name3'])+"\n")
        text_box.insert(tk.END,'-'*140+"\n")
        d1=kwargs['data1']
        d2=kwargs['data2']
        d3=kwargs['data3']
        for ITEM in dictionary:
            text_box.insert(tk.END,print_header.format(str(ITEM[d1]),"|", 
                                                        str(ITEM[d2]), "|", 
                                                        str(ITEM[d3]))+"\n")
    #----------IMPRIME 4 KEY PAIRS VALUES---------------
    elif num_arg==12:
        print_header='{0:'+kwargs['size1']+'s}{1:1}{2:'+kwargs['size2']+'s}{3:1}{4:'+kwargs['size3']+'s}{5:1}{6:'+kwargs['size4']+'s}'
        text_box.insert(tk.END,print_header.format(kwargs['name1'], "|",
                                                    kwargs['name2'], "|",
                                                    kwargs['name3'], "|", 
                                                    kwargs['name4'])+"\n")
        text_box.insert(tk.END,'-'*140+"\n")
        d1=kwargs['data1']
        d2=kwargs['data2']
        d3=kwargs['data3']
        d4=kwargs['data4']
        for ITEM in dictionary:
            text_box.insert(tk.END,print_header.format(str(ITEM[d1]),"|", 
                                                        str(ITEM[d2]), "|",
                                                        str(ITEM[d3]), "|",
                                                        str(ITEM[d4]))+"\n")
    #----------IMPRIME 5 KEY PAIRS VALUES---------------
    elif num_arg==15:
        print_header='{0:'+kwargs['size1']+'s}{1:1}{2:'+kwargs['size2']+'s}{3:1}{4:'+kwargs['size3']+'s}{5:1}{6:'+kwargs['size4']+'s}{7:1}{8:'+kwargs['size5']+'s}'
        text_box.insert(tk.END,print_header.format(kwargs['name1'], "|",
                                                    kwargs['name2'], "|",
                                                    kwargs['name3'], "|",
                                                    kwargs['name4'], "|", 
                                                    kwargs['name5'])+"\n")
        text_box.insert(tk.END,'-'*140+"\n")
        d1=kwargs['data1']
        d2=kwargs['data2']
        d3=kwargs['data3']
        d4=kwargs['data4']
        d5=kwargs['data5']
        for ITEM in dictionary:
            text_box.insert(tk.END,print_header.format(str(ITEM[d1]),"|", 
                                                        str(ITEM[d2]), "|",
                                                        str(ITEM[d3]), "|",
                                                        str(ITEM[d4]), "|", 
                                                        str(ITEM[d5]))+"\n")    
    #----------IMPRIME 6 KEY PAIRS VALUES---------------
    elif num_arg==18:
        print_header='{0:'+kwargs['size1']+'s}{1:1}{2:'+kwargs['size2']+'s}{3:1}{4:'+kwargs['size3']+'s}{5:1}{6:'+kwargs['size4']+'s}{7:1}{8:'+kwargs['size5']+'s}{9:1}{10:'+kwargs['size6']+'s}'
        text_box.insert(tk.END,print_header.format(kwargs['name1'], "|",
                                                    kwargs['name2'], "|",
                                                    kwargs['name3'], "|",
                                                    kwargs['name4'], "|",
                                                    kwargs['name5'], "|", 
                                                    kwargs['name6'])+"\n")
        text_box.insert(tk.END,'-'*140+"\n")
        d1=kwargs['data1']
        d2=kwargs['data2']
        d3=kwargs['data3']
        d4=kwargs['data4']
        d5=kwargs['data5']
        d6=kwargs['data6']
        for ITEM in dictionary:
            text_box.insert(tk.END,print_header.format(str(ITEM[d1]),"|", 
                                                        str(ITEM[d2]), "|",
                                                        str(ITEM[d3]), "|",
                                                        str(ITEM[d4]), "|",
                                                        str(ITEM[d5]), "|", 
                                                        str(ITEM[d6]))+"\n")
    text_box.config(state="disabled")