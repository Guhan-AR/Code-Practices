from files.pdfgenerator import PdfReport


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
        p1,p2 = (flatmate1.days_in_house/(flatmate1.days_in_house + flatemate2.days_in_house)) * bill.amount , (flatemate2.days_in_house/(flatmate1.days_in_house + flatemate2.days_in_house)) * bill.amount
        # print("inside bill method:",p1,p2)
        return [p1,p2]

total = Bill(1000,30)
Guhan = Flatmate("Guhan",20)
AR = Flatmate("AR",20)
total_bill = Guhan.bill(Guhan,AR,total)
print(round(total_bill[0]),round(total_bill[1]))
print(total_bill[0]+total_bill[1]," ",total.amount)
pdf = PdfReport("Feb")
pdf.generate(Guhan.name,AR.name,total_bill[0],total_bill[1])