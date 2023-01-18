from pymongo import MongoClient

url = "mongodb+srv://student:admin@cluster0.bwvpaaq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

print('-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ')

docs = db.students.find({},{'_id':0})

for doc in docs:
    print(doc)

coll = db.students
myquery = {'student_id': 1007}
new_last = {'$set': {'last_name': 'Daleson'}}
coll.update_one(myquery, new_last)

print(' -- DISPLAYING STUDENT DOCUMENT 1007 -- ')
call = db.students.find_one({'student_id': 1007},{'_id':0})
print(call)


input(' End of program, press any key to exit... ')
if input:
    exit(0) 