# Write a python program to merge two python dictionaries into one dictionary.
first_dict={101:"Azam",102:"Adil",103:"Shabbir",104:"Amir"}
second_dict={105:"iNeuron",106:"MysirG Education Services",107:"Python Development"}
for e in second_dict:
    key=e
    first_dict[key]=second_dict[e]
print(first_dict)