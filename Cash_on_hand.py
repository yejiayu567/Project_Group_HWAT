# import required modules
import csv


def COH_Function(filename):
    """
    This function will compute the difference in cash on hand values between days, 
    return the cash deficit value if the current day value is less than any of the previous days, 
    or return a statement if the current day value is the highest of all days.
    One parameter is required: filename
    """

    with open('csv_reports/cash_on_hand.csv') as file:
        # create csv reader object using csv
        data = csv.reader(file)
        # skip reading the header
        next(data)
        # create empty lists to store value
        data = []
        # iterate each row with loop
        for row in data:
            # append cash on hand data as a list back to each empty list
            data.append([(row[0]), float(row[1])])
    # sort the data by date
    sorted(data)
    # determine whether the data is surplus
    is_surplus = True
    for index in range(len(data) - 1):
        # find the deficit data and calculate the difference 
        if data[index + 1][1] < data[index][1]:
            is_surplus = False
            day = data[index + 1][0]
            diff = data[index][1] - data[index + 1][1]
            # write the statement in the txt file
            with open(filename, mode='a') as f:
                f.write(f'[CASH DEFICIT] DAY: ({day}:.1f), AMOUNT: USD{diff}')
    # if the data is surplus, return the statement to the txt file
    if is_surplus:
        with open(filename, mode='a') as f:
            f.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY" + "\n")
