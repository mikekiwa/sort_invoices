import csv
import shutil
import re
import os


def read_csv_report(filename):
    file_list = []
    with open(filename, 'r') as my_file:
        csv_reader = csv.reader(my_file, delimiter=',')
        for row in csv_reader:
            file_list.append(row)
    return file_list


def create_folder_structure(root_path, company, year, vendor):
    new_vendor = re.sub('[>,\/]', '', vendor)
    dir_path = root_path + os.path.sep + company + os.path.sep + year + os.path.sep + new_vendor
    if not (os.path.exists(dir_path)):
        os.makedirs(dir_path)
    return dir_path


def copy_files(file_list, src_path, root_path):
    for each_file in file_list:
        dest_path = create_folder_structure(root_path, each_file[0], each_file[3], each_file[5])
        new_invoice_num = re.sub('[\/]', '-', each_file[1])
        new_date = re.sub(',\s', ' ', each_file[2])
        src_file = src_path + os.path.sep + each_file[7]+'.pdf'
        dest_file = dest_path + os.path.sep + new_invoice_num + '-' + new_date + '.pdf'
        if not os.path.isfile(src_file):
            print('file missing {0}'.format(dest_file))
        else:
            print(dest_file)
            shutil.copy2(src_file, dest_file)


def missing_files(file_list, files_location):
    count = 0
    missing_file_list = []
    for each_file in file_list:
        src_file = files_location+'\\'+each_file[7]+'.pdf'
        if not os.path.isfile(src_file):
            missing_file_list.append(each_file)
            count += 1
    print(count)
    return missing_file_list


def create_csv_file(filepath, error_list):
    with open(filepath, 'w+', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for item in error_list:
            csv_writer.writerow(item)


if __name__ == '__main__':
    invoice_list = read_csv_report(r'C:\Users\vinod\Desktop\invoice_list.csv')
    not_found_list = missing_files(invoice_list, r'C:\Users\vinod\Downloads\ConcurInvoices\InvoiceFiles')
    create_csv_file(r'C:\Users\vinod\Desktop\missing_invoices.csv', not_found_list)

    copy_files(invoice_list, r'C:\Users\vinod\Downloads\ConcurInvoices\InvoiceFiles', r'C:\Users\vinod\Downloads')
