from tkinter import CENTER, Button, Entry, Label, Tk 
from tkinter import filedialog
from tkinter import messagebox
from src.kabum_spider import KabumSpider
from scrapy.crawler import CrawlerProcess
from src.views.helpers.navigate_helper import navigate_helper

class kabum_scrapping_screen:

    def __init__(self):
        self.window = Tk()
        self.product_txtfld = None
        self.dir_entry = None
        
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
        self.product_txtfld = Entry(self.window,bd=5)
        self.product_txtfld.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        
    def _dir_alert_dialog(self,directory):
        if  directory == None or not directory :
            messagebox.showerror("Erro","Selecione um Diretório válido...") 
            return False    
        else:
             messagebox.showinfo("Alerta", "O arquivo sera salvo em " + self.dir_entry )
             return True
    
    
    
        
    def _directory_selection(self):
        selected_dir = filedialog.askdirectory(initialdir="~")
        
        self.dir_entry = selected_dir
        
        
    def _handle_alert_dialog_return(self,return_value):
            if return_value == False:
                return None
            #print('INICIA O SCRAPY AQUI HENRIQUE '+self.product_txtfld.get() + " " + self._directory_selection)
            process = CrawlerProcess()
            process.crawl(KabumSpider, produto=self.product_txtfld.get(), path=self.dir_entry)
            process.start()

    

#definir o command do botao
    def setup_buton(self):
        #"o produto pega assim  "+self.product_txtfld.get() + "o diretorio assim " + self.dir_entry
        directory_btn = Button(self.window,text="Selecione o diretório", bg='black',fg='white',command=lambda: self._directory_selection())
        directory_btn.place(relx= 0.5,rely=0.6,anchor=CENTER)

        back_btn = Button(self.window,text="Voltar", bg='black',fg='white',command=lambda: navigate_helper._navigate_back_to_main(window=self.window) )
        back_btn.place(relx= 0.9,rely=0.9)
        
        go_btn = Button(self.window,text='Iniciar',bg='black',fg='white',command=lambda: self._handle_alert_dialog_return(self._dir_alert_dialog(self.dir_entry))  ) 
        go_btn.place(relx=0.5,rely=0.7,anchor=CENTER)
        
        