import csv
import json

data = []

# Append the json rows to the list "data"
with open('yelp_training_set_review.json') as f:
    for line in f:
        data.append(json.loads(line))

dataWriter = csv.writer(open('training_set_review.csv', 'wb'))
# Write headers to csv file
dataWriter.writerow(
    ['votes_funny', 'votes_useful', 'votes_cool', 'user_id', 'review_id', 'text', 'business_id',
     'stars', 'date', 'type'])

# Write the json data to the csv file.
for each in range(len(data)):
    # Variables are created intentionally for readability.
    # We can write the data directly to the csv file using writerow without creating variables to store
    # the values
    votes_funny_read = data[each]['votes']['funny']
    votes_useful_read = data[each]['votes']['useful']
    votes_cool_read = data[each]['votes']['cool']
    user_id_read = data[each]['user_id'].replace("-", '')
    review_id = data[each]['review_id'].replace("-", '')
    text_read = data[each]['text'].encode('utf-8').replace("-", '')
    business_id_read = data[each]['business_id']
    stars_read = data[each]['stars']
    date_read = data[each]['date']
    type_read = data[each]['type']
    dataWriter.writerow(
        [votes_funny_read, votes_useful_read, votes_cool_read, user_id_read, review_id, text_read,
         business_id_read, stars_read, date_read, type_read])
