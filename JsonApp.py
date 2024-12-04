#Imported the class library.
import json

#Making the dictionery for the Python.
data1 = {

    'name':'Alina Ivanov',
    'age': 28,
    'city': 'New York',
    'interests': ['Traveling','Books','Fashion','Yoga','Photography','History'],
    'is_student': False

}

#Creating a Json and writing the python object contents to the Json.
with open('data1.json','w') as json_file:

#Use data.dump to write data to the file with an indentation of 4 for readability.
    json.dump(data1,json_file,indent=4)

print("Data has been written to data1.json")

#Read the JSON file.
with open('data1.json','r') as json_file:

#Load the data from the JSON file.
    loaded_data = json.load(json_file)

#Print a success message and the loaded data.
print("Successful able to read data1.json")
print(loaded_data)

#######
#Change the contents of the Json Dictionary.
loaded_data['age'] = 29
loaded_data['interests'].append('Movies')

#Rewrite the changes to the JSON file.
with open('data1.json','w') as json_file:

    json.dump(loaded_data, json_file, indent=4)

print('Data has been re-written to data1.json')

####
#Resave the altered JSON file.
