class car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"{self.brand},{self.model},{self.year}")
mycar = car("Audi","Q7",2006)
mycar.display_info()
