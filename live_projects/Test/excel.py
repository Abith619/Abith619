import pandas as pd
import openpyxl as xl
from googletrans import Translator
from translate import Translator
from mtranslate import translate
import csv

def translate_csv(input_file, output_file, target_language):
    translated_rows = []
    
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        
        for row in reader:
            translated_row = []
            for cell in row:
                translation = translate(cell, target_language)
                translated_row.append(translation)
            translated_rows.append(translated_row)
    
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(translated_rows)


target_language = 'en'  

input_file = 'C:\\Users\\DELL\\Downloads\\category_listings_categories.csv'
output_file = 'C:\\Users\\DELL\\Downloads\\category_listings_categories.csv'

translate_csv(input_file, output_file, target_language)
