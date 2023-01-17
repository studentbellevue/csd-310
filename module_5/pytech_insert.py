from pymongo import MongoClient
url = "mongodb+srv://student:admin@cluster0.bwvpaaq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(' -- INSERT STATEMENT -- ')
dale = {"student_id": 1007,
"first_name": "Dale ",
"last_name": "Dribble"
}
dale_student_id = str(db.students.insert_one(dale).inserted_id)
print(f'Inserted student record Dale Dribble into the students collection with document_id'+ dale_student_id)


bobby = {"student_id": 1008,
"first_name": "Bobby ",
"last_name": "Hill"
}
bobby_student_id = str(db.students.insert_one(bobby).inserted_id)
print(f'Inserted student record Bobby Hill into the students collection with document_id' + bobby_student_id)

hank = {"student_id": 1009,
"first_name": "Hank ",
"last_name": "Hill"
}
hank_student_id = str(db.students.insert_one(hank).inserted_id)
print(f'Inserted student record Hank Hill into the students collection with document_id' + hank_student_id)
 
input(' End of program, press any key to exit... ')
if input:
    exit(0) 
