import sys
import os as os

# setup path variables
sys.path.insert(0, "/home/kemal/Programming/Python/ReportGenerator")
from TestReport import TestReport


def generateReports(articulation_type=None, benchmark_problem=None):
    load_folder = '/home/kemal/Programming/Python/Articulation/data/txts_and_plots'
    save_folder = '/home/kemal/Programming/Python/Articulation/data/pdfs'
    load_folder_txts = load_folder + '/' + articulation_type + '/' + benchmark_problem + '/txts/'
    load_folder_plots = load_folder + '/' + articulation_type + '/' + benchmark_problem + '/plots/'
    save_folder = save_folder + '/' + articulation_type + '/' + benchmark_problem + '/'
    os.chdir(load_folder_txts)
    txt_file_names = os.listdir(load_folder_txts)
    for file_name in txt_file_names:
        pdf = TestReport(raw_data_folder=load_folder_txts, file_name=file_name.replace('.txt', ''))
        pdf.alias_nb_pages()
        pdf.add_from_txt()
        pdf.add_image(load_folder_plots)
        os.chdir(save_folder)
        pdf.meta_data()
        pdf.output("r_" + file_name + '.pdf', 'F')


if __name__ == '__main__':
    generateReports('aposteriori', 'BK1')

