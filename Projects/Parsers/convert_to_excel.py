"""
Convert a log (*.txt) file into pre-formatted excel output
Columns:JOB ID,LOAD STEP,STATUS,START TS,END TS,RUN TIME,LOCK TIME,TOTAL TIME,REFRESHED,INSERTED,UPDATED,DELETED,
        TOTAL I+U+D,TOTAL RECORDS,I+U+D/SEC,TOTAL/SEC,LOADED/SEC,
"""

import sys
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
 

def main(argv):
    try:
        # GUI select file dialog
        root = tk.Tk()
        root.withdraw()

        # Promot for the file
        input_file_name = filedialog.askopenfilename(initialdir = ".") 
        
        # Pandas Excel writer using XlsxWriter as the engine
        writer = pd.ExcelWriter(input_file_name[:-4] + ".xlsx", engine='xlsxwriter')

        # Get data and create the Excel file
        df = pd.read_csv(input_file_name) 
        df.to_excel(writer, index = False) 

        # Format worksheet
        workbook  = writer.book
        worksheet = writer.sheets['Sheet1']
        worksheet.freeze_panes(1, 1)
        
        num_format = workbook.add_format({'num_format': '#,###'})
        date_format = workbook.add_format({'num_format': 'D:HH:MM'})

        worksheet.set_column('I:Q', None, num_format)
        worksheet.set_column('F:H', None, date_format)

        # Auto fit columns 
        for idx, col in enumerate(df):  # loop through all columns
            series = df[col]
            max_len = max((
                series.astype(str).map(len).max(),  # len of largest item
                len(str(series.name))  # len of column name/header
                )) + 1  # adding a little extra space
            worksheet.set_column(idx, idx, max_len)  # set column width

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

        # Start Excel
        os.system('start excel.exe ' + input_file_name[:-4] + ".xlsx")

    except ValueError as exception:
        print(exception) 


if __name__ == "__main__":
    main(sys.argv)

