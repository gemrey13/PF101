class Payment:
    def __init__(self, price) -> None:
        self.__final_price = price + (price * 0.05)

    def setDiscount(self, discount):
        self.__final_price = self.__final_price - self.__final_price * (discount / 100)

    def getFinalPrice(self):
        return self.__final_price

laptop = Payment(100)

laptop.setDiscount(50)
print(laptop.getFinalPrice())