class XPdf:
	def __init__(self):
		self.files_per_month_per_year = {23:[0]*12, 24:[0]*12, 25:[0]*12}
		self.revenue_per_month_current_year = [0] * 12
		self.revenue_per_month_last_year = [0] * 12
		self.files_per_date = {}
		self.last_name = ""
		self.total_files = 0
		self.total_revenue = 0
		self.net_revenue = 0
		self.bill_date = ""