import webbrowser


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


class PdfReport:
    """
    This class contains the functionality to create a bill PDF for the flatmates.
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def generate_pdf_by_input(self, flatmate_1, flatmate_2, bill, fpay1, fpay2):
        from fpdf import FPDF

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
        pdf.cell(w=150, h=40, txt=bill.month, border=0, ln=1)

        # Inserting the Flatmate 1's output
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=90, h=25, txt=flatmate_1.name, border=0)
        pdf.cell(w=90, h=25, txt=str(fpay1) , border=0, ln=1)

        # Inserting the flatemate 2's output
        pdf.cell(w=90, h=25, txt=flatmate_2.name, border=0)
        pdf.cell(w=90, h=25, txt= str(fpay2), border=0, ln=1)

        pdf.output(self.file_name)
        webbrowser.open(self.file_name)

    def generate_pdf_by_operation(self, flatmate_1, flatmate_2, bill):
        from fpdf import FPDF

        flatmate_1_pays = str(flatmate_1.pays(bill, flatmate_2))
        flatmate_2_pays = str(flatmate_2.pays(bill, flatmate_1))

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
        pdf.cell(w=150, h=40, txt=bill.month, border=0, ln=1)

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
    the_bill = Bill(amount=120, period=30, month= "March 2024")
    person_1 = Flatmate(name="name_1", days_in_house=1)
    person_2 = Flatmate(name="name_2", days_in_house=2)
    a = person_2.pays(bill=the_bill, another_person=person_1)
    b = person_1.pays(bill=the_bill, another_person=person_2)
    print(f"Person 2 pays: {a:.2f}")
    print(f"Person 1 pays: {b:.2f}")
    print(f"Total: {a + b:.2f}")
    c=PdfReport(file_name="Bill.pdf")
    c.generate_pdf_by_input(person_1, person_2, the_bill, a, b)


def input_function():

    # for Bill Class
    amount = int(input("Enter the amount:"))
    period = int(input("Enter the whole time period of Rental:"))
    Month = input("Month of stay:")

    person_1_name = str(input("Name of person one:"))
    person_1_days_in_house = int(input("Number of Days in house by person One:"))

    person_2_name = str(input("Name of person Two:"))
    person_2_days_in_house = int(input("Number of Days in house by person Two:"))

    the_bill = Bill(amount, period, Month)
    person_1 = Flatmate(name = person_1_name, days_in_house = person_1_days_in_house)
    person_2 = Flatmate(name = person_2_name, days_in_house = person_2_days_in_house)

    b = person_2.pays(bill=the_bill, another_person=person_1)
    a = person_1.pays(bill=the_bill, another_person=person_2)

    print(f"Person 1 pays: {a:.2f}")
    print(f"Person 2 pays: {b:.2f}")
    print(f"Total: {a + b:.2f}")
    c = PdfReport("Bill.pdf")
    c.generate_pdf_by_input(person_1, person_2, the_bill, a, b)


tester_function()
# input_function()