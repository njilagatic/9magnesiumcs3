class Patient: # Super Class Patient
    def __init__(self, name: str, bill_amount: float):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self): # returns name of patient
        return self.name

    def set_name(self, name: str): # sets name of patient
        self.name = name

    def get_bill_amount(self): # returns bill amount of patient
        return self.bill_amount

    def set_bill_amount(self, bill_amount: float): # sets bill amount, check if value is positive
        if bill_amount >= 0:
            self.bill_amount = bill_amount
        else:
            print("Bill amount cannot be negative.")

    def calculate_bill(self): # calculates final bill, to be overridden by subclasses
        return self.bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")

class SeniorPatient(Patient): # Sub class Senior Patient inherits from Patient
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill(self): # calculates final bill with 20% discount
        discount = 0.2 * self.bill_amount
        return self.bill_amount - discount

    def display_patient_type(self): # displays patient type (Senior citizen)
        print("Patient Type: Senior Citizen")

class PhilHealthPatient(Patient): # Sub class PhilHealth Patient inherits from Patient
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill(self): # calculates the final bill with 15% discount for Philhealth patients
        discount =  0.15 * self.bill_amount
        return self.bill_amount - discount

    def display_patient_type(self): # displays patient type which is Philhealth member
            print("Patient Type: PhilHealth Member")

if __name__ == "__main__": # main execution
    print("Hospital Billing System")
    print("-----------------------")

    Patient1 = Patient("Juan Dela Cruz", 15000.00) # creates instance of Patient
    Patient2 = SeniorPatient("Maria Santos", 15000.00) # creates instance
    Patient3 = PhilHealthPatient("Pedro Reyes", 15000.00) # creates instance

    # Displays patient info and final bill
    Patient1.display_patient_type() 
    print(f"Patient Name: {Patient1.get_name()}")
    print(f"Original Bill: ₱{Patient1.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{Patient1.calculate_bill():,.2f}")

    # Displays patient info & final bill for Senior Patient
    print()
    Patient2.display_patient_type()
    print(f"Patient Name: {Patient2.get_name()}")
    print(f"Original Bill: ₱{Patient2.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{Patient2.calculate_bill():,.2f}")
    
    # Displays patient info & final bill for PhilHealth Patient
    print()
    Patient3.display_patient_type()
    print(f"Patient Name: {Patient3.get_name()}")
    print(f"Original Bill: ₱{Patient3.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{Patient3.calculate_bill():,.2f}")