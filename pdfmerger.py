from os import listdir, path, startfile
from tkinter.filedialog import askdirectory
from PyPDF2 import PdfFileMerger

def search_folder():
    path_name = askdirectory()
    return path_name

def merged_name(path_name):
    if input('Would like to customise the merged pdf\'s name? (y or n): ') == 'y':
        merged_filename = input('Enter name of merged PDF: ')
    else:
        merged_filename = path.basename(path_name)
    return merged_filename


def merge_PDFs(path_name, merged_filename):
    merger = PdfFileMerger()

    for item in listdir(path_name):
        if item.endswith('pdf'):
            merger.append(path_name + '/' + item)

    full_mergedPDF_path = path_name + "/" + merged_filename + '.pdf'
    merger.write(full_mergedPDF_path)
    merger.close()
    return full_mergedPDF_path


print('Welcome to PDFMerg.ed \n')

if input('Would you like to proceed to choose your folder containing the PDFs to be merged? (y or n): ') == 'y':

    repeat = 'y'
    while repeat == 'y':

        desired_folder = search_folder()
        mergedPDF_name = merged_name(desired_folder)
        print('Merging PDFs in: ' + desired_folder + '...')
        mergedPDF_path = merge_PDFs(desired_folder, mergedPDF_name)

        startfile(mergedPDF_path)

        print('\nMerging complete...')

        repeat = input('Would you like to merge PDFs again? (y or n): ')

print('\nBye...')