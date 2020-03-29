from fpdf import FPDF
from datetime import date
from datetime import datetime
import json as json
import os as os


class PDF(FPDF):
    def meta_data(self):
        self.set_title("Test Report")
        self.set_author("Kemal Altwlkany")

    def header(self):
        # Logo
        self.image('etfsa_en.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(35)
        # Title
        self.cell(50, 10, 'LocalSearch, BK1', 1, 0, 'C')
        self.set_font('Arial', '', 11)
        self.cell(50, 10, datetime.now().strftime("%A, %d. %B %Y.  %H:%M:%S"))
        # Line break
        self.ln(20)

    def test_results(self):
        pass

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def save_file(self):
        pass
#
print date.today()
print date.today().strftime("%A, %d. %B %Y")
# print type(datetime.now().strftime("%A, %d. %B %Y.  %H:%M:%S"))
# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
for i in range(1, 41):
    pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
pdf.output('tuto2.pdf', 'F')



# pdf = FPDF('P', 'mm', 'A4')  # portrait, millimeters, A4
# pdf.add_page()
# pdf.set_font('Arial', 'B', 24)
# pdf.cell(w=0, h=0, txt = 'Hello World!', border=0, ln=1, align='C')
# pdf.set_font('Arial', '', 12)
# pdf.cell(w=0, h=0, txt = 'I am right now testing whether this is working or not')
# pdf.output('tutorial1.pdf', 'F')
#
