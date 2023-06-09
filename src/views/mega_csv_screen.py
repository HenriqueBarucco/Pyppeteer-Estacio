from tkinter import Button, Entry, Label, Tk 

from tkinter import messagebox

from tkinter import filedialog
import re

from src.entities.person import Person 

from src.app import run_application
from src.views.helpers.navigate_helper import navigate_helper

class mega_csv:


    def __init__(self):

        self.window = Tk()

        self.email_entry = None

        self.password_entry = None

        self.login_photo_button = None

        self.phone_entry = None

        self.dir_entry = None

        self.frame = self.window


    def create_login_screen(self):

        self.window.title("Pyppeter Estacio")

        self.window.geometry("600x500")

        self.window.configure(bg="white")
        self.draw_screen()

        self.window.mainloop()


    def draw_screen(self):

        #CRIANDO OS WIDGETS

        login_label = Label(

            self.frame, text="Iniciar", bg='white', fg="black", font=("Arial", 30),
        )

        email_label = Label(

    self.frame, text="Email", bg='white', fg="black", font=("Arial", 16))

        dir_label = Label(self.frame,text="Diretório:",bg='white', fg="black", font=("Arial", 16))

        dir_button = Button(

        self.frame, text="Selecionar", bg="black", fg="#FFFFFF", font=("Arial", 16), command=self.open_directory_dialog
    )

        self.email_entry = Entry(self.frame,font=("Arial",16),width=40)

        self.password_entry = Entry(self.frame,show="*",font=("Arial",16),width=40)

        self.phone_entry = Entry(self.frame,font=("Arial",16),width=40)

        password_label = Label(

    self.frame, text="Senha", bg='white', fg="black", font=("Arial", 16))

        phone_label = Label(

    self.frame, text="Telefone", bg='white', fg="black", font=("Arial", 16))

        login_button = Button(self.frame, text="Iniciar", bg="black", fg="#FFFFFF", font=("Arial", 16), command=self.validate_login,border=10)

        back_btn = Button(self.window,text="Voltar", bg='black',fg='white',command=lambda: navigate_helper._navigate_back_to_main(window=self.window) )
        back_btn.place(relx= 0.9,rely=0.9)
        #POSICIONANDO NA TELA 
        

        login_label.grid(row=0, column=0,columnspan=2,  sticky="news", pady=40)

        email_label.grid(row=1, column=0)

        self.email_entry.grid(row=1, column=1, pady=20)

        password_label.grid(row=2, column=0)

        phone_label.grid(row=3, column=0)

        dir_label.grid(row=4,column=0,sticky="e")

        self.password_entry.grid(row=2, column=1, pady=20)

        self.phone_entry.grid(row=3, column=1, pady=20)

        dir_button.grid(row=4, column=1, columnspan=2, pady=10,sticky="news")

        login_button.grid(row=5, column=0, columnspan=2, pady=30)


    

    #def show_custom_dialog():

      #  dialog = tk.Toplevel()

      #  dialog.title("AUTO-ESTACIO")


    def open_directory_dialog(self):

        selected_directory = filedialog.askdirectory(initialdir="~")

        self.dir_entry = selected_directory



    def validate_login(self):

        username = self.email_entry.get()

        email_pattern = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"


        if  re.match(email_pattern, username) and self.dir_entry != None:

            person = Person(phone=self.phone_entry.get(),email=self.email_entry.get(),
            password=self.password_entry.get(),directory=self.dir_entry)



            message = messagebox.showinfo("Alerta", "Iniciando o procedimento, do usuario " + username.split('@')[0] + "! " + "em " +self.dir_entry )

            if message == 'ok':

                            run_application(person)

        else:

            messagebox.showerror("falha", "o email digitado não é um email ou não foi selecionado um diretório.")
            

