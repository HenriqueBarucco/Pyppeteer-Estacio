import tkinter as tk
from tkinter import messagebox
import re 

class login_screen:


    def __init__(self):
        self.window = tk.Tk()
        self.username_entry = None
        self.password_entry = None
        self.login_photo_button = None
        self.telefone_entry = None
        self.frame = tk.Frame(bg='white')

    def create_login_screen(self):
        self.window.title("Login Screen")
        self.window.geometry("900x500")
        self.window.configure(bg="white")
        self.draw_screen()



        self.window.mainloop()



    def draw_screen(self):

        #CRIANDO OS WIDGETS
        login_label = tk.Label(
            self.frame, text="Login", bg='white', fg="black", font=("Arial", 30)
        )
        username_label = tk.Label(
    self.frame, text="Email", bg='white', fg="black", font=("Arial", 16))
        self.username_entry = tk.Entry(self.frame,font=("Arial",16))
        self.password_entry = tk.Entry(self.frame,show="*",font=("Arial",16))
        self.telefone_entry = tk.Entry(self.frame,show="*",font=("Arial",16))
        password_label = tk.Label(
    self.frame, text="Senha", bg='white', fg="black", font=("Arial", 16))
        telefone_label = tk.Label(
    self.frame, text="Telefone", bg='white', fg="black", font=("Arial", 16))
        login_button = tk.Button(self.frame, text="Login", bg="#bb86ff", fg="#FFFFFF", font=("Arial", 16), command=self.validate_login)
        
        #POSICIONANDO NA TELA 
        
        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=20)
        password_label.grid(row=2, column=0)
        telefone_label.grid(row=3, column=0)
        self.password_entry.grid(row=2, column=1, pady=20)
        self.telefone_entry.grid(row=3, column=1, pady=20)
        login_button.grid(row=4, column=0, columnspan=2, pady=30)
        self.frame.pack()

   
    def validate_login(self):
        username = self.username_entry.get()
        
        email_pattern = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

        if  re.match(email_pattern, username):
            messagebox.showinfo("Login bem sucedido", "Iniciando o procedimento, " + username.split('@')[0] + "!")
        else:
            messagebox.showerror("O login falhou", "o email digitado não é um email.")    


