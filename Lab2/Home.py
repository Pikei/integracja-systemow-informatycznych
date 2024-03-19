class Home:
    def __init__(self, header_name, address, price, price_for_m2, m2):
        self.header_name = header_name
        self.address = address
        self.price = price
        self.price_for_m2 = price_for_m2
        self.m2 = m2

    def print_values(self):
        print(f"====================================================================\n"
              f"Name: {self.header_name}\n"
              f"Address: {self.address}\n"
              f"Price: {self.price}\n"
              f"Price for square meter: {self.price_for_m2}\n"
              f"Apartment area: {self.m2}\n"
              f"====================================================================\n")


