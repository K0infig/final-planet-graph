import csv

dataset_1 =[]
dataset_2 =[]

planet_data = []

with open("dataset1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)


with open("dataset2_sorted.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)


header1 = dataset_1[0]
planet_data1 = dataset_1[1:]

header2 = dataset_2[0]
planet_data2 = dataset_2[1:]


header = header1+ header2

# array = ["a", "b", "c", "d"];
# (0,"a"), (1,"b"), (2, "c")
for index, data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index] + planet_data2[index])


with open("full_planet_graph.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(planet_data)
