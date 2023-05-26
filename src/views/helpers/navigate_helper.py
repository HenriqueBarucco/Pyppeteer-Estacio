

class navigate_helper:
        

        def _navigate_back_to_main(window):
                from src.views.main_screen import main_screen as main
                main.navigate_command(window=window,button_clicked='Voltar')
                
                