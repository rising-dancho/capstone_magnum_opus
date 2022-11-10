
class Pizza:
    name = ""
    ingredients = ""
    price = 0.0
    vegetarian = False

    def __init__(self, name, ingredients, price, vegetarian):
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.vegetarian = vegetarian

    def get_dictionary(self):
        return {"name": self.name, "ingredients": self.ingredients, "price": self.price, "vegetarian": self.vegetarian}



