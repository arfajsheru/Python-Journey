# ----------- Product Class -----------
class Product:
    """
    Product class -> Represent karta hai ek item jo user kharid sakta hai.
    Attributes:
        name (str): Product ka naam.
        price (float): Product ka price.
        stock (int): Product ka available stock.
    """
    def __init__(self, name, price, stock ):
        # Constructor: Product ki properties set karta hai jab naye product create hote hain.
        self.name = name  # Product ka naam store hota hai yaha.
        self.price = price  # Product ka price store hota hai.
        self.stock = stock  # Available stock ko track karta hai.

    def restock(self, quantity):
        # Method: Jab stock kam ho jaye to naye stock ko add karne ke liye.
        self.stock += quantity  # Stock ko badhata hai.
        print(f"{self.name} ka stock restock ho gaya! New stock: {self.stock}")


# ----------- ShoppingCart Class -----------
class ShoppingCart:
    """
    ShoppingCart class -> User ke cart ko manage karta hai.
    Attributes:
        products (dict): Cart me jo items hain unka record rakhta hai.
    """
    def __init__(self):
        # Constructor: Initialize karta hai khali cart.
        self.products = {}  # Dictionary: Key = Product, Value = Quantity.

    def add_product(self, product, quantity):
        # Method: Cart me product add karta hai aur stock validate karta hai.
        if product.stock < quantity:  # Check karta hai ki stock available hai ya nahi.
            print(f"Sorry bro, {product.name} ka stock itna nahi hai!")
            return


        

        if product in self.products:
            # Agar product pehle se cart me hai to quantity badha deta hai.
            self.products[product] += quantity
        else:
            # Naya product cart me add karta hai.
            self.products[product] = quantity

        product.stock -= quantity  # Stock kam kar deta hai cart me add hone ke baad.
        print(f"{product.name} add ho gaya! Quantity: {quantity}")

    def checkout(self, discount_code=None):
        # Method: Cart ka checkout karta hai aur total cost calculate karta hai.
        if not self.products:
            # Agar cart khali hai to warning dega.
            print("Cart empty hai bro, pehle kuch daal to sahi!")
            return None

        total_cost = sum(product.price * qty for product, qty in self.products.items())  # Total cost calculate karta hai.

        # Discount code ka logic handle karta hai.
        if discount_code == "DISCOUNT10":
            total_cost *= 0.9  # 10% discount lagata hai.
            print("Bhai discount lag gaya 10%! 😎")

        order = Order(self.products.copy(), total_cost)  # Naya order create kar raha hai.
        print(f"Order place ho gaya! Total: ₹{total_cost:.2f}")
        self.products.clear()  # Cart ko empty kar deta hai after order.
        return order


# ----------- Order Class -----------
class Order:
    """
    Order class -> Order ke details ko manage karta hai.
    Attributes:
        products (dict): Jo products order hue hain.
        total_cost (float): Order ka total price.
        delivery_status (str): Order ka delivery status (Pending, Shipped, etc.).
    """
    def __init__(self, products, total_cost):
        # Constructor: Order ki details initialize karta hai.
        self.products = products  # Jo products aur quantity order me hain.
        self.total_cost = total_cost  # Order ka total cost store karta hai.
        self.delivery_status = "Pending"  # Pehle "Pending" set hota hai.

    def update_status(self, status):
        # Method: Order ka delivery status update karta hai.
        self.delivery_status = status  # Delivery status ko change kar raha hai.
        print(f"Order status updated to: {status}")


# ----------- User Class -----------
class User:
    """
    User class -> E-commerce user ko represent karta hai.
    Attributes:
        name (str): User ka naam.
        cart (ShoppingCart): User ka shopping cart.
    """
    def __init__(self, name):
        # Constructor: User ke details initialize karta hai.
        self.name = name  # User ka naam store karta hai.
        self.cart = ShoppingCart()  # Har user ka ek shopping cart hota hai.

    def add_to_cart(self, product, quantity):
        # Method: User apne cart me product add kar sakta hai.
        if quantity <= 0:
            print("Are bhai quantity 0 nahi chalegi")
            return 
        self.cart.add_product(product, quantity)

    def place_order(self, discount_code=None):
        # Method: User cart ka order place karta hai.
        return self.cart.checkout(discount_code)


# ----------- Example Usage -----------
# Products create karte hain.
iphone = Product("iPhone", 80000, 5)  # Ek iPhone ka product with stock and price.
laptop = Product("Laptop", 60000, 2)  # Laptop product with stock and price.
headphones = Product("Headphones", 2000, 10)  # Headphones product with stock and price.


# User create karte hain.
user = User("Rahul")  # Naya user banaya.

# User apne cart me items daal raha hai.
user.add_to_cart(headphones, 0)
user.add_to_cart(iphone, 5)  # 1 iPhone add kar raha hai.
user.add_to_cart(laptop, 1)  # 1 Laptop add kar raha hai.

# User order place kar raha hai with discount code.
order = user.place_order(discount_code="DISCOUNT10")

# Agar order place hua to uska delivery status update karte hain.
if order:
    order.update_status("Shipped")  # Order status "Shipped" kar diya.

# Agar stock kam ho gaya, to restock karte hain.
iphone.restock(10)  # iPhone ka stock badha diya.
laptop.restock(5)  # Laptop ka stock bhi badha diya.
