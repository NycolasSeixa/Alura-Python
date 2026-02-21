class Restaurant:
    r_list = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._active = False
        Restaurant.r_list.append(self)

    @property
    def active(self):
        return 'Active' if self._active else 'Inactive'

    def __str__(self):
        return f'{self.name} | {self.category}'
    
    def show_all():
        print(f'{'NAME'.ljust(5)} | {'CATEGORY'.ljust(5)}')
        for r in Restaurant.r_list:
            print(f'{r.name.ljust(5)} | {r.category.ljust(5)}')

plaza_restaurant = Restaurant('Plaza', 'Pizzeria ')
biggy_restaurant = Restaurant('Biggy', 'Fast Food ')

Restaurant.show_all()