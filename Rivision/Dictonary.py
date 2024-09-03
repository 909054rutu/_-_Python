#dictionary
random={"color":"purple",
"diff_color":["pink","yellow","black"],#list
"f_name":("rose",22)} #tupple

print(random["color"])
random["color"]="sky_blue" #update
random["lap_name"]="hp" #add mutable
print(random)
        
null_dict={}
null_dict["No"]=22
print(null_dict)


#nested dect
student={
    "name":"om",
    "subject":{
        "math":99,
        "stat":98
        }
    }
print(student["subject"]["math"])

print(student.keys())

#type cast
print(list(student.keys()))

#method
print(len(list(student.keys())))

print(student.values())
print(list(student.values()))

#dict.items()

print(student.items())#tupe format
pairs=list(student.items())
print(pairs[0])

#methos

#like try catch finally after error program remining part will be execute
#print(student["name10"]) #error
print("BEFORE")
print(student.get("name10"))  #none op
print("AFTER")


#print(student.update({"college":"rbnb"}))
new_kv={"per":99,"name":"shresha"}
student.update(new_kv)
print(student)

#practice quetion
dict_n={}

x=int(input("enter1 sub marks"))
dict_n.update({"math":x})

x=int(input("enter 2 sub marks"))
dict_n.update({"python":x})

x=int(input("enter 3 sub marks"))
dict_n.update({"java":x})

print(dict_n)









