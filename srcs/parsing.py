from datetime import datetime
from XPdf import XPdf
import re

def count_revenue(line, date, my_pdf, line_elements):
	current_year = datetime.now().year
	current_year = current_year % 100
	line_revenue = line_elements[-2]
	my_pdf.total_revenue += float(line_revenue)
	if (int(date[4:6]) == current_year):
		my_pdf.revenue_per_month_current_year[int(date[2:4]) - 1] += float(line_revenue)
	elif (int(date[4:6]) == current_year - 1):
		my_pdf.revenue_per_month_last_year[int(date[2:4]) - 1] += float(line_revenue)

def count_files_per_date(date, my_pdf, file_name) :
	if file_name != my_pdf.last_name:
		if (date) in my_pdf.files_per_date:
			my_pdf.files_per_date[date] += 1
		else:
			my_pdf.files_per_date[date] = 1
		my_pdf.last_name = file_name

def extract_payment(line, my_pdf):
	line_elements = line.split()
	if (len(line_elements) >= 6 and line_elements[1] == "NET"):
		if line_elements[1]+line_elements[2]+line_elements[3] == "NETAPAYER":
			print(line_elements[5])
			my_pdf.net_revenue = float(line_elements[5])

def extract_data(line, my_pdf):
	day_str = line[0:2]
	month_str = line[3:5]
	year_str = line[6:8]
	date = day_str+month_str+year_str
	line_elements = line.split()
	file_name = line_elements[1]+line_elements[2]

	count_files_per_date(date, my_pdf, file_name)
	count_revenue(line, date, my_pdf, line_elements)

	my_pdf.last_name = file_name

def count_files_per_month(mypdf):
	current_year = datetime.now().year
	current_year = current_year % 100

	for key, value in mypdf.files_per_date.items():
		for month in range(1,13) :
			month_str= str(month)
			if (month < 10):
				month_str ="0"+month_str
			if key.endswith(f"{month_str}{current_year}"):
				mypdf.file_per_month_current_year[month -1] += mypdf.files_per_date[key]
			elif key.endswith(f"{month_str}{current_year - 1}"):
				mypdf.file_per_month_last_year[month -1] += mypdf.files_per_date[key]

def parsing_lines(lines, my_pdf):
	pattern = re.compile(r"\d{2}/\d{2}/\d{2}\|?\d{9}", re.IGNORECASE)
	for line in lines:
		match = re.match(pattern, line)
		if match:
			extract_data(line, my_pdf)
		extract_payment(line, my_pdf)
	my_pdf.total_files = sum(my_pdf.files_per_date.values())
	count_files_per_month(my_pdf)
	total_per_month= sum(my_pdf.revenue_per_month_current_year)+sum(my_pdf.revenue_per_month_last_year)

	print(f"total files : {my_pdf.total_files}")
	print(f"total revenue : {my_pdf.total_revenue}")
	print(f"total revenue per month : {total_per_month}")
	print(f"NET revenue : {my_pdf.net_revenue}")
	print(my_pdf.file_per_month_current_year)