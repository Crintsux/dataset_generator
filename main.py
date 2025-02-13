import csv
import random

# Fake date generation utility.
from faker import Faker
fake = Faker()

# Generates a row of data for a given sample list object. 
# Value and date are generated randomly both within beliveable limits.
def generate_row(sample):
      return [sample['location'], 'Test', sample['matrix'], sample['compound'], 
              round(random.uniform(0, sample['limit']), 5), sample['unit'], 
              fake.date_between(start_date='-30y', end_date='today').strftime('%d.%m.%Y')]


# Uses the generate_row() function to create a subset of data of a specified number of rows.
def generate_subset(rows, sample):
      subset = []
      for i in range(rows):
            subset.append(generate_row(sample))
      return subset  

# Prepare the file using the csv module. Expects a 'files' directiory
# with an empty 'dataset.csv' file in it.
with open('files/dataset.csv', 'w') as file:
    dataset = csv.writer(file)
    
    # Name the column headers.
    column_headers = ['Location', 'Project', 'Matrix', 'Compound', 
                 'Value', 'Unit', 'Date of Measurement']
    dataset.writerow(column_headers)

    # Somewhat realistic looking base for our data set. Limit puts a ceiling
    # on the random number generation to make the values look beliveable.
    samples = [
      {'location':'Congo', 'compound': 'Dielrin', 'matrix':'Air', 'unit':'pg/m3', 'limit' : 100},
      {'location':'Egypt', 'compound': 'HCB', 'matrix':'Air', 'unit':'pg/m3', 'limit' : 30},
      {'location':'Burkina Faso', 'compound': 'PFOS', 'matrix':'Water', 'unit':'pg/l', 'limit' : 1000},
      {'location':'Ethiopia', 'compound': 'PFHxS', 'matrix':'Water', 'unit':'pg/l', 'limit' : 1000},
      {'location':'Brazil', 'compound': 'p,p-DDE', 'matrix':'Human blood', 'unit':'ng/l', 'limit' : 100000},
      {'location':'Romania', 'compound': 'p,p-DDE', 'matrix':'Human blood', 'unit':'ng/g fat', 'limit' : 3000},
      {'location':'Côte dIvoire', 'compound': 'Sum 6 PCBs', 'matrix':'Human milk', 'unit':'ng/g fat', 'limit' : 30},
      {'location':'Congo', 'compound': 'HCB', 'matrix':'Human milk', 'unit':'ng/g fat', 'limit' : 2},
      ]


    # Execution starts here by prompting the user to enter
    # the number of rows for each subset.
    print("Please enter how many rows do you want in each subset:")
    input = int(input())

    # Generate and write the data.
    for sample in samples:
          subset = generate_subset(input, sample)
          for set in subset:
                dataset.writerow(set)
