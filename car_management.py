# Practiced Instantiating Classes and Instances

# Still Need to Implement Terminal Interface and Instance Methods
# for allowing user to input data through Terminal
# But ran out of time
class CarManager:
    # class attributes
    id = 0
    all_cars = {}
    total_cars = 0
    
    # instance attributes
    def __init__(self, make, model, year, mileage, services):
        self.id = CarManager.id + 1
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.services = services

    def __repr__(self):
        return f"Car Make: {self.make}, Car Model {self.model}, Car Year: {self.year}, Car Mileage {self.mileage}, Car Services {self.services}"
    

# Adding Two Vehicle Instances
car = {'make': 'toyota', 'model': 'corolla', 'year': 2010, "mileage": 200, "services": ['wash']}
truck = {'make': 'honda', 'model': 'cr-v', 'year': 2019, "mileage": 100, "services": ['oil change', 'tire rotation']}
car_class = CarManager(**car)
CarManager.id += 1
CarManager.all_cars[CarManager.id] = car_class
CarManager.total_cars += 1
truck_class = CarManager(**truck)
CarManager.id += 1
CarManager.all_cars[CarManager.id] = truck_class
CarManager.total_cars += 1

# Viewing All Cars:
print(CarManager.all_cars)

# Viewing Total Number of Cars
print(CarManager.total_cars)

# Viewing a Car's Details by ID:
print(CarManager.all_cars[1]) # View Corolla
print(CarManager.all_cars[2]) # View Truck

# Adding Servicing to Car
CarManager.all_cars[1].services.append("break")
print(CarManager.all_cars[1]) # Verify Service got Added

# Updating Mileage of Truck
CarManager.all_cars[2].mileage += 50
print(CarManager.all_cars[2]) # View Mileage got Updated