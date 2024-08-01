import pdfplumber
import pandas as pd

from XPdf import XPdf
from parsing import parsing_lines
from to_excel import parsing_to_excel

def pdf_extraction(inputpdf):
	pdf_path = inputpdf
	text = ""
	with pdfplumber.open(pdf_path) as pdf:
		for page in pdf.pages:
			text += page.extract_text() + "\n"
		lines = text.split('\n')
	return lines

def MyAccountant(inputpdf, inputxlsx):
	my_pdf = XPdf()
	lines = pdf_extraction(inputpdf)
	parsing_lines(lines, my_pdf)
	return(parsing_to_excel(inputxlsx, my_pdf))

