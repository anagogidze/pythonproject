import requests
import json

key = "4a3ca191393176ba69ed5aede11076ec"

name = str(input("Enter your name: "))
url = f"https://api.genderize.io?name={name}"
resp = requests.get(url)

print(resp)
print(resp.headers)
print(resp.status_code)
print(resp.text)

data = resp.json()
filename = 'gender_by_your_name.json'
with open(filename,'w') as json_file:
    json.dump(data,json_file, indent=4)

def your_gender(gender):
    if gender == "female":
        return f"Your gender is {gender}"
    else:
        return f"Your gender is {gender}"

gender_api = data.get("gender")
print(your_gender(gender_api))
with open(filename, 'r') as json_file:
    data_gender = json.load(json_file)
    print("Loaded data from file:")
    print(json.dumps(data_gender, indent=4))

#შევქმენი ბაზა,რომელშიც აისახება ის სახელი და გენდერი,რომელსაც შევიყვანთ.
import sqlite3
def gender_data():
    conn = sqlite3.connect("gender.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS gtable (
                    name TEXT,
                    gender TEXT
                )''')

    name = data.get("name")
    gender = data.get("gender")

    c.execute("INSERT INTO gtable VALUES (?,?)", (name, gender))

    conn.commit()
    conn.close()


gender_data()
