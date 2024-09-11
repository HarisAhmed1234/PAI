class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = []
        self.customer_orders = {}
    
    def add_item_to_menu(self, item_name, price):
        """Add an item to the menu."""
        self.menu_items[item_name] = price
    
    def book_table(self, table_number, customer_name):
        """Book a table for a customer."""
        reservation = {'table_number': table_number, 'customer_name': customer_name}
        self.booked_tables.append(reservation)
    
    def customer_order(self, customer_name, item_name, quantity):
        """Place an order for a customer."""
        if customer_name not in self.customer_orders:
            self.customer_orders[customer_name] = []
        self.customer_orders[customer_name].append({'item_name': item_name, 'quantity': quantity})
    
    def print_menu(self):
        """Print the menu items."""
        print("Menu:")
        for item_name, price in self.menu_items.items():
            print(f"{item_name}: ${price:.2f}")
    
    def print_booked_tables(self):
        """Print the table reservations."""
        print("Table Reservations:")
        for reservation in self.booked_tables:
            print(f"Table {reservation['table_number']} reserved for {reservation['customer_name']}")
    
    def print_customer_orders(self):
        """Print the customer orders."""
        print("Customer Orders:")
        for customer_name, orders in self.customer_orders.items():
            print(f"Orders for {customer_name}:")
            for order in orders:
                print(f"  {order['item_name']} x {order['quantity']}")

if __name__ == "__main__":
    restaurant = Restaurant()
    
    restaurant.add_item_to_menu("Burger", 5.99)
    restaurant.add_item_to_menu("Pizza", 8.99)
    restaurant.add_item_to_menu("Salad", 4.99)
    
    restaurant.book_table(1, "Haris")
    restaurant.book_table(2, "Sabeeh")
    
    restaurant.customer_order("Haris", "Burger", 2)
    restaurant.customer_order("Sabeeh", "Pizza", 1)
    restaurant.customer_order("Haris", "Salad", 1)

    restaurant.print_menu()

    restaurant.print_booked_tables()

    restaurant.print_customer_orders()
