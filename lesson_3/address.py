class Address:
    post_index: str
    city: str
    street: str
    house: int
    flat: int
    def __init__(self, post_index, city, street, house, flat):
        self.post_index = post_index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat