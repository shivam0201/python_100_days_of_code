# Dictionary
programming_dict={
    "name":"Shivam",
    "age":23,
    "location":"Kanpur"
}
print(programming_dict["age"])

# Adding new items
programming_dict["Program"]="Masters of Technology"
print(programming_dict)

empty_dict={}
programming_dict["location"]="Satna"

for key in programming_dict:
    print(key)
    print(programming_dict[key])

#----------------------------------------------------------------------------------------------------

grades={
    "shivam":84,
    "aditya":91,
    "mohit":85,
    "rahul":78,
    "ajay":70
}
result={}
for key in grades:
    if grades[key]>=91:
        result[key]="Outstanding"
    elif grades[key]>=81:
        result[key]="Exceds Expectation"
    elif grades[key]>=71:
        result[key]="Acceptable"
    else:
        result[key]="Fail"

print(result)

#----------------------------------------------------
# Complex data structures
"""
dict={
key:[list],
key2:{dict},
}
"""

travel_log={
    "France":["Paris","Lille",'Dijon'],
    "India":{"MP":"Satna","UP":"Kanpur"}
}
print(travel_log)
print(travel_log["France"][2])
print(travel_log["India"]["MP"])

# Dictionary in list
travel=[
    {
        "country":"India",
        "cities":["Delhi","Agra","Kolkata"],
        "visits":12
    },
    {
        "country":"Germany",
        "cities":["Berlin","Stuttgart","Hamburg"],
        "visits":4
    },
    {
        "country":"France",
        "cities":["Paris","Lille","Dijon"],
        "visits":8
    }
]
print(travel)
addition={}
addition["country"]="Russia"
addition["visits"]=3
addition["cities"]=["Moscow","Saint Petersburg"]

travel.append(addition)
print(travel)
