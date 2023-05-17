import py7zr
import pandas as pd
import os
import openpyxl 
import math

class save_data:

    def __init__(self, seven_zip_file_path, seven_csv, directory):
        self.seven_csv = seven_csv
        self.seven_zip_file_path = seven_zip_file_path
        self.directory = directory
        self.desktop_path = os.path.expanduser("~\Desktop")

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
            
        return csv_file_name

    def _toXlsx(self, df):
        max_rows = 350000
        total_files = math.ceil(len(df) / max_rows)

        for i in range(total_files):
            start_row = i * max_rows
            end_row = (i + 1) * max_rows

            df_temp = df.iloc[start_row:end_row]

            excel_path = os.path.join(self.desktop_path, f'arquivo_{i+1}.xlsx')

            workbook = openpyxl.Workbook()
            sheet = workbook.active

            for r, row in enumerate(df_temp.values, start=1):
                for c, value in enumerate(row, start=1):
                    
                    sheet.cell(row=r, column=c).value = value
                    
            workbook.save(excel_path)
            print(f'Arquivo {i+1} salvo em {excel_path}')