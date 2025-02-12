# # How to Solve Coding Problems:
"""
1. Break each problem down into as many little pieces as possible.
- Parameter, Return, Examples, Pseudocode
2. When it comes to turning pseudocode into actual code
- Constantly test code line by line, even if it might seem trivial.
3. Twenty Minute Rule: After being stuck and exhausting all resources... 
   - then seek solution or personal help
   - no shame, because if you're genuinely stuck for too long, you're not being productive anymore
   - but with personal help, make sure you can explain what you've done
4. Write solution(s) youself, add multiple comments to ensure you understand each line.
5. Come Back Later to re-do problem from scratch to see if you remember.
6. If you find you get still stuck, just repeat this process at the step you got stuck on.
***There are no shortcuts or quick fixes. As much hands on as you can get is the only way to progress***
***Limit content consuming as it can turn into a never-ending time-wasting trap.***
"""
# # Create a class named CarManager
class CarManager:
    # # CLASS ATTRIBUTES
    all_cars = {} # data structure storing all the car instances created.
    total_cars = 0  # int representing total number of cars.

    # # INSTANCE ATTRIBUTES
    def __init__(self, id, make, model, year):
        self._id = id # int that won't repeat and increment by 1 with each new car instance
        self._make = make # str 
        self._model = model # str
        self._year = year # int
        self._mileage = 0 # int
        self._services = [] # list

        CarManager.all_cars[self._id] = self # add new car_obj to all_cars with new car instance
        CarManager.total_cars += 1 # increment total_cars with new car_instance

    # return string representation of object
    def __repr__(self):
        return f"""Make: {self.get_make} Model: {self.get_model} Year: {self.get_year} | Mileage: {self.get_mileage} Services: {", ".join(self.get_services)}"""       

    # GETTER METHODS and corresponding SETTER METHODS for instance attribute
    @property
    def get_id(self):
        return self._id # no corresponding setter as id can't be reset
        
    @property
    def get_make(self):
        return self._make
        
    @get_make.setter
    def set_make(self, make):
        self._make = make

    @property
    def get_model(self):
        return self._model

    @get_model.setter
    def set_model(self, model):
        self._model = model

    @property
    def get_year(self):
        return self._year

    @get_year.setter
    def set_year(self, year):
        self._year = year

    @property
    def get_mileage(self):
        return self._mileage

    @get_mileage.setter
    def set_mileage(self, mileage):
        self._mileage = mileage

    @property
    def get_services(self):
        return self._services

    @get_services.setter
    def set_services(self, service):
        self._services.append(service)

    #DEFINE TERMINAL APPLICATION METHODS
    def add_car():
        # get input from user for required instance attributes
        id = CarManager.total_cars + 1 # id corresponds to total_cars class attribute
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        year = int(input("Enter manufacturing year: "))
        # create new car instance
        CarManager(id, make, model, year)
        # print statements
        print("Car added successfully!")
        print(CarManager.all_cars)

    def print_cars():
        print("All Cars:")
        # iterate through class attribute all_cars dict
        for car in CarManager.all_cars.values():
            print(f"{car.get_year} {car.get_make} {car.get_model}")

    def view_total_cars():
        # print class attribute total_cars int
        print(f"Total number of cars: {CarManager.total_cars}")

    def see_car_details():
        # get id input from user to see car details (key/pair value)
        id = int(input("Enter Car ID to see car details: "))
        print(CarManager.all_cars.get(id))

    def service_car():
        # get id input from user for accessing that car's services
        id = int(input("Enter Car ID for adding service: "))
        car = CarManager.all_cars.get(id)
        # get service input from user to add service
        service = input("Enter service description: ")
        car.set_services = service

    def update_mileage():
        # get id input from user for update mileage
        id = int(input("Enter Car ID for updating mileage: "))
        car = CarManager.all_cars.get(id)
        # get service input from user to add service
        mileage = int(input("Enter new mileage: "))
        if mileage < 0:
            print("Wrong Input")
        else:
            car.set_mileage = mileage

    # Print Terminal Menu
    def options():
        print("\n1: Add a car")
        print("2: View all cars")
        print("3: View total number of cars")
        print("4: See a Car's Details")
        print("5: Service a car")
        print("6: Update mileage")
        print("7: Quit\n")

    # run terminal application
    def run_terminal():
        # local variables
        boolean = True
        choice_list = [1,2,3,4,5,6,7]

        # continually prompt user with options menu until they quit
        while boolean == True:
            CarManager.options()
            try:
                option = int(input())
                flag = any(x == option for x in choice_list)
                # only accounts for covering user entering invalid number
                if not flag:
                    print("Invalid Number! Try Again!\n")
                if option == 1:
                    CarManager.add_car()
                elif option == 2:
                    CarManager.print_cars()
                elif option == 3:
                    CarManager.view_total_cars()
                elif option == 4:
                    CarManager.see_car_details()
                elif option == 5:
                    CarManager.service_car()
                elif option == 6:
                    CarManager.update_mileage()
                elif option == 7:
                   print("Goodbye!")
                   # changing local variable to False exits while loop and program
                   boolean = False
            # accounts for all other user input errors.
            except ValueError: 
                print("Invalid Choice! Try Again!\n")
                
    
CarManager.run_terminal()