# import modules
import csv


def Overhead_Function(filename):
    """
    This function will find the highest overheads and its category
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
    # setting max_category to keep track of the day when the highest value of the net profit occurred
    max_category = data[0][0]
    # setting max_overheads to keep track of the highest value of the net profit
    max_overheads = data[0][1]
    # iterate each data with loop
    for index in range(1, len(data)):
        if data[index][1] > max_overheads:
            # If a value is found that is higher than the current maximum,
            # the value of max_category can be updated to reflect the new maximum.
            max_category = data[index][0]
            # If a value is found that is higher than the current maximum, 
            # the value of max_overheads can be updated to reflect the new maximum.
            max_overheads = data[index][1]
            
    # write the statement to the txt file
    with open(filename, mode='w') as f:
        f.write(f"[HIGHEST OVERHEADS] {max_category.upper()}: {max_overheads}%" +'\n')
