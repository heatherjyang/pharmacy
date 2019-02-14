import sys
input_dir = sys.argv[1]
ourput_dir = sys.argv[2]
file = open(input_dir,"r")
title = file.readline()
# maps drug_name to unique prescribers and costs
drug_map = {}
for i in file:
    id, prescriber_last_name, prescriber_first_name, drug_name, drug_cost = i.split(",")
    if drug_name not in drug_map:
        drug_map[drug_name] = [set(), 0]
    prescriber = prescriber_first_name + " " + prescriber_last_name
    drug_map[drug_name][0].add(prescriber)
    drug_map[drug_name][1] += int(drug_cost)
f = open(ourput_dir, "w")
f.write("drug_name,num_prescriber,total_cost\n")
for drug_name in sorted(drug_map, reverse=True):
    prescriber_set, total_cost = drug_map[drug_name]
    num_prescriber = len(prescriber_set)
    f.write(drug_name + "," + str(num_prescriber) + "," + str(total_cost) + "\n")
f.close()
