

# crud
#append
lst = ("sai",1,True)
print(lst)
#list can be  any data type
lst : lst = []
lst.append("sai")
print(lst)

#insert

attendences = ["dhanunjai" ,"sundhar"]
attendences.insert(1,"sai")
print(attendences)

#read
#access or get from the list
print(attendences.index("dhanunjai"))

#count
attendences = ["dhanunjai" ,"sai","sundhar"]
print(attendences.count("sai"))


attendences = ["dhanunjai" ,"sai","sundhar"]
if print(attendences.count("sai")> 0):
    print(attendences)

#update
#by using index
attendences = ["dhanunjai" ,"sai","sundhar"]
attendences[1] = ["sundhar"]
print(attendences)

#extend
attendences = ["dhanunjai" ,"sai","sundhar"]
attendences1 = ["sundhar"]
attendences.extend(attendences1)
print(attendences)
print(attendences1)

#delete
#remove

b = ["dhanunjai" ,"sai","sundhar"]
b.remove("dhanunjai")
print(b)

#pop eith index
b = ["dhanunjai" ,"sai","sundhar"]
b.pop(1)
print(b)


#pop without index
b = ["dhanunjai" ,"sai","sundhar"]
b.pop()
b.pop()
b.pop()
print(b)

#clear

a = ["dhanunjai","sai","sundhar"]
print(a.clear())
print(type(a))
print(a)

#delete

a = ["dhanunjai","sai","sundhar"]
del a[1]
print(a)



a1 = input("enter a1 name:")
a2 = input("enter a2 name:")
a3 = input("enter a3 name:")

a.append(a1)
a.append(a2)
a.append(a3)
print(a)


#sort
lst = [1,2,6,5,8,66,99,52,1008]
lst.sort()
print(lst)

#reverse

lst = [1,2,6,5,8,66,99,52,1008]
lst.reverse()
print(lst)

#tuple
#implicit

tpl = (1,2,53,6)
print(type(tpl))


#explicit

tpl = ((1,2,53,6))
print(type(tpl))

#tuple  method

tpl = ((1,2,53,6,2,2,2,5,6,99,99))
print(tpl.count(2))
print(tpl.count(99))

#index


tpl =tuple((1,2,53,6,2,2,2,5,6,99,99))
print(tpl.index(5))
print(tpl.index(99))

#tuple convert to list

tpl =tuple((1,2,53,6,2,2,2,5,6,99,99))
lst = list(tpl)
print(lst)
print(type(lst))
