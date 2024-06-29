#creating a list
#my_list

my_list = [10,20,30,40,50]

my_list.append(60)

my_list.remove(30)

my_list[0] = (20)

print("updated list :" , my_list)



# cerating a dictionary

# my_dictionary


my_dict = {'Name ': 'harshali' , 'age' : 25  ,'City': 'Pune'}
 

#adding

my_dict ['Gender']='Female'

print(my_dict)

#Removing

del my_dict['age']

print(my_dict)

#Modifying

my_dict['City']='Solapur'

print(my_dict)

#Creat a set

my_set={1,2,3}

my_set.add(4)

print(my_set)

my_set.remove(2)

print(my_set)

my_set.discard(1)

print(my_set)

my_set.add(5)

print(my_set)

print('Final result :' ,my_list)

print('Final result :' , my_dict)

print('Final result :' ,my_set)