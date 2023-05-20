from tkinter import Tk
from kabum_scrap_screen import kabum_scrapping_screen


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
        csv_project_btn = Button(self.window,text='Mega Csv',bg='black',fg='white',command=lambda: self.navigate_command("Mega Csv"))
        csv_project_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

        kabum_scrapping = Button(self.window,text='Kabum Scrap',bg='black',fg='white',command=lambda: self.navigate_command("Kabum Scrap"))
        kabum_scrapping.place(relx=0.5, rely=0.6, anchor=CENTER)


    def navigate_command(self,button_clicked):
        if button_clicked == "Mega Csv":
            #chama a login screen
            self.window.destroy()
        elif button_clicked == "Kabum Scrap":
            kabum = kabum_scrapping_screen()
            self.window.destroy()
            kabum.show_screen()
            

    
   


#exemplo de chamada
#main = main_screen()
#main.show_screen()






