import py7zr
import modin.pandas as pd
import os
import math
import ray
from openpyxl import Workbook

class save_data:

    def __init__(self, seven_zip_file_path, seven_csv, directory,desktop_path):
        self.seven_csv = seven_csv
        self.seven_zip_file_path = seven_zip_file_path
        self.directory = directory
        self.desktop_path = desktop_path
        ray.init()

    def execute(self):
        df = pd.read_csv(self._unzip())
        df.fillna(0)
        self._toXlsx(df)

    def _search_file(self, directory, filename):
        for root, dirs, files in os.walk(directory):
            if filename in files:
                return os.path.join(root, filename)
        return None

    def _unzip(self):
        if(self._search_file(self.directory,self.seven_csv) != None):
            print('ja lido ')
            return self.seven_csv

        with py7zr.SevenZipFile(self.seven_zip_file_path, mode='r') as z:
            csv_file_name = z.getnames()[0]  
            z.extract(targets=csv_file_name)
        print('arquivo descompactado')    
        return csv_file_name

    def _toXlsx(self, df):
        max_rows = 350000
        total_files = math.ceil(len(df) / max_rows)

        for i in range(total_files):
            start_row = i * max_rows
            end_row = (i + 1) * max_rows

            df_temp = df.iloc[start_row:end_row]

            excel_path = os.path.join(self.desktop_path, f'arquivo_{i+1}.xlsx')

            df_temp.to_excel(excel_path, index=False)  # Exporta o DataFrame diretamente para o arquivo Excel

            print(f'Arquivo {i+1} salvo em {excel_path}')
            
    def productToXlsx(products_list,path):
        workbook = Workbook()
        sheet = workbook.active
        
        headers = ['Nome','Status','Preço Normal','Preço com desconto a vista','Preço com desconto','Duração da oferta','Url']
        sheet.append(headers)
        
        for product in products_list:
            data = [
                product.get('nome', None),
                product.get('status', None),
                product.get('preco_normal', None),
                product.get('preco_desconto', None),
                product.get('preco_desconto_normal', None),
                product.get('url', None)
            ]
            sheet.append(data)
        
        save_spot = os.path.join(path, 'produtos.xlsx') 
        workbook.save(save_spot)
        