class MenuItem:
    def __init__(self, item_name: str, price: float, description: str) -> None:
        self.item_name = item_name
        self.price = price
        self.description = description

    def display_details(self):
        print(f'Item Name:\t{self.item_name}\nPrice:\t{self.price}\nDescription:\t{self.description}')

    def get_item_name(self):
        return self.item_name

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description

    def update_item(self, item_name, price, description):
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
        self.orders.append(order_item)

    def calculate_total(self):
        pass

class FoodItem:
    def __init__(self) -> None:
        pass

    def cook(self):
        pass

class DrinkItem:
    def __init__(self) -> None:
        pass

    def pour(self):
        pass

class PremiumFoodItem(FoodItem):
    def __init__(self) -> None:
        super().__init__()