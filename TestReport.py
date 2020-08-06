from fpdf import FPDF
from datetime import datetime
import os as os
import sys


class TestReport(FPDF):
    """
    This class simply defines how the test data is read from the raw txt files, and how the image is embedded into
    the pdf report. It accepts the path to the raw data location, as well as the filename to where it should save
    the generated pdf report.
    It is somewhat hardcoded and should be modified when the option to generate aposteriori and progressive reports is
    to be added.
    """
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
        # Procedure for adding data from the raw txt file:
        # load the txt file, line-by-line and add all the lines to the list "data".
        # Since every line is an entry, to make a distinction between the name of attribute and its value
        # split the data uppon the equality sign "==". Write the name of the attribute bolded, while its value
        # stays in common format.
        data = []
        with open(self.file_name + '.txt', 'r') as f:
            for line in f:
                data.append(line)
        # data is a list of strings
        for entry in data:
            pom = entry.split("==")
            self.set_font('Arial', 'B', 10)
            if len(pom) is 1:
                self.cell(w=50, h=4, txt=pom[0], ln=1)
            else:
                self.cell(w=50, h=4, txt=pom[0])
                self.set_font('Arial', '', 10)
                self.cell(w=50, h=4, txt=pom[1], ln=1)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    # This could be a lot cleaner but to save time as a requirement the image location path needs to be passed
    # as an additional argument to this method.
    def add_image(self, image_location):
        if not os.path.exists(image_location):
            os.makedirs(image_location)
        try:
            os.chdir(image_location)
        except OSError:
            print('Could not cwd to: ', image_location)
            print('Exiting.')
            sys.exit(2)
        self.image(self.file_name + '.png', x=45, w=115)

