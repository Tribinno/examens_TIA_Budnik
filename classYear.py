from vehicle import Vehicle


class VehicleYear(Vehicle):
	def display_year_info(self):
		if self.year >= 2020:
			condition = "new"
		else:
			condition = "old"

		print(f"{self.brand} ({self.year}) is an {condition} vehicle.")


vehicle_one = VehicleYear("Honda", 2018)
vehicle_two = VehicleYear("Tesla", 2024)

vehicle_one.display_year_info()
vehicle_two.display_year_info()
