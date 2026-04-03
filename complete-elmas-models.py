# ELMAS ERP Models

class Asset:
    def __init__(self, asset_id, name, value):
        self.asset_id = asset_id
        self.name = name
        self.value = value

class Employee:
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id
        self.name = name
        self.position = position

# Add additional models as necessary
