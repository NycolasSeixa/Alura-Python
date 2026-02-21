class Restaurant:
    r_list = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
        Restaurant.r_list.append(self)

    def __str__(self):
        return f'{self.name} | {self.category}'
    
    def show_all():
        for r in Restaurant.r_list:
            print(f'{r.name} | {r.category}')

plaza_restaurant = Restaurant('Plaza', 'Pizzeria ')
biggy_restaurant = Restaurant('Biggy', 'Fast Food ')

Restaurant.show_all()