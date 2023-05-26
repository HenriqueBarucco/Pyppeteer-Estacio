from tkinter import CENTER, Button, Label, Tk
from src.views.kabum_scrap_screen import kabum_scrapping_screen
from src.views.mega_csv_screen import mega_csv

class main_screen:

    def __init__(self):
        self.window = Tk()


    def show_screen(self):
        self.window.title('Pyppeter Estacio')
        self.window.geometry('500x500')
        self.setup_label()
        self.setup_buttons()

        self.window.mainloop()


    def setup_label(self):
        lbl = Label(self.window, text= 'Pyppeter Estacio',font=("Arial", 30))
        lbl.place(relx=0.5,rely=0.4,anchor=CENTER)

    def setup_buttons(self):
        csv_project_btn = Button(self.window,text='Mega Csv',bg='black',fg='white',command=lambda: main_screen.navigate_command(self.window,"Mega Csv"))
        csv_project_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

        kabum_scrapping = Button(self.window,text='Kabum Scrap',bg='black',fg='white',command=lambda: main_screen.navigate_command(self.window,"Kabum Scrap"))
        kabum_scrapping.place(relx=0.5, rely=0.6, anchor=CENTER)

    @staticmethod
    def navigate_command(window,button_clicked):
        if button_clicked == "Mega Csv":
            mega_csv_screen = mega_csv()
            window.destroy()
            mega_csv_screen.create_login_screen()
        elif button_clicked == "Kabum Scrap":
            kabum = kabum_scrapping_screen()
            window.destroy()
            kabum.show_screen()
        elif button_clicked == "Voltar":
             main = main_screen()
             window.destroy()
             main.show_screen()
            
#exemplo de chamada
#main = main_screen()
#main.show_screen()
