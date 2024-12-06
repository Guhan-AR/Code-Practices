import webbrowser


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

    def pays(self, bill, another_person):
        """
        Calculate how much the flatmate needs to pay.
        """
        if self.days_in_house + another_person.days_in_house != 0:
            return self.days_in_house/(self.days_in_house+another_person.days_in_house)*bill.amount
        else:
            return bill.amount/2


class PdfReport:
    """
    This class contains the functionality to create a bill PDF for the flatmates.
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def generate(self, flatmate_1, flatmate_2, bill):
        from fpdf import FPDF

        flatmate_1_pays = str(flatmate_1.pays(bill, flatmate_2))
        flatmate_2_pays = str(flatmate_2.pays(bill,flatmate_1))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Inserting Image
        pdf.image(name="house.png", w=30, h=30)

        # Inserting Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatemates Bill", border=0, align="C", ln=1)

        # Inserting Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=90, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt="March 2024", border=0, ln=1)

        # Inserting the Flatmate 1's output
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=90, h=25, txt=flatmate_1.name, border=0)
        pdf.cell(w=90, h=25, txt=flatmate_1_pays, border=0, ln=1)

        # Inserting the flatemate 2's output
        pdf.cell(w=90, h=25, txt=flatmate_2.name, border=0)
        pdf.cell(w=90, h=25, txt=flatmate_2_pays, border=0, ln=1)

        pdf.output(self.file_name)
        webbrowser.open(self.file_name)

def tester_function():
    the_bill = Bill(amount=120, period=30)
    person_1 = Flatmate(name="name_1", days_in_house=10)
    person_2 = Flatmate(name="name_2", days_in_house=2)
    a = person_2.pays(bill=the_bill, another_person=person_1)
    b = person_1.pays(bill=the_bill, another_person=person_2)
    print(f"Person 2 pays: {a:.2f}")
    print(f"Person 1 pays: {b:.2f}")
    print(f"Total: {a + b:.2f}")
    c=PdfReport(file_name="Bill.pdf")
    c.generate(person_1, person_2, the_bill)


def input_function():
    the_bill = Bill(amount=int(input("Enter the amount:")), period=int(input("Enter the whole time period of Rental:")))    
    person_1 = Flatmate(name=str(input("Name of person one:")), days_in_house=int(input("Number of Days in house by person One:")))
    person_2 = Flatmate(name=str(input("Name of person one:")), days_in_house=int(input("Number of Days in house by person One:")))
    a = person_2.pays(bill=the_bill, another_person=person_1)
    b = person_1.pays(bill=the_bill, another_person=person_2)
    print(f"Person 2 pays: {a:.2f}")
    print(f"Person 1 pays: {b:.2f}")
    print(f"Total: {a + b:.2f}")


tester_function()
#input_function()