class Bill:
    """
    This class contains the data about the bill.
    """
    def __init__(self, amount, period, month):
        """
        Initialize the Bill object.
        :param amount: The total bill amount.
        :param period: The total period of time for the bill.
        """
        self.amount = amount
        self.period = period
        self.month = month


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

    def pays(self, bill, another_person):
        """
        Calculate how much the flatmate needs to pay.
        """
        if self.days_in_house + another_person.days_in_house != 0:
            return self.days_in_house/(self.days_in_house+another_person.days_in_house)*bill.amount
        else:
            return bill.amount/2
