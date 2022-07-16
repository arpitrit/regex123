# tup = (1,2,3,4,'Hello World')
# print(tup)
# print(type(tup))
# print(tup[1:5])




# st = set([1,2,2,3,4])
# print(st)
# st = {1,2,3,3,4,5,6,8,7,7}
# print(st)
# type(st)
# print(type(st))
# bt = {4,5,6}
# print(st.union(bt))
# print(st.intersection(bt))
# print(len(bt))
# print(st.difference(bt))
# print(st.discard(3))
# print(st)



map = {
    'first_name' : 'Arpit', 
    'last_name' : 'Agarwal',
    'com' : 'Google'
}
print(map['first_name'])
print(map['last_name'])
# print(map['something']) # here we get key error
print(map.get('com'))
print(map.get('com','Not Found'))
map.update({'com' : 'Amazon'})
print('after updation:',map)
print(map.clear())
print(map)
