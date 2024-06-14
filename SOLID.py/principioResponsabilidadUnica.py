# Aqui estamos violando el principio de responsabilidad única. Ya que esta clase tiene dos responsabilidades. Recuerda que el constructor no cuenta como una responsabilidad.

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_employee_data(self):
        return f"Name: {self.name}, ID: {self.id}"
    
    # Maneja la lógica de la persistencia del empleado
    def save_employee_data(self):
        with open(f"{self.id}.txt", "w") as f:
            f.write(self.get_employee_data())

# Ahora vamos a separar las responsabilidades en dos clases diferentes para cumplir con el principio de responsabilidad única.

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_employee_data(self):
        return f"Name: {self.name}, ID: {self.id}"

class EmployeePersistence:
    @staticmethod
    def save_employee_data(employee):
        if not isinstance(employee, Employee):
            raise ValueError("Expected an instance of Employee")
        with open(f"{employee.id}.txt", "w") as f:
            f.write(employee.get_employee_data())

# Ahora tenemos dos clases, una para manejar la lógica del empleado y otra para manejar la persistencia del empleado.