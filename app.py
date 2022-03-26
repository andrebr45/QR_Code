#BIBLIOTECAS NECESSÁRIAS
#--------------------------------------
# importamos o módulo os
import os as sistema
import os
from tkinter import font
import qrcode
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.messagebox as MessageBox
from tkinter import ttk
#--------------------------------------
#CONTADOR DA VERIFICACAO DOS ARQUIVOS
cont = []
#--------------------------------------

# vamos obter o nome do usuário logado no sistema
usuario = sistema.getlogin()

#CONFIG - LÓGICA DO MENU
valor_menu = [2]
def abrir_menu():
   #VERIFICA SE O MENU ESTA ABERTO
   if sum(valor_menu) == 1 :
       barra_menu.place_forget()
       #-----------------------------------------------
       valor_menu[0] = 2

   elif sum(valor_menu) == 2:
       barra_menu.place(y=82,height=390,width=200)
       valor_menu[0] = 1
#-------------------------------------------------------
def atualiza_foto_texto():
   mensagem["text"]= " "
   l_logo3.place_forget()
#-----------------------------------------------
#FUNCAO QUE GERA O QRCODE -PRINCIPAL
#-----------------------------------------------------------------------

def qr(event=None):
  global logo3, l_logo3
  if textolink.get()=="":
        MessageBox.showinfo("Status", "O Campo de Link está vazio")
        atualiza_foto_texto()

  else:

       qr = qrcode.QRCode(version=1,
                     box_size=20,
                     border=2)
       data= textolink.get()
       qr.add_data(data)
       qr.make(fit=True)

       os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))
       
       image = qr.make_image(fill_color='black', back_color="white")

       if(os.path.exists('qrcode.png')):
          print("O arquivo existe")
          image.save(f"qrcode{sum(cont)}.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode{sum(cont)}.png')

       else:
          print("O arquivo não existe")
          image.save("qrcode.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode.png')

       #CONTA O NUMERO DE ARQUVIOS CRIADOS   
       cont.append(1)
       print(cont)
       #----------------------------------
      
       #MENSAGEM DE FINALIZACAO
       textolink.delete(0, 'end')
       status = '''Gerado com Sucesso!
       Área de Trabalho'''
       mensagem["text"]= status

       #CRIAANDO A IMAGEM QR
       logo3 = Image.open(f'{ba}')
       logo3 = logo3.resize((140,140), Image.ANTIALIAS)
       logo3 = ImageTk.PhotoImage(logo3)
       #LABEL IMAGEM QR CRIADA
       l_logo3 = Label(frame, image=logo3, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#3b3b3b')
       l_logo3.place(x=228,y=330)
       #----------------------------------------------------------------

#IMAGEM M1
def m1():
   global logo3, l_logo3
   if textolink.get()=="":
          MessageBox.showinfo("Status", "O Campo de Link está vazio")
          atualiza_foto_texto()

   else:
       barra_menu.place_forget()
       valor_menu[0] = 2
       qr = qrcode.QRCode(version=1,
                     box_size=20,
                     border=2)
       data= textolink.get()
       qr.add_data(data)
       qr.make(fit=True)

       os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))
       
       image = qr.make_image(fill_color='white', back_color="blue")

       if(os.path.exists('qrcode.png')):
          print("O arquivo existe")
          image.save(f"qrcode{sum(cont)}.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode{sum(cont)}.png')
          
       else:
          print("O arquivo não existe")
          image.save("qrcode.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode.png')

       #CONTA O NUMERO DE ARQUVIOS CRIADOS   
       cont.append(1)
       print(cont)
       #----------------------------------
              #----------------------------------
      
       #MENSAGEM DE FINALIZACAO
       textolink.delete(0, 'end')
       status = '''Gerado com Sucesso!
  Na Área de Trabalho'''
       mensagem["text"]= status

       #CRIAANDO A IMAGEM QR
       logo3 = Image.open(f'{ba}')
       logo3 = logo3.resize((140,140), Image.ANTIALIAS)
       logo3 = ImageTk.PhotoImage(logo3)
       #LABEL IMAGEM QR CRIADA
       l_logo3 = Label(frame, image=logo3, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#3b3b3b')
       l_logo3.place(x=228,y=330)
       #----------------------------------------------------------------
          

#IMAGEM M2
def m2():
   global logo3, l_logo3
   if textolink.get()=="":
          MessageBox.showinfo("Status", "O Campo de Link está vazio")
          atualiza_foto_texto()

   else:
       barra_menu.place_forget()
       valor_menu[0] = 2
       qr = qrcode.QRCode(version=1,
                     box_size=20,
                     border=2)
       data= textolink.get()
       qr.add_data(data)
       qr.make(fit=True)

       os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))
       
       image = qr.make_image(fill_color='black', back_color="red")

       if(os.path.exists('qrcode.png')):
          print("O arquivo existe")
          image.save(f"qrcode{sum(cont)}.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode{sum(cont)}.png')

       else:
          print("O arquivo não existe")
          image.save("qrcode.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode.png')

       #CONTA O NUMERO DE ARQUVIOS CRIADOS   
       cont.append(1)
       print(cont)
       #----------------------------------
              #----------------------------------
      
       #MENSAGEM DE FINALIZACAO
       textolink.delete(0, 'end')
       status = '''Gerado com Sucesso!
  Na Área de Trabalho'''
       mensagem["text"]= status

       #CRIAANDO A IMAGEM QR
       logo3 = Image.open(f'{ba}')
       logo3 = logo3.resize((140,140), Image.ANTIALIAS)
       logo3 = ImageTk.PhotoImage(logo3)
       #LABEL IMAGEM QR CRIADA
       l_logo3 = Label(frame, image=logo3, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#3b3b3b')
       l_logo3.place(x=228,y=330)
       #----------------------------------------------------------------

#novos
#IMAGEM M3
def m3():
   global logo3, l_logo3
   if textolink.get()=="":
          MessageBox.showinfo("Status", "O Campo de Link está vazio")
          atualiza_foto_texto()

   else:
       barra_menu.place_forget()
       valor_menu[0] = 2
       qr = qrcode.QRCode(version=1,
                     box_size=20,
                     border=2)
       data= textolink.get()
       qr.add_data(data)
       qr.make(fit=True)

       os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))
       
       image = qr.make_image(fill_color='black', back_color="#6f9fbd")

       if(os.path.exists('qrcode.png')):
          print("O arquivo existe")
          image.save(f"qrcode{sum(cont)}.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode{sum(cont)}.png')

       else:
          print("O arquivo não existe")
          image.save("qrcode.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode.png')

       #CONTA O NUMERO DE ARQUVIOS CRIADOS   
       cont.append(1)
       print(cont)
       #----------------------------------
              #----------------------------------
      
       #MENSAGEM DE FINALIZACAO
       textolink.delete(0, 'end')
       status = '''Gerado com Sucesso!
  Na Área de Trabalho'''
       mensagem["text"]= status

       #CRIAANDO A IMAGEM QR
       logo3 = Image.open(f'{ba}')
       logo3 = logo3.resize((140,140), Image.ANTIALIAS)
       logo3 = ImageTk.PhotoImage(logo3)
       #LABEL IMAGEM QR CRIADA
       l_logo3 = Label(frame, image=logo3, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#3b3b3b')
       l_logo3.place(x=228,y=330)
       #----------------------------------------------------------------
          

#IMAGEM M4
def m4():
   global logo3, l_logo3
   if textolink.get()=="":
          MessageBox.showinfo("Status", "O Campo de Link está vazio")
          atualiza_foto_texto()

   else:
       barra_menu.place_forget()
       valor_menu[0] = 2
       qr = qrcode.QRCode(version=1,
                     box_size=20,
                     border=2)
       data= textolink.get()
       qr.add_data(data)
       qr.make(fit=True)

       os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))
       
       image = qr.make_image(fill_color='white', back_color="blue")

       if(os.path.exists('qrcode.png')):
          print("O arquivo existe")
          image.save(f"qrcode{sum(cont)}.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode{sum(cont)}.png')

       else:
          print("O arquivo não existe")
          image.save("qrcode.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode.png')


       #CONTA O NUMERO DE ARQUVIOS CRIADOS   
       cont.append(1)
       print(cont)
       #----------------------------------
              #----------------------------------
      
       #MENSAGEM DE FINALIZACAO
       textolink.delete(0, 'end')
       status = '''Gerado com Sucesso!
  Na Área de Trabalho'''
       mensagem["text"]= status

       #CRIAANDO A IMAGEM QR
       logo3 = Image.open(f'{ba}')
       logo3 = logo3.resize((140,140), Image.ANTIALIAS)
       logo3 = ImageTk.PhotoImage(logo3)
       #LABEL IMAGEM QR CRIADA
       l_logo3 = Label(frame, image=logo3, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#3b3b3b')
       l_logo3.place(x=228,y=330)
       #----------------------------------------------------------------

#novos
#IMAGEM M5
def m5():
   global logo3, l_logo3
   if textolink.get()=="":
          MessageBox.showinfo("Status", "O Campo de Link está vazio")
          atualiza_foto_texto()

   else:
       barra_menu.place_forget()
       valor_menu[0] = 2
       qr = qrcode.QRCode(version=1,
                     box_size=20,
                     border=2)
       data= textolink.get()
       qr.add_data(data)
       qr.make(fit=True)

       os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))
       
       image = qr.make_image(fill_color='white', back_color="red")

       if(os.path.exists('qrcode.png')):
          print("O arquivo existe")
          image.save(f"qrcode{sum(cont)}.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode{sum(cont)}.png')

       else:
          print("O arquivo não existe")
          image.save("qrcode.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode.png')

       #CONTA O NUMERO DE ARQUVIOS CRIADOS   
       cont.append(1)
       print(cont)
       #----------------------------------
              #----------------------------------
      
       #MENSAGEM DE FINALIZACAO
       textolink.delete(0, 'end')
       status = '''Gerado com Sucesso!
  Na Área de Trabalho'''
       mensagem["text"]= status

       #CRIAANDO A IMAGEM QR
       logo3 = Image.open(f'{ba}')
       logo3 = logo3.resize((140,140), Image.ANTIALIAS)
       logo3 = ImageTk.PhotoImage(logo3)
       #LABEL IMAGEM QR CRIADA
       l_logo3 = Label(frame, image=logo3, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#3b3b3b')
       l_logo3.place(x=228,y=330)
       #----------------------------------------------------------------
          

#IMAGEM M6
def m6():
   global logo3, l_logo3
   if textolink.get()=="":
          MessageBox.showinfo("Status", "O Campo de Link está vazio")
          atualiza_foto_texto()

   else:
       barra_menu.place_forget()
       valor_menu[0] = 2
       qr = qrcode.QRCode(version=1,
                     box_size=20,
                     border=2)
       data= textolink.get()
       qr.add_data(data)
       qr.make(fit=True)

       os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))
       
       image = qr.make_image(fill_color='white', back_color="green")

       if(os.path.exists('qrcode.png')):
          print("O arquivo existe")
          image.save(f"qrcode{sum(cont)}.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode{sum(cont)}.png')

       else:
          print("O arquivo não existe")
          image.save("qrcode.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode.png')

       #CONTA O NUMERO DE ARQUVIOS CRIADOS   
       cont.append(1)
       print(cont)
       #----------------------------------
              #----------------------------------
      
       #MENSAGEM DE FINALIZACAO
       textolink.delete(0, 'end')
       status = '''Gerado com Sucesso!
  Na Área de Trabalho'''
       mensagem["text"]= status

       #CRIAANDO A IMAGEM QR
       logo3 = Image.open(f'{ba}')
       logo3 = logo3.resize((140,140), Image.ANTIALIAS)
       logo3 = ImageTk.PhotoImage(logo3)
       #LABEL IMAGEM QR CRIADA
       l_logo3 = Label(frame, image=logo3, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#3b3b3b')
       l_logo3.place(x=228,y=330)
       #----------------------------------------------------------------

#novos
#IMAGEM M7
def m7():
   global logo3, l_logo3
   if textolink.get()=="":
          MessageBox.showinfo("Status", "O Campo de Link está vazio")
          atualiza_foto_texto()

   else:
       barra_menu.place_forget()
       valor_menu[0] = 2
       qr = qrcode.QRCode(version=1,
                     box_size=20,
                     border=2)
       data= textolink.get()
       qr.add_data(data)
       qr.make(fit=True)

       os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))
 
       image = qr.make_image(fill_color='white', back_color="purple")

       if(os.path.exists('qrcode.png')):
          print("O arquivo existe")
          image.save(f"qrcode{sum(cont)}.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode{sum(cont)}.png')

       else:
          print("O arquivo não existe")
          image.save("qrcode.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode.png')

       #CONTA O NUMERO DE ARQUVIOS CRIADOS   
       cont.append(1)
       print(cont)
       #----------------------------------
              #----------------------------------
      
       #MENSAGEM DE FINALIZACAO
       textolink.delete(0, 'end')
       status = '''Gerado com Sucesso!
  Na Área de Trabalho'''
       mensagem["text"]= status

       #CRIAANDO A IMAGEM QR
       logo3 = Image.open(f'{ba}')
       logo3 = logo3.resize((140,140), Image.ANTIALIAS)
       logo3 = ImageTk.PhotoImage(logo3)
       #LABEL IMAGEM QR CRIADA
       l_logo3 = Label(frame, image=logo3, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#3b3b3b')
       l_logo3.place(x=228,y=330)
       #----------------------------------------------------------------
          

#IMAGEM M8
def m8():
   global logo3, l_logo3
   if textolink.get()=="":
          MessageBox.showinfo("Status", "O Campo de Link está vazio")
          atualiza_foto_texto()
          
   else:
       barra_menu.place_forget()
       valor_menu[0] = 2
       qr = qrcode.QRCode(version=1,
                     box_size=20,
                     border=2)
       data= textolink.get()
       qr.add_data(data)
       qr.make(fit=True)

       os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))
       
       image = qr.make_image(fill_color='white', back_color="black")

       if(os.path.exists('qrcode.png')):
          print("O arquivo existe")
          image.save(f"qrcode{sum(cont)}.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode{sum(cont)}.png')

       else:
          print("O arquivo não existe")
          image.save("qrcode.png")
          ba = (f'C:/Users/{usuario}/Desktop/qrcode.png')
          
       #CONTA O NUMERO DE ARQUVIOS CRIADOS   
       cont.append(1)
       print(cont)
       #----------------------------------
              #----------------------------------
      
       #MENSAGEM DE FINALIZACAO
       textolink.delete(0, 'end')
       status = '''Gerado com Sucesso!
  Na Área de Trabalho'''
       mensagem["text"]= status

       #CRIAANDO A IMAGEM QR
       logo3 = Image.open(f'{ba}')
       logo3 = logo3.resize((140,140), Image.ANTIALIAS)
       logo3 = ImageTk.PhotoImage(logo3)
       #LABEL IMAGEM QR CRIADA
       l_logo3 = Label(frame, image=logo3, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#3b3b3b')
       l_logo3.place(x=228,y=330)
       #----------------------------------------------------------------

#CONFIG TELA
#---------------------------------
janela = Tk()
janela.geometry("600x500+400+100")
janela.title("Gerador de QR Code")
janela.iconbitmap("images/icone.ico")
#---------------------------------
#FRAME PRINCIPAL
#---------------------------------
frame = Frame(janela, bg='#3b3b3b')
frame.place(width=600,height=500,)

titulotexto = Label(frame, text="QR Code", font=("ARIAL BLACK",25),bg='#3b3b3b',fg="#feffff")
titulotexto.pack(pady = 10)

texto1 = Label(frame, text="Insira o seu link para gerar", font=("bold",13),bg='#3b3b3b',fg="#feffff")
texto1.place(x=200,y = 185)

textolink = Entry(frame, text="",font=("bold",13))
textolink.place(x=80, y=230, width=400, height=25)

mensagem = Label(frame, text=" ",font=("ARIAL BLACK",10),bg="#3b3b3b",fg="#feffff")
mensagem.pack(pady=198)

#IMAGENS PAGINA PRINCIPAL
#-------------------------------------------------
#IMAGEM QRCODE TITULO
#-------------------------------------------------
logo = Image.open('images/fundo_qr_wa1.png')
logo = logo.resize((120,120), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
#LABEL IMAGEM
l_logo = Label(janela, image=logo, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#3b3b3b')
l_logo.place(x=240,y=50)
#-------------------------------------------------
#IMAGEM INSERIR LINK NO QRCODE
logo1 = Image.open('images/link.png')
logo1 = logo1.resize((50,50), Image.ANTIALIAS)
logo1 = ImageTk.PhotoImage(logo1)
#LABEL IMAGEM LINK QRCODE
l_logo1 = Label(janela, image=logo1, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#3b3b3b')
l_logo1.place(x=20,y=217)
#-------------------------------------------------
#IMAGEM BOTAO
logo2 = Image.open('images/bt.png')
logo2 = logo2.resize((80,70), Image.ANTIALIAS)
logo2 = ImageTk.PhotoImage(logo2)
#LABEL IMAGEM BOTAO
l_logo2 =  Button(janela, command=qr, image=logo2, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#3b3b3b',bd=0,activebackground="#3b3b3b")
l_logo2.place(x=495,y=205)
#-------------------------------------------------
#-----------------------------------------------
#BARRA MENU LATERAL
#-----------------------------------------------
#-----------------------------------------------
#CRIA IMAGEM MENU
#-----------------------------------------------
im_clie_user = Image.open('images/menubar.png')
im_clie_user = im_clie_user.resize((50,50), Image.ANTIALIAS)
im_clie_user = ImageTk.PhotoImage(im_clie_user)
#-----------------------------------------------
#CARREGA IMAGEM MENU
#-----------------------------------------------
l_clie_user= Button(janela, image=im_clie_user, compound=LEFT, anchor='nw', bg="#3b3b3b",bd=0,activebackground="#3b3b3b", command=abrir_menu)
l_clie_user.place(x=25,y=14)
#-----------------------------------------------

#FRAME MENU VERTICAL 
#-----------------------------------------------
barra_menu = Frame(janela,bg="#6f9fbd",highlightbackground="#feffff",highlightthickness=1)

#-----------------------------------------------

#-----------------------------------------------
#BARRA MENU LATERAL
#-----------------------------------------------
texto_menu = Label(barra_menu, text="Modelos Disponíveis", font=("ARIAL BLACK",12),bg='#6f9fbd',fg="#feffff")
texto_menu.pack(pady = 10)

linha_menu = ttk.Separator(barra_menu, orient=HORIZONTAL)
linha_menu.place(x=0, y=50,width=199)
#-------------------------------------------------
#IMAGEM M1
m_m1 = Image.open('modelos/m1.png')
m_m1 = m_m1.resize((50,50), Image.ANTIALIAS)
m_m1 = ImageTk.PhotoImage(m_m1)
#LABEL IMAGEM BOTAO
l_m_m1 =  Button(barra_menu, command=m1, image=m_m1, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#6f9fbd',bd=0,activebackground="#3b3b3b")
l_m_m1.place(x=30,y=60)

linha_menu1 = ttk.Separator(barra_menu, orient=HORIZONTAL)
linha_menu1.place(x=30, y=125,width=133)

linha_menu2 = ttk.Separator(barra_menu, orient=VERTICAL)
linha_menu2.place(x=95, y=70,height=270)
#-------------------------------------------------

#IMAGEM M2
m_m2 = Image.open('modelos/m2.png')
m_m2 = m_m2.resize((50,50), Image.ANTIALIAS)
m_m2 = ImageTk.PhotoImage(m_m2)
#LABEL IMAGEM BOTAO
l_m_m2 =  Button(barra_menu, command=m2, image=m_m2, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#6f9fbd',bd=0,activebackground="#3b3b3b")
l_m_m2.place(x=110,y=60)

linha_menu3 = ttk.Separator(barra_menu, orient=HORIZONTAL)
linha_menu3.place(x=30, y=205,width=133)
#-------------------------------------------------

#IMAGEM M3
m_m3 = Image.open('modelos/m3.png')
m_m3 = m_m3.resize((50,50), Image.ANTIALIAS)
m_m3 = ImageTk.PhotoImage(m_m3)
#LABEL IMAGEM BOTAO
l_m_m3 =  Button(barra_menu, command=m3, image=m_m3, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#6f9fbd',bd=0,activebackground="#3b3b3b")
l_m_m3.place(x=30,y=140)

linha_menu4 = ttk.Separator(barra_menu, orient=HORIZONTAL)
linha_menu4.place(x=30, y=285,width=133)
#-------------------------------------------------

#IMAGEM M4
m_m4 = Image.open('modelos/m4.png')
m_m4 = m_m4.resize((50,50), Image.ANTIALIAS)
m_m4 = ImageTk.PhotoImage(m_m4)
#LABEL IMAGEM BOTAO
l_m_m4 =  Button(barra_menu, command=m4, image=m_m4, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#6f9fbd',bd=0,activebackground="#3b3b3b")
l_m_m4.place(x=110,y=140)
#-------------------------------------------------

#IMAGEM M5
m_m5 = Image.open('modelos/m5.png')
m_m5 = m_m5.resize((50,50), Image.ANTIALIAS)
m_m5 = ImageTk.PhotoImage(m_m5)
#LABEL IMAGEM BOTAO
l_m_m5 =  Button(barra_menu, command=m5, image=m_m5, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#6f9fbd',bd=0,activebackground="#3b3b3b")
l_m_m5.place(x=30,y=220)
#-------------------------------------------------

#IMAGEM M6
m_m6 = Image.open('modelos/m6.png')
m_m6 = m_m6.resize((50,50), Image.ANTIALIAS)
m_m6 = ImageTk.PhotoImage(m_m6)
#LABEL IMAGEM BOTAO
l_m_m6 =  Button(barra_menu, command=m6, image=m_m6, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#6f9fbd',bd=0,activebackground="#3b3b3b")
l_m_m6.place(x=110,y=220)
#-------------------------------------------------

#IMAGEM M7
m_m7 = Image.open('modelos/m7.png')
m_m7 = m_m7.resize((50,50), Image.ANTIALIAS)
m_m7 = ImageTk.PhotoImage(m_m7)
#LABEL IMAGEM BOTAO
l_m_m7 =  Button(barra_menu, command=m7, image=m_m7, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#6f9fbd',bd=0,activebackground="#3b3b3b")
l_m_m7.place(x=30,y=300)
#-------------------------------------------------

#IMAGEM M8
m_m8 = Image.open('modelos/m8.png')
m_m8 = m_m8.resize((50,50), Image.ANTIALIAS)
m_m8 = ImageTk.PhotoImage(m_m8)
#LABEL IMAGEM BOTAO
l_m_m8 =  Button(barra_menu, command=m8, image=m_m8, compound=LEFT, font=('Ivy 10 bold'), anchor='nw',bg='#6f9fbd',bd=0,activebackground="#3b3b3b")
l_m_m8.place(x=110,y=300)
#-------------------------------------------------
def teste22(Event):
     barra_menu.place_forget()
     valor_menu[0] = 2

janela.bind('<Return>', qr)

frame.bind('<Button-1>',teste22)
janela.mainloop()
