from fpdf import FPDF
from datetime import datetime
import json as json
import os as os
import sys


class TestReport(FPDF):
    def __init__(self, orientation='P', unit='mm', format='A4', raw_data_folder=None, file_name=None):
        super(TestReport, self).__init__(orientation, unit, format)
        self.raw_data_folder = raw_data_folder
        self.file_name = file_name

    def meta_data(self):
        self.set_title("Test Report: " + self.file_name)
        self.set_author("Kemal Altwlkany")

    def header(self):
        # Logo
        self.image('/home/kemal/Programming/Python/ReportGenerator/etfsa_en.png', 10, 8, 25)
        self.set_font('Arial', 'B', 14)
        # Move to the right
        self.cell(40)
        # Title
        self.cell(80, 10, self.file_name, 1, 0, 'C')
        self.cell(10)
        self.set_font('Arial', '', 10)
        self.cell(60, 10, datetime.now().strftime("%A, %d. %B %Y.  %H:%M:%S"))
        # Line break
        self.ln(20)

    def add_from_txt(self):
        self.add_page()
        if not os.path.exists(self.raw_data_folder):
            os.makedirs(self.raw_data_folder)
        try:
            os.chdir(self.raw_data_folder)
        except OSError:
            print('Could not cwd to: ', self.raw_data_folder)
            print('Exiting.')
            sys.exit(2)

        self.set_font('Arial', '', 10)
        with open(self.file_name + '.txt', 'r') as json_file:
            data = json.load(json_file)
        self.write(5, json.dumps(data, indent=4))

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def add_image(self):
        if not os.path.exists(self.raw_data_folder):
            os.makedirs(self.raw_data_folder)
        try:
            os.chdir(self.raw_data_folder)
        except OSError:
            print('Could not cwd to: ', self.raw_data_folder)
            print('Exiting.')
            sys.exit(2)
        self.image(self.file_name + '.png', w=115)

