# Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.
key,item,dictionary=["key1","key2","key3","key4"],["Item1","item2","item3","item4"],{}
i,len=0,len(key)
while(i<len):
    k=key[i]
    dictionary[k]=item[i]
    i=i+1
print(dictionary)