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
        self.n_obj = 0
        self.n_dec = 0

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
        data = []
        with open(self.file_name + '.txt', 'r') as f:
            for line in f:
                data.append(line)
        print(data)

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

        # here comes the new piece of code
        # self.n_obj = int(data[0].replace("\n", ''))
        # self.n_dec = int(data[1].replace("\n", ''))
        data = data[2:]  # remove 1st two elements
        # headers = ['-----------------Algorithm parameters-----------------', 'Delta = ', 'Max iterations = ', 'M (criteria punishment) = ', 'Seed = ', 'Max loops = ',
        #            'Min progress = ', 'Tabu list max length = ', 'Weights = {', '}', '-----------------Performance-----------------',
        #            'Termination reason: ', 'Last iteration = ', 'Initial solution: ', 'x = {', '}', 'f = {', '}', '---------',
        #            'Final solution: ', 'x = {', '}', 'y = {', '}']
        # for ind, head in enumerate(headers):
        #     self.set_font('Arial', 'B', 10)
        #     self.cell(w=40, h=10, txt=head)





    def add_from_txt_modified(self):
        self.add_page()
        if not os.path.exists(self.raw_data_folder):
            os.makedirs(self.raw_data_folder)
        try:
            os.chdir(self.raw_data_folder)
        except OSError:
            print('Could not cwd to: ', self.raw_data_folder)
            print('Exiting.')
            sys.exit(2)
        with open(self.file_name + '.txt', 'r') as file:
            data = file.read()


        # print(type(data))
        # print(data)
        lst = self.dict_to_lst(data)


    def add_tuple(self, tup):
        if type(tup[1]) is list:
            self.set_font('Arial', 'B', 10)
            self.cell(w=30, h=10, txt=tup[0], ln=1)
            for nested_tup in tup[1]:
                self.add_tuple(nested_tup)
        else:
            self.set_font('Arial', 'B', 10)
            self.cell(w=30, h=10, txt=tup[0] + " = ")
            self.set_font('Arial', '', 10)
            self.cell(w=40, h=10, txt=tup[1], ln=1)

    def dict_to_lst(self, dict_):
        # this list contains tuples of json data. The name of the attribute, and its value.
        # it can also contain a recursive type of its own, that is, another list which contains only tuples.
        lst = []
        for key, val in dict_.items():
            if type(val) is dict:
                # the dictonary contains a nested dictionary. Do a recursive call, and then just append the list
                # returned by the nested dictionary as an element as well. Object is still a tuple.
                lst.append((key, self.dict_to_lst(val)))
            lst.append((key, str(val)))
        return lst

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
        self.image(self.file_name + '.png', x=45, w=115)  # check whether x=45 does the job

