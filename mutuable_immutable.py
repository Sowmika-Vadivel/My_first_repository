items = [(10,20) , 71 , ['a','b'],{1,2,3},'python']
mutable = []
immutable = []
index = 0
while index < len(items):
    item = items[index]
    index+=1
    if type(item) in (list,set,dict):
        mutable.append(item)
    else:
        immutable.append(item)
print(f" {mutable}is a mutable datatype items present in the string")
print(f" {immutable} list is a immutable datatype items present in the string")


   