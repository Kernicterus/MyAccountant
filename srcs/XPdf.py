class XPdf:
	def __init__(self):
		self.file_per_month_current_year = [0] * 12
		self.file_per_month_last_year = [0] * 12
		self.revenue_per_month_current_year = [0] * 12
		self.revenue_per_month_last_year = [0] * 12
		self.file_per_date = {}
		self.last_id = ""
		self.total_files = 0