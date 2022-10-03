#print("hello")

import pandas as pd 
import numpy as np

#Group by Aggrigate

x=pd.DataFrame({'company':["google","google","yahoo","yahoo","Amazone","Amazone"],'person':['Akash','kajal','kiran','koyal','Anjali','Aman'],'sales_in_India':[100,140,540,670,240,551]})

print(x)


#print(x.groupby('company'))
#print(type(x.groupby('company')))
#z = (x.groupby('company'))
#print(z)

#print(z.std())
#print(z.min())
#print(z.mean())
#print(z.sum()) 
#print(z.count())
#print(z.describe())
#print(z.describe().transpose())  # It will change the position of data frame, row become column and column become row.
#print(z.describe().transpose()['Amazone'])



'''Create a DataFrame first column should be Product and group this data frame according 
to product,
second column should be company name and third column should be cost
apply all methods on this data frame. sum, mean,min,count, describe, change the 
position of rows columns and make any visualization'''




















'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : ["Good for health","sweet","yummy"]},index = [1,2,3], columns=["quality", "Fruits", "cost"])
x.to_csv('pooja.csv')'''

'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : ["Good for health","sweet","yummy"]},index = [1,2,3], columns=["quality", "Fruits", "cost"])
x.to_csv('Raj.csv')'''


'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : ["Good for health","sweet","yummy"]},index = [1,2,3], columns=["quality", "Fruits", "cost"])
x.to_csv('Hum_index_false.csv',index = False)'''


'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : ["Good for health","sweet","yummy"]},index = [1,2,3], columns=["quality", "Fruits", "cost"])
x.to_csv('shum_index_false.csv',index = False)'''


#MERGE, JOIN, CONCATENATE AND Append

'''x = pd.DataFrame({"Name":["Abc","xyz","Awd"], "Marks": [78,67,92]}, index = [1,2,3])
y = pd.DataFrame({"Name":["www","fff","ttt"], "Marks": [56,34,89]}, index = [4,5,6])
z = (x,y)
w = pd.concat(z)
print(w)'''


'''x = pd.DataFrame({"Name":["Abc","xyz","Awd"], "Marks": [78,67,92]}, index = [1,2,3])
y = pd.DataFrame({"Name":["www","fff","ttt"], "Marks": [56,34,89]}, index = [4,5,6])
z = pd.DataFrame({"Name":["Deepak","Kanika","Samridhi"], "Marks": [78,67,92]},index =[7,8,9])

r=(x,y,z)
w = pd.concat(r)
print(w)'''

'''x = pd.DataFrame({"Name":["Abc","xyz","Awd"], "Marks": [78,67,92]}, index = [1,2,3])
y = pd.DataFrame({"Name":["Raj","Deepak","Kanika"], "Marks": [56,34,89]}, index = [4,5,6])
z=x.append(y)
print(z)'''



'''x = pd.DataFrame({"Name":["Abc","xyz","Awd"], "Marks": [78,67,92]}, index = [1,2,3])
y = pd.DataFrame({"Name":["Raj","Deepak","Kanika"], "Marks": [56,34,89]}, index = [4,5,6])
z=x.append(y)
print(z)'''


#USE OF MERGE

'''x = pd.DataFrame({'Name_1':['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'],'Eng':[99,78,98,87,97,67]})
print(x)

y = pd.DataFrame({'Name_2':['Ashish','Ashish','Tajesvi','Omkar','Nikhil','Abhishek','Rahul','Ranjeet'],'Math':[99,78,98,87,97,67,75,98]})
print(y)



z=pd.merge(left=x, right=y, how='inner', left_on='Name_1',right_on='Name_2')
print(z)




z=pd.merge(left=x, right=y, how='inner', left_on='Name_1',right_on='Name_2', indicator = True)
print(z)'''

#INNER MERGE

'''z=pd.merge(left=x, right=y, how='inner', left_on='Name_1',right_on='Name_2', indicator = 'True')
print(z)

#OUTER MERGE


z=pd.merge(left=x, right=y, how='outer', left_on='Name_1',right_on='Name_2', indicator = True)
print(z)

#LEFT MERGE

z=pd.merge(left=x, right=y, how='left', left_on='Name_1',right_on='Name_2', indicator = True)
print(z)'''


#RIGHT MERGE

'''z=pd.merge(left=x, right=y, how='right', left_on='Name_1',right_on='Name_2', indicator = True)
print(z)'''



