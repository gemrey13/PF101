class MenuItem:
    def __init__(self, item_name: str, price: float, description: str) -> None:
        self.__item_name = item_name
        self.__price = price
        self.__description = description

    def display_details(self):
        print(f'Item Name:\t{self.get_item_name().title()}\nPrice:\t\t{self.get_price()}\nDescription:\t{self.get_description().title()}')

    def get_item_name(self):
        return self.__item_name

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    def update_item(self, item_name: str=None, price: float=None, description: str=None):
        if item_name is not None:
            self.__item_name = item_name
            msg += f'\nItem name changed to {item_name}'

        if price is not None:
            self.__price = price
            msg += f'\nPrice Updated to {price}'

        if description is not None:
            self.__description = description
            msg += f'\nDescription changed to {description}'
        msg = ''
        print(msg)

class Order:
    def __init__(self) -> None:
        self.orders = []

    def add_item(self, order_item: object):
        if order_item.get_status():
            self.orders.append(order_item)
            print(f'The {order_item.get_item_name().title()} in the order list.')
        else:
            print(f'You need to cook {order_item.get_item_name().title()} to add it in the order.')

    def calculate_total(self):
        total = 0
        for order in self.orders:
           total += order.get_price()
        print(f'Total Amount:\t${total}')

class FoodItem(MenuItem):
    def __init__(self, item_name: str, price: float, description: str, cook: bool = False) -> None:
        super().__init__(item_name, price, description)
        self.cook = cook

    def cook_food(self):
        self.cook = True
        print(f'The {self.get_item_name().title()} has been cooked!')

    def get_status(self):
        return self.cook

class DrinkItem(MenuItem):
    def __init__(self, item_name: str, price: float, description: str, poured: bool = False) -> None:
        super().__init__(item_name, price, description)
        self.poured = poured

    def pour(self):
        self.poured = True
        print(f'The {self.get_item_name().title()} has been Poured!')

    def get_status(self):
        return self.poured

class PremiumFoodItem(FoodItem):
    def __init__(self) -> None:
        super().__init__()

order1 = Order()
pizza = FoodItem('pizza', 20.0, 'A Rounded Food and yummy')
order1.add_item(pizza)

pizza.cook_food()
pizza.display_details()
redhorse = DrinkItem('redhorse', 20.0, 'A beer')
redhorse.pour()

order1.add_item(pizza)
order1.add_item(redhorse)
order1.calculate_total()
