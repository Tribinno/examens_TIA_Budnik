from vehicle import Vehicle


class VehicleBrand(Vehicle):
	def display_brand_info(self):
		print(f"This vehicle is a {self.brand} from {self.year}.")


vehicle_one = VehicleBrand("Toyota", 2020)
vehicle_two = VehicleBrand("Ford", 2023)

vehicle_one.display_brand_info()
vehicle_two.display_brand_info()
