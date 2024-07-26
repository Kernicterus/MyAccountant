import pdfplumber
import pandas as pd
from openpyxl import load_workbook
import sys

from XPdf import XPdf
from parsing import parsing_lines

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

def pdf_extraction(inputpdf):
	pdf_path = inputpdf
	text = ""
	with pdfplumber.open(pdf_path) as pdf:
		for page in pdf.pages:
			text += page.extract_text() + "\n"
		lines = text.split('\n')
	return lines

def parsing_to_excel(outputxlsx,my_pdf):
	excel_path = outputxlsx
    
def MyAccountant():
	if len(sys.argv) != 3:
		print("Usage: python MyAccountant.py <input.pdf> <output.xlsx>")
		sys.exit(1)
	inputpdf = sys.argv[1]
	outputxlsx = sys.argv[2]
	my_pdf = XPdf()
	lines = pdf_extraction(inputpdf)
	parsing_lines(lines, my_pdf)
	parsing_to_excel(outputxlsx,my_pdf)

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