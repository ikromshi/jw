import math
import os.path
import csv

file_name = input("Enter the path for the csv file to process: (i.e. customer_1.csv): ")

# customer transaction records  
customer_records = {}

def read_transactions():
  file =  open(file_name, "r")
  csv_reader = csv.reader(file)

  for row in csv_reader:
    # extracting customer id, transaction date and amount
    if not ''.join(row).strip():
      continue
    
    customer_id = row[0]
    transaction_date = row[1]
    transaction_sum = int(row[2])

    # extracting the month and the year from the give date
    date = transaction_date.split("/")
    month = date[0]
    year = date[2]

    # creating a key for the customer for a given month in a year
    customer_key = f"{customer_id}_{month}/{year}"
    
    # initializing a balance transaction for a customer - if there is none - for a given month
    if customer_key not in customer_records:
      customer_records[customer_key] = {
        "minimum_sum": math.inf, # initializing min_sum as infinity so as not to include the initial value when comparing transactions
        "maximum_sum": -math.inf, # initializing max_sum as negative infinity so as not to include the initial value when comparing transactions
        "ending_sum": 0
      }

    # calculating the updated balance after a transaction
    updated_balance = customer_records[customer_key]["ending_sum"] + transaction_sum

    # updating the minimum, maximum, and ending balances after the transaction
    customer_records[customer_key]["minimum_sum"] = updated_balance if updated_balance < customer_records[customer_key]["minimum_sum"] else customer_records[customer_key]["minimum_sum"]
    customer_records[customer_key]["maximum_sum"] = updated_balance if updated_balance > customer_records[customer_key]["maximum_sum"] else customer_records[customer_key]["maximum_sum"]
    customer_records[customer_key]["ending_sum"] = updated_balance


def write_transactions():
  file_name = "customer_records_output.csv"
  file = open(file_name, "w")
  csv_writer = csv.writer(file)

  # Writing the header column for the output file
  csv_writer.writerow(["CustomerID", "MM/YYYY", "MinBalance", "MaxBalance", "EndingBalance"])

  # extracting all the properties of customer_records and writing them in the output file
  for key in customer_records.keys():
    customer_id = key.split("_")[0]
    transaction_date = key.split("_")[1]
    min_sum = customer_records[key]["minimum_sum"]
    max_sum = customer_records[key]["maximum_sum"]
    ending_sum = customer_records[key]["ending_sum"]

    csv_writer.writerow([customer_id, transaction_date, min_sum, max_sum, ending_sum])

read_transactions()
write_transactions()
  
# customer_recods: {
#   customer_key: {
#     minimum_sum,c
#     maximum_sum,
#     ending_sum
#   } 
# }