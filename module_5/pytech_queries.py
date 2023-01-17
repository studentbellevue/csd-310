from pymongo import MongoClient
url = "mongodb+srv://student:admin@cluster0.bwvpaaq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

print('-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ')

docs = db.students.find({},{'_id':0})

for doc in docs:
    print(doc)
 

print(' -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY -- ')

doc = db.students.find_one({'student_id': 1007},{'_id':0})
print(doc)

input(' End of program, press any key to exit... ')
if input:
    exit(0) 