'''x = pd.DataFrame({'Name':['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'],'Eng':[99,78,98,87,97,67]})
print(x)
y = pd.DataFrame({'Name':['Ashish','Ashish','Tajesvi','Omkar','Nikhil','Abhishek','Rahul','Ranjeet'],'Math':[99,78,98,87,97,67,75,98]})
print(y)

z=pd.merge(left=x, right=y, how='inner', on='Name', indicator = True)
print(z)'''

'''z=pd.merge(left=x, right=y, how='outer', on='Name', indicator = True)
print(z)

z=pd.merge(left=x, right=y, how='left', on='Name', indicator = True)
print(z)'''

#String methods in pandas

#Converts strings in the Series/Index to lower case.

#Use of lower()
 	
'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x)
print(x.str.lower())


x = pd.Series(['ashish','arvind','sahil','deepak','nikhil','abhishek'])
print(x.str.title())'''


#Use of upper()

'''Converts strings in the Series/Index to upper case.'''

'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x)
print(x.str.upper())

len()

Computes String length().

x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x.str.len())
print(len(x))'''


# Use of split pattern method()
#split(' ')

#Splits each string with the given pattern.'''

'''x = pd.Series(['Ashish',   'Arvind',   'Sahil',   'Deepak','Nikhil','Abhishek'])
print(x.str.split())'''


#use of cat(sep=pattern)

'''cat(sep='__')

Concatenates the series/index elements with given separator.'''

'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])

print (x.str.cat(sep='**'))'''



# USE OF contains(',')

'''contains(pattern)

Returns a Boolean value True for each element if the substring contains 
in the element, else False.'''

'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print (x.str.contains('sh'))'''



#USE OF replace()
'''replace(a,b)

Replaces the value a with the value b.'''

'''x = pd.Series(['Ashish','Arvind','@Sahil','Deepak','Nikhil','Abhishek'])
print (x.str.replace('@','**'))
print (x.str.replace('A','B'))'''


#USE OF repeat(value)
'''repeat(value)

Repeats each element with specified number of times.'''

'''x = pd.Series(['Ashish ','Arvind ','Sahil ','Deepak','Nikhil','Abhishek'])
print(x.str.repeat(3))'''

#USE OF count() pattern method
'''count(pattern)

Returns count of appearance of pattern in each element.'''

'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x.str.count('e'))
print(x.str.count('A'))'''


#USE OF starts with(pattern)

'''startswith(pattern)

Returns true if the element in the Series/Index starts with the pattern.'''

'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x)
print(x.str. startswith ('A'))'''

#USE OF ends with(pattern)
'''endswith(pattern)

Returns true if the element in the Series/Index ends with the pattern.'''

'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x.str.endswith ('l'))'''


#USE OF find(pattern)
'''find(pattern)

Returns the first position of the first occurrence of the pattern.'''
#"-1" indicates that there no such pattern available in the element.

'''x = pd.Series(['Ashish','Arvind','SAhil','Deepak','NiAhil','Abhishek'])
print(x.str.find('A'))'''


#USE OF FINDALL METHOD
'''findall(pattern)

Returns a list of all occurrence of the pattern.'''

'''x = pd.Series(['Ashish','Arvind','SAhil','Deepak','NiAhil','Abhishek'])
print(x.str.findall('A'))'''


#USE OF SWAP CASE

'''swapcase

Swaps the case lower/upper.'''

'''x = pd.Series(['Ashish','Arvind','SAhil','Deepak','NiAhil','Abhishek'])
print(x.str.swapcase())'''

#isupper()

'''Checks whether all characters in each string in the Series/Index in upper case or not. 
Returns Boolean.'''
	
'''x = pd.Series(['Ashish','ARVIND','SAhil','DEEPAK','NiAhil','Abhishek'])
print(x.str.isupper())'''


#We can drop duplicates items from this data frame

'''x = pd.DataFrame({"Fruits":["apple","mango","banana","papaya","apple","mango"], "cost": [78,67,92,87,78,67]})
print(x)
x = x.drop_duplicates()
print(x)

x = pd.DataFrame({"Fruits":["apple","mango","banana","papaya","apple","mango"], "cost": [78,67,92,78,67]})
z = pd.DataFrame(x)
z = z.drop_duplicates()
print(z)'''

'''strip()

Helps strip whitespace(including newline) from each string in the Series/index from both the 
sides.'''

'''x = pd.Series(['   Ashish',   'Arvind',   'Sahil',   'Deepak','Nikhil','Abhishek'])
print(x)
print (x.str.strip())'''
















