from files.Flatmate import Flatmate
from files.pdfgenerator import PdfReport


class Bill:
    """
    This object stores the total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


def testing():
    total = Bill(1000,30)
    Guhan = Flatmate("Guhan", 1)
    AR = Flatmate("AR", 20)
    total_bill = Guhan.bill(Guhan,AR,total)
    print(round(total_bill[0]),round(total_bill[1]))
    print(total_bill[0]+total_bill[1]," ",total.amount)
    pdf = PdfReport("Feb")
    pdf.generate(Guhan.name,AR.name,total_bill[0],total_bill[1])

def main():
    pdf = PdfReport(input("Month you stayed[File name]:"))
    total = Bill(int(input("Enter the total amount of Bill:")), int(input("Total period of stay:")))
    person1 = Flatmate(input("Enter your Name:"), int(input("Number of days stayed:")))
    person2 = Flatmate(input("Enter flatemate name:"), int(input("Number of days he/she stayed:")))
    bill_1,bill_2 = person1.bill(person1, person2, total)
    print(bill_1, bill_2)
    print(bill_1+bill_2, " ", total.amount)
    pdf.generate(person1.name, person2.name, bill_1, bill_2)

# main()
testing()
