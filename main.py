from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Gdelivery')
root.geometry('800x600')
root.config(background = 'black')
root.resizable(width = False, height = False)
root.iconbitmap('assets/delivey.ico')

imag_1 = PhotoImage(file= "assets/backgroundDelivery.png")
imag_2 = PhotoImage(file = "assets/mapaBrasilia.png")
imag_3 = PhotoImage(file = "assets/va_va_land.png")

imageList = [imag_1, imag_2, imag_3]

# Imagem de fundo
background = Label(image=imag_1)
background.grid(row = 0, column = 0, columnspan = 3)
#background.place(x=0,y=0, relwidth=1,relheight=1)

def show_map():
    global background
    background.grid_forget()
    background = Label(image=imag_2)
    background.grid(row = 1, column = 0, columnspan = 3)

    button_back = Button(root,text='Back',padx=117,pady=5,fg='snow',bg='black',command=back)
    button_back.place(relx=0.5,rely=0.9,anchor=CENTER)

def show_path():
    global background
    background.grid_forget()
    background = Label(image=imag_3)
    background.grid(row = 1, column = 0, columnspan = 3)

    button_back = Button(root,text='Back',padx=117,pady=5,fg='snow',bg='black',command=back)
    button_back.place(relx=0.5,rely=0.9,anchor=CENTER)


def back():
    
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row = 0, column = 0, columnspan = 3)

    butaoNew = Button(root, text='Visualizar Mapa',padx=85,pady=5,fg='snow',bg='black',command = show_map)
    butaoNew.place(relx=0.5,rely=0.1,anchor=CENTER)

    butaoPvP = Button(root,text='Calcular Rota',padx=90,pady=5,fg='snow',bg='black',command = show_path)
    butaoPvP.place(relx=0.5,rely=0.2,anchor=CENTER)

    butaoExit = Button(root,text='SAIR',padx=117,pady=5,fg='snow',bg='black',command=root.quit)
    butaoExit.place(relx=0.5,rely=0.5,anchor=CENTER)
   

# Butões do Menu
butaoNew = Button(root, text='Visualizar Mapa',padx=85,pady=5,fg='snow',bg='black',command = show_map)
butaoNew.place(relx=0.5,rely=0.1,anchor=CENTER)

butaoPvP = Button(root,text='Calcular Rota',padx=90,pady=5,fg='snow',bg='black',command = show_path)
butaoPvP.place(relx=0.5,rely=0.2,anchor=CENTER)

butaoExit = Button(root,text='SAIR',padx=117,pady=5,fg='snow',bg='black',command=root.quit)
butaoExit.place(relx=0.5,rely=0.5,anchor=CENTER)



root.mainloop()