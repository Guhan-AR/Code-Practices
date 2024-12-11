from Pdf_report import PdfReport
from flat import Bill, Flatmate


def tester_function():
    the_bill = Bill(amount=120, period=30, month="March_2024")
    person_1 = Flatmate(name="name_1", days_in_house=1)
    person_2 = Flatmate(name="name_2", days_in_house=2)
    a = person_2.pays(bill=the_bill, another_person=person_1)
    b = person_1.pays(bill=the_bill, another_person=person_2)
    print(f"Person 2 pays: {a:.2f}")
    print(f"Person 1 pays: {b:.2f}")
    print(f"Total: {a + b:.2f}")
    c = PdfReport(file_name=f"{the_bill.month}.pdf")
    c.generate_pdf_by_input(person_1, person_2, the_bill, a, b)


def input_function():

    # for Bill Class
    amount = int(input("Enter the amount (E.g 100) : "))
    period = int(input("Enter the whole time period of Rental in (days) : "))
    month = input("Month of stay (E.g January 2024) : ")

    # person 1
    person_1_name = str(input("What is your name : "))
    person_1_days_in_house = int(input("How many days do you stayed : "))

    person_2_name = str(input("Name of Your Flatmate : "))
    person_2_days_in_house = int(input(f"Number of Days that {person_2_name} stayed : "))

    the_bill = Bill(amount, period, month)
    person_1 = Flatmate(name = person_1_name, days_in_house = person_1_days_in_house)
    person_2 = Flatmate(name = person_2_name, days_in_house = person_2_days_in_house)

    b = person_2.pays(bill=the_bill, another_person=person_1)
    a = person_1.pays(bill=the_bill, another_person=person_2)

    print(f"{person_1.name} pays: {a:.2f}")
    print(f"{person_2.name} pays: {b:.2f}")
    print(f"Total: {a + b:.2f}")
    c = PdfReport(f"{the_bill.month}.pdf")
    c.generate_pdf_by_input(person_1, person_2, the_bill, a, b)

# tester_function()
input_function()