from creator.restaurant import Restaurant

gomery_restaurant = Restaurant('Gomery', 'Gourmet')
meadow_restaurant = Restaurant('Meadow', 'Mexican')
meadow_restaurant.toggle_active()

def main():
    Restaurant.show_all()

if __name__ == '__main__':
    main()

