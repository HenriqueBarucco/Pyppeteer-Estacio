from tkinter import *

class kabum_scrapping_screen:

    def __init__(self):
        self.window = Tk()
        #definir os objetos a serem instaciados pelas entrys


    def show_screen(self):
        self.window.title('Pyppeter Estacio')
        self.window.geometry('500x500')
        self.setup_label()
        self.setup_entry()
        self.setup_buton()
        self.window.resizable(False,False)
        self.window.mainloop()


    def setup_label(self):
        lbl_title = Label(self.window, text= 'Kabum Scrapping',font=("Arial", 30))
        lbl_title.place(relx=0.5,rely=0.4,anchor=CENTER)    
        
        lbl_entry_product = Label(self.window,text='Produto',font=('Arial',15))
        lbl_entry_product.place(relx=0.2,rely=0.5,anchor=CENTER)

        lbl_entry_phone = Label(self.window,text='Telefone',font=('Arial',15))
        lbl_entry_phone.place(relx=0.2,rely=0.6,anchor=CENTER)

    def setup_entry(self):

        product_txtfld = Entry(self.window,bd=5)
        product_txtfld.place(relx=0.5,rely=0.5,anchor=CENTER)

        phone_txtfld = Entry(self.window,bd=5)
        phone_txtfld.place(relx=0.5,rely=0.6,anchor=CENTER)


#definir o command do botao
    def setup_buton(self):
        go_btn = Button(self.window,text='Iniciar',bg='black',fg='white',command=lambda: print('agua mineraaaal'))
        go_btn.place(relx=0.5,rely=0.7,anchor=CENTER)