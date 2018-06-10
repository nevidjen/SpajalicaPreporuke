import csv
import numpy as np
import pandas as pd
import random

cities = [];
userNames = [];
gender = ['male', 'female'];
age = range(18, 60);

# this is main array area
Users = [];
# end of array

# cities extraction
with open('cities.txt') as f:
    lines = f.readlines();

for city in lines:
    cities.append( ((city.split('\t'))[0]) );
# end of cities

# user name extraction
file = open('petfinder_shelters.csv');
reader = csv.reader(file, delimiter=',');

for row in reader:
    userNames.append( ((row[4]).split('@'))[0] );

file = open('schools_detailed.csv');
reader = csv.reader(file, delimiter=',');

for row in reader:
    userNames.append( ((row[11]).split('@'))[0] );

if 'email' in userNames:
    userNames.remove('email');
# end of user names

print len(cities);
# for city in cities:
#     print city;
print len(userNames);

for user in userNames:
    tempUserArray = [];
    tempUserArray.append(user);
    tempUserArray.append(random.choice(gender));
    tempUserArray.append(random.choice(age));
    tempUserArray.append(random.choice(cities));
    Users.append(pd.Series(tempUserArray, ['user_name', 'gender', 'age', 'city']));

UsersDF = pd.DataFrame(Users);

UsersDF.to_csv('./GeneratedData/Users.csv');
