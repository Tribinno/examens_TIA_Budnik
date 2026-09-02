class Vehicle:
	def __init__(self, brand, year):
		self.brand = brand
		self.year = year

	def display_info(self):
		print(f"Brand: {self.brand}, Year: {self.year}")


vehicle_one = Vehicle("Toyota", 2020)
vehicle_two = Vehicle("Ford", 2023)

vehicle_one.display_info()
vehicle_two.display_info()
