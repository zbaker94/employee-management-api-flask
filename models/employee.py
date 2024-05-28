
class Employee:
    def __init__(self, name, email, id):
        self.name = name
        self.email = email
        self.id = id

    @staticmethod
    def is_valid(employee):
        return "name" in employee and type(employee["name"]) == str and len(employee["name"]) > 0

        