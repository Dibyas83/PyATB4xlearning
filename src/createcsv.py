
"""


Create a Csv File Using Python
Below are some of the ways by which we can create a CSV file using Python:

Using Python CSV Module
Using Pandas Library
Using plain text file writing
Using Python CSV Module
Now, Python provides a CSV module to work with CSV files, which allows Python programs to create, read, and manipulate tabular data in the form of CSV, This 'CSV' module provides many functions and classes for working with CSV files, It includes functions for reading and writing CSV data, as well as classes like csv.reader and csv.writer for more advanced operations.

"""

import csv

data = [
    ['Name', 'Age', 'City'],
    ['Aman', 28, 'Pune'],
    ['Poonam', 24, 'Jaipur'],
    ['Bobby', 32, 'Delhi']
    ]
# File path for the CSV file
csv_file_path = 'example.csv'
# Open the file in write mode
16
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print(f"CSV file '{csv_file_path}' created successfully")

import pandas as pd
data = {
    'Name': ['Rajat', 'Tarun', 'Bobby'],
    'Age': [30, 25, 35],
    'City': ['New York', 'Delhi', 'Pune']
}
# Step 3 Create a DataFrame using DataFrame function
df = pd.DataFrame(data)

# Step 4 Specify the file path to save data
csv_file_path = 'data.csv'
# Step 5 Write the DataFrame to a CSV file using to_csv() function where file path is passed
df.to_csv(csv_file_path, index=False)
print(f'CSV file &quot;{csv_file_path}&quot; has been created successfully.')
"""
Output:

Screenshot-2024-02-11-104520
File Creation Screenshot
Note: Ignore the deprecation warning message.

Csv File Output:

Screenshot-2024-02-11-102654
csv file
Using Plain Text File Writing
We can manually write data to a CSV file using basic file writing operations. While it is less common and less convenient than using the csv module or pandas, it's still possible and can be done.

"""
# data to be stored in csv in form of list of list
data = [
    ['Name', 'Gender', 'Age', 'Course'],
    ['Aman', 'M', 22, 'B.Tech'],
    ['Pankaj', 'M', 24, 'M.Tech'],
    ['Beena', 'F', '23', 'MBA']
]

# file path of csv to be stored

csv_file_path = 'ex3.csv'
# opening file in write mode using a context manager
with open(csv_file_path, mode='w') as file:

    for row in data:
        file.write(','.join(map(str, row)) + '\n')  # writing data row by row

print(f"CSV file '{csv_file_path}' created successfully!!!")