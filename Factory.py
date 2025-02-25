class Pizza:
    def prepare(self):
        pass

class VegPizza(Pizza):
    def prepare(self):
        return "Preparing Veg Pizza 🍀"

class ChickenPizza(Pizza):
    def prepare(self):
        return "Preparing Chicken Pizza 🍗"

class PizzaFactory:
    @staticmethod
    def get_pizza(pizza_type):
        if pizza_type == "veg":
            return VegPizza()
        elif pizza_type == "chicken":
            return ChickenPizza()
        else:
            raise ValueError("Invalid Pizza Type!")

# Usage
pizza = PizzaFactory.get_pizza("chicken")
print(pizza.prepare())  

# Output: Preparing Chicken Pizza 🍗