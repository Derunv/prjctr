class Restaurant():
    def __init__(self, name: str, cuisine: str, menu: dict):
        self.name = name
        self.cuisine = cuisine.lower()
        self.menu = dict(menu)


class FastFood(Restaurant):
    def __init__(self, name: str, cuisine: str, menu: dict, drive_thru: bool):
        Restaurant.__init__(self, name, cuisine, menu)
        # super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru


    def order(self, dish_name: str, quantity: int) -> float:
        return self.menu.get(dish_name) * quantity


menu =  {'burger':  5,
    'pizza': 10,
    'drink': 1}

mc = FastFood('McDonalds', 'Fast Food', menu, True)
print(mc.order('burger', 5)) # 25
print(mc.order('burger', 15)) # Requested quantity not available
print(mc.order('soup', 5)) # Dish not available