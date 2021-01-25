class Calendar():
	def __init__(self, start_day_in_week, start_day, start_month, start_year):
		self.days = ["Monday", "Tuesday", "Wedensday", "Thursday", "Friday", "Saturday", "Sunday"]
		self.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		self.num_days_in_month = dict(zip(self.months, month_days))
		self.current_day = start_day_in_week
		self.day_in_month = start_day
		self.month = start_month
		self.year = start_year
		self.is_leap_year()
		self.sol = 0
		self.sol2 = 0
		
	def is_leap_year(self):
		if ((self.year % 4 == 0) and (self.year % 100 != 0)) or self.year % 400 == 0:
			self.num_days_in_month["Feb"] = 29
			return True
		else:
			self.num_days_in_month["Feb"] = 28
			return False
			
	def next_year(self):
		self.year += 1
		self.is_leap_year()
		
	def next_month(self):
		# REMOVE THIS IF YOU AREN'T SOLVING THE PROBLEM
		if self.current_day == "Sunday":
			self.sol += 1
		##################################################
		self.month = self.months[(self.months.index(self.month) + 1) % len(self.months)]
		if self.month == self.months[0]:
			self.next_year()
		
	
	def next_day(self):
		self.current_day = self.days[(self.days.index(self.current_day) + 1) % len(self.days)]			
		if self.day_in_month < 28:
			self.day_in_month += 1
			return
		else:
			if self.day_in_month == self.num_days_in_month[self.month]:
				self.next_month()
				self.day_in_month = 1
			else:
				self.day_in_month += 1
			

m_cal = Calendar("Tuesday", 1, "Jan", 1901)


while m_cal.year!=2001:
	m_cal.next_day()
	
print m_cal.sol
