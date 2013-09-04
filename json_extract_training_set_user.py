import csv
import json

data = []

# Append the json rows to the list "data"
with open('yelp_training_set_user.json') as f:
    for line in f:
        data.append(json.loads(line))

dataWriter = csv.writer(open('training_set_user.csv', 'wb'))
# Write headers to csv file
dataWriter.writerow(
    ['votes_funny', 'votes_useful', 'votes_cool', 'review_count', 'name', 'average_stars',
     'user_id', 'type'])

# Write the json data to the csv file.
for each in range(len(data)):
    # Variables are created intentionally for readability.
    # We can write the data directly to the csv file using writerow without creating variables to store
    # the values
    votes_funny_read = data[each]['votes']['funny']
    votes_useful_read = data[each]['votes']['useful']
    votes_cool_read = data[each]['votes']['cool']
    review_count_read = data[each]['review_count']
    name_read = data[each]['name'].encode('utf-8')
    average_stars_read = data[each]['average_stars']
    user_id_read = data[each]['user_id'].encode('utf-8')
    type_read = data[each]['type'].encode('utf-8')
    dataWriter.writerow(
        [votes_funny_read, votes_useful_read, votes_cool_read, review_count_read,
         name_read, average_stars_read, user_id_read, type_read])
