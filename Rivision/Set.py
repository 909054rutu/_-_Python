#unorder
#print random

collection={1,1,2,3,2,2,"Hello","Hello"}
print(collection)

#empty set
s=set()
s.add(101)
s.add(101)
s.add(102)
s.add((1,2,3,4)) #tuple
s.remove(101)
#s.clear()
print(len(s))

collect={"coder","coding","programmer","python"}
print(collect.pop())


#set is mutable.............but..............set values is immutable


#union
set2={1,2,3}
set1={3,4,1}
print(set2.union(set1))

#intersection
set4={1,2,3}
set3={3,4,1}
print(set2.intersection(set1))


#Q1 store 10,10.0 in set
#1 store_s={10,"10.0"}
store_s={
    ("int",10),
    ("float",10.0)
    }
print(store_s)















