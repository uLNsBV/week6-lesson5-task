class Car:

    def input(self):
        self.name = input("1. Enter vehicle brand: ")
        self.color = input("2. Vehicle color: ")
        self.price = float(input('3. Enter vehicle price: '))
        self.COMPANY = input('4. Company name: ')

    def print(self):
        print(f"The vehicle brand is {self.name},\
      the color is {self.color},\
      given price is {self.price},\
      the Company is {self.COMPANY}")

    def change(self):
        price_with_percent = self.price * 0.1
        print(f'New price: {self.price + price_with_percent}')


tesla = Car()
tesla.input()
tesla.print()
tesla.change()