# import modules
import csv


def Overhead_Function(filename):
    """
    This function will find the highest overheads and category
    One parameter is required: filename
    """

    # read csv file
    with open('csv_reports/overheads.csv') as file:
        # create csv reader object using csv
        reader = csv.reader(file) 
        # skip reading the header
        next(reader)
        # create empty lists to store value
        data = []
        # iterate each row with loop
        for row in reader:
            data.append([(row[0]), (float(row[1]))])
    # find the highest overheads and category
    max_category = data[0][0]
    max_overheads = data[0][1]
    # iterate each data with loop
    for index in range(1, len(data)):
        if data[index][1] > max_overheads:
            max_category = data[index][0]
            max_overheads = data[index][1]
            
    # write the statement to the txt file
    with open(filename, mode='w') as f:
        f.write(f"[HIGHEST OVERHEADS] {max_category.upper()}: {max_overheads}%" +'\n')
