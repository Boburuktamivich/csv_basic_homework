import csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    reader = csv.reader(data)
    row = list(data)[0]
    return row
data = open('data.csv', 'r')
print(get_first_column(data))