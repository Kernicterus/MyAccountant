import pdfplumber
import pandas as pd
import re
from openpyxl import load_workbook
from datetime import datetime

#extracted data from pdf to object
class XPdf:
	def __init__(self):
		self.file_per_month_current_year = [0] * 12
		self.file_per_month_last_year = [0] * 12
		self.revenue_per_month_current_year = [0] * 12
		self.revenue_per_month_last_year = [0] * 12

# # Écrire les données dans une première feuille Excel
# with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
#     for i, table_df in enumerate(tables):
#         table_df.to_excel(writer, sheet_name=f'Tableau_{i+1}', index=False)

# # Charger le fichier Excel pour ajouter des formules
# workbook = load_workbook(excel_path)
# sheet = workbook['Tableau_1']

# # Exemple : écrire une somme de la colonne A dans la cellule B1
# sheet['B1'] = 'Total'
# sheet['B2'] = '=SUM(A2:A10)'

# # Sauvegarder les modifications
# workbook.save(excel_path)

# # Écrire des données dans une deuxième feuille
# with pd.ExcelWriter(excel_path, engine='openpyxl', mode='a') as writer:
#     additional_data = {
#         'Col1': [1, 2, 3],
#         'Col2': [4, 5, 6]
#     }
#     additional_df = pd.DataFrame(additional_data)
#     additional_df.to_excel(writer, sheet_name='Additional_Data', index=False)

def pdf_extraction():
	pdf_path = 'f42kx9wn14032024_LEDE00.pdf'
	text = ""
	with pdfplumber.open(pdf_path) as pdf:
		for page in pdf.pages:
			text += page.extract_text() + "\n"
		lines = text.split('\n')
	return lines

def parsing_lines(lines, my_pdf):
	current_year = datetime.now().year
	current_year = current_year % 100
	print (current_year)
	pattern = re.compile(r"\d{2}/\d{2}/\d{11}", re.IGNORECASE)
	for line in lines:
		match = re.match(pattern, line)
		if match:
			year_str = line[6:8]
			if current_year == int(year_str):
				print(line)

def parsing_to_excel(my_pdf):
	excel_path = 'output.xlsx'
    
def MyAccountant():
	my_pdf = XPdf()
	lines = pdf_extraction()
	parsing_lines(lines, my_pdf)
	parsing_to_excel(my_pdf)

if __name__ == "__main__":
    MyAccountant()		
	
	
	# im = pdf.pages[0].to_image(resolution=150)
		# im.show()
		# for page_num, page in enumerate(pdf.pages):
		# 	extracted_tables = page.extract_tables()
		# 	for table in extracted_tables:
		# 		df = pd.DataFrame(table[1:], columns=table[0])
		# 		tables.append(df)
		# 		print(f"Tableau extrait de la page {page_num + 1} :")
		# 		print(df)
		# 		print()