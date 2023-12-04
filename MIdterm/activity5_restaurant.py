class MenuItem:
    def __init__(self, item_name: str, price: float, description: str) -> None:
        self.item_name = item_name
        self.price = price
        self.description = description

    def display_details(self):
        print(f'Item Name:\t{self.item_name.title()}\nPrice:\t\t{self.price}\nDescription:\t{self.description.title()}')

    def get_item_name(self):
        return self.item_name

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description

    def update_item(self, item_name: str=None, price: float=None, description: str=None):
        if item_name is not None:
            self.item_name = item_name
            msg += f'\nItem name changed to {item_name}'

        if price is not None:
            self.price = price
            msg += f'\nPrice Updated to {price}'

        if description is not None:
            self.description = description
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
            print(f'The {order_item.get_item_name().title()} is not Ready.')

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
        print(f'The {self.item_name.title()} has been cooked!')

    def get_status(self):
        return self.cook

class DrinkItem(MenuItem):
    def __init__(self, item_name: str, price: float, description: str, poured: bool = False) -> None:
        super().__init__(item_name, price, description)
        self.poured = poured

    def pour(self):
        self.poured = True
        print(f'The {self.item_name.title()} has been Poured!')

    def get_status(self):
        return self.poured

class PremiumFoodItem(FoodItem):
    def __init__(self) -> None:
        super().__init__()

pizza = FoodItem('pizza', 20.0, 'A Rounded Food and yummy')
burger = FoodItem('burger', 37.0, 'A bigmak')
nachos = FoodItem('nachos', 38.0, 'A chips')

burger.cook_food()
pizza.cook_food()
nachos.cook_food()

redhorse = DrinkItem('redhorse', 20.0, 'A beer')
redhorse.pour()

order1 = Order()
order1.add_item(pizza)
order1.add_item(burger)
order1.add_item(redhorse)
order1.add_item(nachos)
order1.calculate_total()

ha = input('')
sa = input('>')
ha = sa

print(ha)
