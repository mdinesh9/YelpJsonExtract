import csv
import json


data = []

# Append the json rows to the list "data"
with open('yelp_training_set_checkin.json') as f:
    for line in f:
        data.append(json.loads(line))

dataWriter = csv.writer(open('training_set_checkin.csv', 'wb'))
# Write headers to csv file
dataWriter.writerow(['checkin_info', 'type', 'business_id'])

# Write the json data to the csv file.
for each in range(len(data)):
    # Variables are created intentionally for readability.
    # We can write the data directly to the csv file using writerow without creating variables to store
    # the values
    checkin_info_read = data[each]['checkin_info']
    type_read = data[each]['type']
    business_id_read = data[each]['business_id'].encode('utf-8')
    dataWriter.writerow([checkin_info_read, type_read, business_id_read])
