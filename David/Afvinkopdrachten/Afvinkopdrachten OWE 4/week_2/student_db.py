from wrappers import Db_Wrapper as DB_Wrapper
import json
from datetime import datetime

def handler(username, password, id):
    try:
        database = f'A{username}'
        print(f"username: {username}, password: {password}, id: {id}, database: {database}")
        db = DB_Wrapper(host="145.74.104.144", database=database, user=username, password=password)
        query = f"SELECT * FROM student WHERE student_nr = {id}"
        result = list(db.execute(query)[0])
        for i in range(len(result)):
            result[i] = entry(result[i])
        student = "{}"
        student = json.loads(student)
        student["student_nr"] = f'{result[0]}'
        student["name"] = f'{result[1]} {result[2]} {result[3]}'
        student["geb_datum"] = f"{result[4].strftime('%d - %m - %Y')}"
        student["woonplaats"] = f"{result[5]}"
        student["email"] = f"{result[6]}"
        student["telefoon"] = f"{result[7]}"
        query2 = f"SELECT klas_naam FROM klas WHERE klas_id = {result[8]}"
        klas = db.execute(query2)[0][0]
        print(klas)
        student["klas"] = f"{klas}"
        query3 = f"SELECT voornaam FROM docent WHERE slb_id = {result[9]}"
        slber = db.execute(query3)[0][0]
        student["slber"] = f"{slber}"
        return student
    except Exception as e:
        print(e)
        return "Error"


def entry(value):
    if value is None:
        value = "Onbekend"
    return value


