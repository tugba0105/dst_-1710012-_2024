thislist = ["apple","banana","cherry"]
print(thislist)

thislist1 = ["apple","banana","cherry","apple","cherry"]
print(thislist1)
print(len(thislist1))

list1 =["abc", 34, True, 40, "male", True, 46]
print(list1[1])
print("[2:5] =", list1[2:5])
print("[:4]= ", list1[:4])
print("[2:]=", list1[2:])

list1.append(3)

tuple1 = ("abc", 34, True, 40, "Male")
#tuple1.append(3)

list2 = [2,2,"hello"]
tuple2 = (2,2, "hello")
set1 = {2,3,"hello"}

print(set1)
set1.add("ola")
print(set1)

list3 = ["tugba","can","artificial intelligente"]
print(list3)

set2={2,2,2,3,4,5}
print(set2)

thisisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964",
}
print(thisisdict)
today= {
    "class": ["dst", "network", "programming"],
    "quantitiy-of-students": 14,
    "students-name": {"joao","pablo"}
}

print(today)

print(today.keys())
print(today["students-name"])


