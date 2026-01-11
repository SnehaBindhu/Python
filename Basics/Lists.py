List1 = ["abc","sfdfc","abc","hghtq","dfgdfg"]
List1[1] = "efgh"
List1[3:] = ["yuih","tfgd"]
List1[4:] = ""
print(List1)
print(type(List1))
print (List1[0:2])
print (List1[-2])
appendList = List1.append("tefg") ## Append the list 
print(appendList)

insertList = List1.insert(1,"qwerty")  ## Insert an item into the list at mentioned location 
print(insertList)
List2 = ["asdf",234,"ghjkl",54.97,"True"]
print (List2[-3:])
print (List2[-3:-1])
print (len(List2))

List1.extend(List2)   ## Append elementsfrom another list into current list using extend(). Can also be used for tuples, sets and dictionaries 
print(List1)

## check if item existis in the list 
itemInList = ["asdf","ghjk",4528.12,"True"]
if "asdf" in itemInList :
    print ("Item found in the list ")
else :
    print("item not found in the list ")


List1.remove("abc") ## remove abc from list1 
print(List1)

List1.pop(4)   ## Remove index 4 element from the list
List1.pop()  ## removes last index element by default
print(List1)

List2.clear()  ## clears the whole list  
print(List2)

List2 = ["asdf",234,"ghjkl",54.97,"True"]   ## Loop through the list
for x in List2 :
    print(x)

for x in range (len(List2)):
    print(List2[x])

## List comprehension
fruits = ["apple", "banana","raspberries","blueberries","pineapple","cherry", "kiwi", "mango"]
newList =[x for x in fruits if "a" in x]
print(newList)

numbers = [15, 10, 25, 65, 83]
newNumberList = [x for x in numbers if x>=15]
print(newNumberList)

rangeList = [x for x in range(30)]
print(rangeList)

rangeList = list(range(0,30,10))
print(rangeList)

newFruitsList = [x.upper() for x in fruits]
print(newFruitsList)

newFruitsList = [x if x!="banana" else "orange" for x in fruits]
print(newFruitsList)

newFruitsList = ["fruits" for x in fruits]
print(newFruitsList)


## Sort Lists
print(fruits)
newFruitsList = sorted(fruits)  ### This updates the new list without affecting the original
print(newFruitsList)
newfruitsList = fruits.sort()   ### This sorts the original fruits list and does not update the newFruitsList
print(fruits)
fruits.sort(reverse = True)   ### This is for sorting in descending order
print(fruits)

fruits.reverse() ### reverse the entire list irrespestive of the sorting order
print(fruits)

### copy the lists
freshList = ["abcd","bcde","cdef","defg","efgh","fghi","ghij","hijk"]
copyFreshList = freshList.copy()
print(copyFreshList)

sliceOperatorList = freshList[:]   ### print whole list 
print(sliceOperatorList)

sliceOperatorList = freshList[2:] ### print all the elements after 3rd element
print(sliceOperatorList)

sliceOperatorList = freshList[:5]   ### print first 5 elements of the initial list 
print(sliceOperatorList)


### Join multiple Lists

List3 = List2 + List1
print(List3)

### Append

for x in List2:
    List1.append(x)
print(List1)

### extend()
List1.extend(List2)
print(List1)

