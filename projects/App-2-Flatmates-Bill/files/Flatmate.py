class Flatmate:
    """
    This object stores the things like name , number of days they stayed and payment of each flatmate.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def bill(self,flatmate1,flatemate2,bill):
        p1,p2 = (flatmate1.days_in_house/(flatmate1.days_in_house + flatemate2.days_in_house)) * bill.amount , (flatemate2.days_in_house/(flatmate1.days_in_house + flatemate2.days_in_house)) * bill.amount
        # print("inside bill method:",p1,p2)
        return round(p1),round(p2)
