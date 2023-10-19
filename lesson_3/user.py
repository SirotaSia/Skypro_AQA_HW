class User:
    def __init__(self, first_name, last_name):
        self.user_fname = first_name
        self.user_lname = last_name

    def sayFirstName(self):
        print(f"User first name: {self.user_fname}")

    def sayLastName(self):
        print(f"User last name: {self.user_lname}")

    def sayFullName(self):
        print(f"User full name: {self.user_fname} {self.user_lname}")