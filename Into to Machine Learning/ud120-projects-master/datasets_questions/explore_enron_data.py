#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pprint

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


### # How many data points (people)?
print(len(enron_data))

### # For each person, how many features are available?
print(len(enron_data.itervalues().next().keys()))


### How many POIs are there in the E+F dataset? where data[person_name]["poi"]==1
count = 0
for key in enron_data:
	if enron_data[key]["poi"]==1:
		count += 1

print(count)

### How many POIs are there in total?
poi_reader = open('../final_project/poi_names.txt', 'r')
poi_reader.readline() # skip url
poi_reader.readline() # skip blank line

poi_count = 0
for poi in poi_reader:
	poi_count += 1

print(poi_count)

### What is the total value of the stock belonging to James Prentice?
print(enron_data["PRENTICE JAMES"]['total_stock_value'])

### How many email messages do we have from Wesley Colwell to persons of interest?
print(enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])

### Whats the value of stock options exercised by Jeffrey K Skilling?
print(enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])

### Among Lay, Skilling and Fastow, who took home the most money?
most_paid = ''
highest_payment = 0

for key in ('LAY KENNETH L', 'FASTOW ANDREW S', 'SKILLING JEFFREY K'):
	if enron_data[key]['total_payments'] > highest_payment:
		highest_payment = enron_data[key]['total_payments']
		most_paid = key

print(most_paid, highest_payment)


### How is it denoted when a feature doesn't have a well-defined value?
pprint.pprint(enron_data['SKILLING JEFFREY K'])


### How many folks have a quantified salary?
pprint.pprint(len(dict((key, value) for key, value in enron_data.items() if value["salary"] != 'NaN')))

### How many with a known email address?
pprint.pprint(len(dict((key, value) for key, value in enron_data.items() if value["email_address"] != 'NaN')))

### How many people have NaN for total_payments? What is the percentage of total?
no_total_payments = len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == 'NaN'))
print (float(no_total_payments)/len(enron_data) * 100)

### What percentage of POIs in the data have "NaN" for their total payments?
POIs = dict((key,value) for key, value in enron_data.items() if value['poi'] == True)
number_POIs = len(POIs)
no_total_payments = len(dict((key, value) for key, value in POIs.items() if value["total_payments"] == 'NaN'))
print (float(no_total_payments)/number_POIs * 100)

### If 10 POIs with NaN total_payments were added, what is the new number of people? 
### What is the new number of people with NaN total_payments?
print len(enron_data) + 10
print 10 + len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == 'NaN'))

### What is the new number of POIs?
print 10 + len(POIs)

### What percentage have NaN for their total_payments?
print float(10)/(10 + len(POIs))*100