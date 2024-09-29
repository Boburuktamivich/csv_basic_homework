import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    reader = csv.reader(data)
    a = next(reader)
    return len(a)
data = open("data.csv", 'r')
print(find_number_of_columns(data))