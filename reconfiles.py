import os.path
import csv


def read_all_files(path):
    all_invoices = []
    list_of_files = os.listdir(path)

    for file in list_of_files:
        with open(path+'\\'+file, 'r') as my_file:
            csv_reader = csv.reader(my_file, delimiter=',')
            for row in csv_reader:
                all_invoices.append(row)

    count = 0
    for invoice_file in all_invoices:
        print(invoice_file)
        count += 1

    print(count)


if __name__ == '__main__':
    read_all_files(r'C:\Users\vinod\Downloads\ConcurInvoices\Invoices')
