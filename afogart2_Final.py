#Get database 1
import csv

#Get columns from database 1
from collections import defaultdict

columns = defaultdict(list)
with open("afogart2_Final_Dataset1.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        for (k,v) in row.items():
            columns[k].append(v)

#Variables for columns
sensitive = columns["Sensitive"]
redness = columns["Redness"]
acne = columns["Acne"]
dry = columns["Dry"]
oily = columns["Oily"]
anti_aging = columns["Anti-Aging"]
scars = columns["Scars"]

#Get input from user for database 1
issue = input("What skin issue do you want to address? Sensitivity, Redness, Acne, Dryness, Oiliness, Aging, or Scarring: " + "\n")

if issue.lower() == "sensitivity":
    issue_results = list(filter(None, sensitive)) #Remove empty spaces from list using filter()

elif issue.lower() == "redness":
    issue_results = list(filter(None, redness))

elif issue.lower() == "acne":
    issue_results = list(filter(None, acne))

elif issue.lower() == "dryness":
    issue_results = list(filter(None, dry))

elif issue.lower() == "oiliness":
    issue_results = list(filter(None, oily))

elif issue.lower() == "aging":
    issue_results = list(filter(None, anti_aging))

elif issue.lower() == "scarring":
    issue_results = list(filter(None, scars))

else:
    print("Please type in an option as provided.")
    issue = input("\n" + "What skin issue do you want to address? Sensitivity, Redness, Acne, Dryness, Oiliness, Aging, or Scarring: " + "\n")

#Get columns from database 2
from collections import defaultdict

columns = defaultdict(list)
with open("afogart2_Final_Dataset2.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        for (c,a) in row.items():
            columns[c].append(a)

cleanser = columns["Cleanser"]
toner = columns["Toner"]
emulsion = columns["Emulsion"]
moisturizer = columns["Moisturizer"]
essence = columns["Essence"]
serum = columns["Serum"]
ampoule = columns["Ampoule"]
eye_cream = columns["Eye Cream"]
sunscreen = columns["Sunscreen"]

#Get input from user for database 2

product_type = input("\n" + "What type of product are you looking for? Cleanser, Toner, Emulsion, Moisturizer, Essence, Serum, Ampoule, Eye Cream, or Sunscreen: " + "\n")

if product_type.lower() == "cleanser":
    product_type_results = list(filter(None, cleanser))

elif product_type.lower() == "toner":
    product_type_results = list(filter(None, toner))

elif product_type.lower() == "emulsion":
    product_type_results = list(filter(None, emulsion))

elif product_type.lower() == "moisturizer":
    product_type_results = list(filter(None, moisturizer))

elif product_type.lower() == "essence":
    product_type_results = list(filter(None, essence))

elif product_type.lower() == "serum":
    product_type_results = list(filter(None, serum))

elif product_type.lower() == "ampoule":
    product_type_results = list(filter(None, ampoule))

elif product_type.lower() == "eye cream":
    product_type_results = list(filter(None, eye_cream))

elif product_type.lower() == "sunscreen":
    product_type_results = list(filter(None, sunscreen))

else:
    print("Please type in an option as provided.")
    product_type = input("\n" + "What type of product are you looking for? Cleanser, Toner, Emulsion, Moisturizer, Essence, Serum, Ampoule, Eye Cream, or Sunscreen: " + "\n")

#Combine user inputs to pair down output (product recommendations)

print("\n" + "Suggested products:" + "\n")

for i in issue_results:
    for p in product_type_results:
        if i == p:
            print(i)
