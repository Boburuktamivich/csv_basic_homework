import csv
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    reader = csv.reader(data)
    a = list(reader)
    return len(a)
data = open("data.csv", 'r')
print(find_number_of_rows(data))