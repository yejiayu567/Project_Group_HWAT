# import modules
import csv


def Profit_Loss_Function(filename):
    """
    This function will compute the difference in net profit values between days, 
    return the profit deficit value if the current day value is less than any of the previous days, 
    or return a statement if the current day value is the highest of all days.
    One parameter is required: filename
    """

    with open('csv_reports/profit_and_loss.csv') as file:
        # reading csv file
        reader = csv.reader(file)
        # skip reading the header
        next(reader)
        # create empty lists to store value
        data = []
        # iterate each row with loop
        # 
        for row in reader:
            data.append([(row[0]), (float(row[4]))])
    # sort the data by date
    sorted(data)
    # determine whether the data is surplus
    surplus = True
    #setting a for loop that will run through the data in data list by finding the number of elements by len(data)
    for index in range(len(data) - 1):
        # check if the net profit of the next day (data[index + 1][1]) is less than the net profit of the current day (data[index][1]).
        if data[index + 1][1] < data[index][1]:
            # if net profit of the next day is less than the net profit of the current day, surplus will return false
            surplus = False
            # finding the day value for the next row of data
            day = data[index + 1][0]
            # calculating the difference between the net profit of two consecutive days, and assigning it to the variable dif.
            dif = data[index][1] - data[index + 1][1]
            # write the statement into the txt file
            with open(filename, mode='a') as f:
                # append to the end of the txt file
                f.write(f'[PROFIT DEFICIT]DAY: ({day}:.1f), AMOUNT: USD{dif}')

    # if the data is surplus, return the statement to the txt file
    if surplus:
        with open(filename, mode='a') as f:
            f.write('[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
