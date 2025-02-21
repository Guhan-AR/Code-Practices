class Bill:
    """
    This object stores the total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    This object stores the things like name , number of days they stayed and payment of each flatmate.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def bill(self,flatmate1,flatemate2,bill):
        if flatmate1.days_in_house + flatemate2.days_in_house <= total.period:
            p1,p2 = (flatmate1.days_in_house/(flatmate1.days_in_house + flatemate2.days_in_house)) * bill.amount , (flatemate2.days_in_house/(flatmate1.days_in_house + flatemate2.days_in_house)) * bill.amount
            return [p1,p2]
        else:
            print("exceeding stay, or wrong input")


class PdfReport:
    """
    This object is fully focused of making a pdf of the bill
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def generate(self, flatemate1, flatemate2, bill):
        pass

total = Bill(500,30)
Guhan = Flatmate("Guhan",10)
AR = Flatmate("AR",20)
Bill = Guhan.bill(Guhan,AR,total)
print(Bill[0],Bill[1])