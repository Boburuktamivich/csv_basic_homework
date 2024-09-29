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
    a = next(reader)
    return a[0]

# Read the csv file
data = open('data.csv', 'r')
print(get_first_column(data))