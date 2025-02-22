from fpdf import FPDF

class Bill_Essentials(FPDF):

    def header(self):
        self.image("house.png",10,8,33)
        self.set_font("Arial","B",12)
        self.cell(80)
        self.cell(40, 10, "Flatemates Bill", border=True, ln=1, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


class PdfReport:
    """
    This object is fully focused of making a pdf of the bill
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def generate(self, flatemate1, flatemate2, bill1,bill2):
        pdf = Bill_Essentials()
        pdf.add_page()

        pdf.set_font("Arial", "B", 14)
        pdf.cell(70, 18, "Monthly Rent and Utilities Bill", ln=True, align="C")
        pdf.ln(10)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(40, 10, "Flatmate", border=1)
        pdf.cell(50, 10, "Amount Due (Rs.)", border=1)
        pdf.ln()

        pdf.set_font("Arial", "B", 12)
        pdf.cell(40, 10, flatemate1, border=1)
        pdf.cell(50, 10, str(bill1), border=1)
        pdf.ln()

        pdf.set_font("Arial", "B", 12)
        pdf.cell(40, 10, flatemate2, border=1)
        pdf.cell(50, 10, str(bill2), border=1)
        pdf.ln()

        the_total=bill1+bill2
        pdf.set_font("Arial", "B", 12)
        pdf.cell(40, 10, "total", border=1)
        pdf.cell(50, 10, str(the_total), border=1)
        pdf.ln()

        pdf.output(f"{self.file_name}.pdf")
        print("success")