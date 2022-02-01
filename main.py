from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Gdelivery')
root.geometry('800x600')
root.config(background = 'black')
root.resizable(width = False, height = False)
root.iconbitmap('assets/delivey.ico')



# Imagem de fundo
imageLogo = PhotoImage(file= "assets/backgroundDelivery.png")
background = Label(image=imageLogo)
background.place(x=0,y=0, relwidth=1,relheight=1)


# Chamar o Função botao
def game():  
    board = Toplevel()
    board.title('Gdelivery')
    board.geometry('800x600')
    board.resizable(width = False, height = False)
    board.iconbitmap('assets/delivey.ico')
    
    #ABRE O MAPA
    imagemTabuleiro = PhotoImage(file = "assets/mapaBrasilia.png")
    Tabuleiro = Label(board, image=imagemTabuleiro)
    Tabuleiro.place(x=0,y=0,relwidth=1,relheight=1)
    
    #FUNÇAO de movimento
    def on_move(event):
        component=event.widget
        locx, locy = component.winfo_x(), component.winfo_y()
        w , h =board.winfo_width(),board.winfo_height()
        mx ,my =component.winfo_width(),component.winfo_height()
        xpos=(locx+event.x)-(15)
        ypos=(locy+event.y)-int(my/2)
        if xpos>=0 and ypos>=0 and w-abs(xpos)>=0 and h-abs(ypos)>=0 and xpos<=w-5 and ypos<=h-5:
            component.place(x=xpos,y=ypos)
    

   
    board.mainloop()

   
   

# Butões do Menu
butaoNew = Button(root, text='Adicionar endereço',padx=65,pady=5,fg='snow',bg='black',command = game)
butaoNew.place(relx=0.5,rely=0.1,anchor=CENTER)
butaoPvP = Button(root,text='Mapa rota',padx=90,pady=5,fg='snow',bg='black',command = game)
butaoPvP.place(relx=0.5,rely=0.2,anchor=CENTER)
butaoExit = Button(root,text='SAIR',padx=117,pady=5,fg='snow',bg='black',command=root.quit)
butaoExit.place(relx=0.5,rely=0.5,anchor=CENTER)



root.mainloop()