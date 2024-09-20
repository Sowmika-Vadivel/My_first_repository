items = [(10,20) , 71 , ['a','b'],{1,2,3},'python']
mutable = []
immutable = []
index = 0
while index < index < len(items):
    item = items[index]
    if type(item) in (list,set,dict):
        mutable.append(item)
         print(f"{mutable} is a mutable datatype items present in the string")
    else:
        immutable.append(item)
        print(f"{immutable} is a immutable datatype items present in the string")

   