def person(name, **data):
  
 print(name)

 for i, j in data.items():
  print(i,j)

person('salma', age=28, city = 'dhaka', mob=89765)
