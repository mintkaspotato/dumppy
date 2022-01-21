class Item:
    def calculate_total_price(self, x, y):
#cant be a pass since pass arg gives us ZERO args in the compile and python
        #has to have at least one in a method
        return x*y

item1 = Item()
    item1.name = "Phone"
    item1.price = 100
    item1.quantity = 5
    item1.calculate_total_price(item1.price, item1.quantity)

item2 = Item()
    item2.name = "Laptop"
    item2.price = 1000
    item2.quantity = 3
    item2.calculate_total_price()
