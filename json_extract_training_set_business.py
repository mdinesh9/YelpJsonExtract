import csv
import json

data = []

# Append the json rows to the list "data"
with open('yelp_training_set_business.json') as f:
    for line in f:
        data.append(json.loads(line))

dataWriter = csv.writer(open('training_set_business.csv', 'wb'))
# Write headers to csv file
dataWriter.writerow(
    ['city', 'review_count', 'name', 'neighborhoods', 'type', 'business_id', 'full_address', 'state',
     'longitude', 'stars', 'latitude', 'open', 'categories'])

# Write the json data to the csv file.
for each in range(len(data)):
    city_read = data[each]['city'].encode('utf-8')
    review_count_read = data[each]['review_count']
    name_read = data[each]['name'].encode('utf-8')
    neighborhoods_read = data[each]['neighborhoods']
    type_read = data[each]['type'].encode('utf-8')
    business_id_read = data[each]['business_id']
    full_address_read = data[each]['full_address'].encode('utf-8')
    state_read = data[each]['state'].encode('utf-8')
    longitude_read = data[each]['longitude']
    stars_read = data[each]['stars']
    latitude_read = data[each]['latitude']
    open_read = data[each]['open']
    categories_read = data[each]['categories'][0:len(data[each]['categories'])]
    dataWriter.writerow(
        [city_read, review_count_read, name_read, neighborhoods_read, type_read, business_id_read,
         full_address_read, state_read, longitude_read, stars_read, latitude_read, open_read, categories_read])
