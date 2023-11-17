from address import Address

class Mailing:
    to_address: Address
    from_address: Address
    cost: int
    track: str
    def __init__(self):
        self.to_address = Address("post_index1", "city1", "street1", 1, 11)
        self.from_address = Address("post_index2", "city2", "street2", 2, 22)
        self.cost = 0
        self.track = "track_1"