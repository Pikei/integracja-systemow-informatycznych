class Home:
    def __init__(self, header_name, address, price, price_for_m2, m2):
        self.header_name = header_name
        self.address = address
        self.price = price
        self.price_for_m2 = price_for_m2
        self.m2 = m2

    def print_values(self):
        print(f"{self.header_name} | {self.address} | {self.price} | {self.price_for_m2} | {self.m2}")
