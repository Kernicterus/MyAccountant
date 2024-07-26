class XPdf:
	def __init__(self):
		self.file_per_month_current_year = [0] * 12
		self.file_per_month_last_year = [0] * 12
		self.revenue_per_month_current_year = [0] * 12
		self.revenue_per_month_last_year = [0] * 12
		self.files_per_date = {}
		self.last_name = ""
		self.total_files = 0
		self.total_revenue = 0
		self.payment_date = 0
		self.net_revenue = 0