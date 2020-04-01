import sys
import os as os

# setup path variables
sys.path.insert(0, "/home/kemal/Programming/Python/ReportGenerator")

from TestReport import TestReport



class ReportGenerator:
    """
    A wrapper around the fpdf class and the TestReport class. This enables to generate multiple reports at once,
    while the class TestReport is used to generate a single report. In this class I process all the data, such as
    check the query (which tests do I want to generate a pdf for), and then simply pass those results to the
    TestReport class.
    """
    rel_path = "/home/kemal/Programming/Python/Articulation/Tests/test_results_raw"
    save_folder_rel_path = "/home/kemal/Programming/Python/ReportGenerator/Reports"
    # this is where all test results are located. (the raw data, .txt and .png)

    def __init__(self, reportType=None, alg_family=None, alg_name=None, problem_name=None):
        self.reportType = reportType
        self.alg_family = alg_family
        self.alg_name = alg_name
        self.problem_name = problem_name
        self.load_folder = ""
        self.save_folder = None
        self.file_names = []

    def setupVariables(self):
        # This function prepares the data such as setting up load/save folder paths, and determining the files
        # to be processed
        # Find raw data folder
        self.load_folder = os.path.join(ReportGenerator.rel_path, self.alg_family, self.alg_name, self.problem_name)
        if not os.path.exists(self.load_folder):
            os.makedirs(self.load_folder)
        try:
            os.chdir(self.load_folder)
        except OSError:
            print('Could not cwd to: ', self.load_folder)
            print('Exiting with flag 11')
            sys.exit(11)

        # Create save_folder if it does not exist
        if self.save_folder is None:
            self.save_folder = os.path.join(ReportGenerator.save_folder_rel_path, self.alg_family, self.alg_name, self.problem_name)
            if not os.path.exists(self.save_folder):
                os.makedirs(self.save_folder)

        if self.reportType is "latest":
            # Reports have a unique ID. The latest report has the highest ID value.
            entries = os.listdir(self.load_folder)
            test_ID = len(entries) // 2
            self.file_names.append(self.problem_name + "_test_ID_" + str(test_ID))
        elif self.reportType is "all":
            entries = os.listdir(self.load_folder)
            n_tests = len(entries) // 2
            for test_ID in range(n_tests):
                self.file_names.append(self.problem_name + "_test_ID_" + str(test_ID))
        elif self.reportType is "new":
            entries = os.listdir(self.load_folder)
            n_tests = len(entries) // 2

            # we now check how many reports exist in the save folder
            n_reports = os.listdir(self.save_folder)
            n_reports = len(n_reports)
            for test_ID in range(n_reports, n_tests, 1):
                self.file_names.append(self.problem_name + "_test_ID_" + str(test_ID))

    def generateReports(self):
        for file_name in self.file_names:
            pdf = TestReport(raw_data_folder=self.load_folder, file_name=file_name)
            pdf.alias_nb_pages()
            pdf.add_from_txt()
            pdf.add_image()
            os.chdir(self.save_folder)
            pdf.meta_data()
            pdf.output("r_" + file_name + '.pdf', 'F')


if __name__ == '__main__':
    # x = ReportGenerator(reportType="new", alg_family="LS", alg_name="LS_apriori", problem_name="BK1")
    # x = ReportGenerator(reportType="new", alg_family="TS", alg_name="TS_apriori", problem_name="BK1")
    # x = ReportGenerator(reportType="new", alg_family="TS", alg_name="TS_apriori", problem_name="IM1")
    x = ReportGenerator(reportType="new", alg_family="TS", alg_name="TS_apriori", problem_name="BK1")
    x.setupVariables()
    x.generateReports()

