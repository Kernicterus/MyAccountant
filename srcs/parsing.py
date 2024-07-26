from datetime import datetime
from XPdf import XPdf
import re

def extract_data(line, my_pdf):
			day_str = line[0:2]
			month_str = line[3:5]
			year_str = line[6:8]
			date = day_str+month_str+year_str
			file_id = line[8:17]
			if file_id != my_pdf.last_id:
				if (date) in my_pdf.file_per_date:
					my_pdf.file_per_date[date] += 1
				elif (file_id != my_pdf.last_id):
					my_pdf.file_per_date[date] = 1
			my_pdf.last_id = file_id	

def parsing_lines(lines, my_pdf):
	current_year = datetime.now().year
	current_year = current_year % 100
	print (current_year)
	pattern = re.compile(r"\d{2}/\d{2}/\d{2}\|?\d{9}", re.IGNORECASE)
	for line in lines:
		match = re.match(pattern, line)
		if match:
			extract_data(line, my_pdf)
	print (my_pdf.file_per_date)
