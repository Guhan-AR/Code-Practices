print("hi")
class Bill:
    """
    This class contains the data about the bill.
    """
    def __init__(self, amount, period):
        """
        Initialize the Bill object.
        :param amount: The total bill amount.
        :param period: The total period of time for the bill.
        """
        self.amount = amount
        self.period = period


class Flatmate:
    """
    This class contains the data about the flatmates.
    """
    def __init__(self, name, days_in_house):
        """
        Initialize the Flatmate object.
        :param name: Name of the flatmate.
        :param days_in_house: Number of days the flatmate stayed in the house.
        """
        self.name = name
        self.days_in_house = days_in_house

    def calculate_unused_days(self, bill, another_person):
        """
        Calculate unused days by both flatmates.
        :param bill: Bill object containing the period and total amount.
        :param another_person: Another flatmate's details.
        :return: Unused days divided by two.
        """
        return (bill.period - (self.days_in_house + another_person.days_in_house)) / 2

    def pays(self, bill, another_person):
        """
        Calculate how much the flatmate needs to pay.
        :param bill: Bill object containing the period and total amount.
        :param another_person: Another flatmate's details.
        :return: Amount the flatmate pays.
        """
        unused_days = self.calculate_unused_days(bill, another_person)
        return bill.amount * (self.days_in_house / bill.period) + bill.amount * (unused_days / bill.period)


class PdfReport:
    """
    This class contains the functionality to create a bill PDF for the flatmates.
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def generate(self, flatmate_1, flatmate_2, bill):
        # Placeholder for PDF generation logic.
        pass


def tester_function():
    the_bill = Bill(amount=120, period=30)
    person_1 = Flatmate(name="name_1", days_in_house=4)
    person_2 = Flatmate(name="name_2", days_in_house=5)
    a = person_2.pays(bill=the_bill, another_person=person_1)
    b = person_1.pays(bill=the_bill, another_person=person_2)
    print(f"Person 2 pays: {a:.2f}")
    print(f"Person 1 pays: {b:.2f}")
    print(f"Total: {a + b:.2f}")


tester_function()
