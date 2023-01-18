from pymongo import MongoClient
url = "mongodb+srv://student:admin@cluster0.bwvpaaq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

#print contents
print('-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ')

docs = db.students.find({},{'_id':0})

for doc in docs:
    print(doc)

#insert new
print(' -- INSERT STATEMENTS -- ')
dave = {"student_id": 1010,
"first_name": "Dave ",
"last_name": "Bolion"
}
dave_student_id = str(db.students.insert_one(dave).inserted_id)
print(f'Inserted student record Dave Bolion into the students collection with document_id' + dave_student_id)

#ensure new has been added
print(' -- DISPLAYING STUDENT TEST DOC -- ')

doc = db.students.find_one({'student_id': 1010},{'_id':0})
print(doc)

# delete new
doc = db.students.delete_one({'student_id': 1010})


#print contents again
print('-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ')

docs = db.students.find({},{'_id':0})

for doc in docs:
    print(doc)

input(' End of program, press any key to exit... ')
if input:
    exit(0) 
