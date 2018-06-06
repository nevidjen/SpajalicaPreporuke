import csv

cities = [];
userNames = [];

# cities extraction
with open('cities.txt') as f:
    lines = f.readlines();

for city in lines:
    if (city.find('1') == -1 and city.find('2') == -1
        and city.find('3') == -1 and city.find('4') == -1
        and city.find('5') == -1 and city.find('6') == -1
        and city.find('7') == -1 and city.find('8') == -1
        and city.find('9') == -1 and city.find('0') == -1):
      cities.append( (city.split('\t'))[0] );

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
print len(userNames);
