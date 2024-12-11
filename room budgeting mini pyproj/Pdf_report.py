import webbrowser
import os

class PdfReport:
    """
    This class contains the functionality to create a bill PDF for the flatmates.
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def generate_pdf_by_input(self, flatmate_1, flatmate_2, bill, fpay1, fpay2):
        from fpdf import FPDF
        path = "file:///A:/A/Python-and-Algorithms/room%20budgeting%20mini%20pyproj"

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Inserting Image
        pdf.image(name="files/house.png", w=30, h=30)

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

        os.chdir("files")

        pdf.output(self.file_name)
        webbrowser.open(self.file_name)

    def generate_pdf_by_operation(self, flatmate_1, flatmate_2, bill):
        from fpdf import FPDF

        flatmate_1_pays = str(flatmate_1.pays(bill, flatmate_2))
        flatmate_2_pays = str(flatmate_2.pays(bill, flatmate_1))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Inserting Image
        pdf.image(name="files/house.png", w=30, h=30)

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
