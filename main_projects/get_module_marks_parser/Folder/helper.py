import requests
import lxml.html
import sqlite3
from bs4 import BeautifulSoup as bs

def create_dbtable():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS MainT
        (   
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id VARCHAR(30),
            last_name VARCHAR(30),
            first_name VARCHAR(30),
            middle_name VARCHAR(30),
            password VARCHAR(30)
        )
        """)
    conn.commit()
    cursor.close()
    conn.close()

def paste_in_db(user_id, last_name, first_name, middle_name, password):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    create_dbtable()
    query = """INSERT INTO MainT (user_id, last_name, first_name, middle_name, password) VALUES (?, ?, ?, ?, ?)"""
    cursor.execute(query, (user_id, last_name, first_name, middle_name, password))
    conn.commit()

    cursor.execute("SELECT * FROM MainT")

    cursor.close()
    conn.close()

def get_by(teleid = False, dbid = False):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    if teleid:
        cursor.execute('SELECT * FROM MainT WHERE user_id = ?', (teleid, ))
    elif dbid:
        cursor.execute('SELECT * FROM MainT WHERE id = ?', (dbid, ))

    output = cursor.fetchall()
    cursor.close()
    conn.close()
    return output

def find(user_id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    create_dbtable()
    cursor.execute('SELECT * FROM MainT WHERE user_id = ?', (user_id, ))
    output = cursor.fetchall()
    cursor.close()
    conn.close()
    return output[0]

def get_all_(students=False, passwords=False, ids=False):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    query = ''

    create_dbtable()
    if students and passwords and ids:
        query = '''SELECT * FROM MainT'''
        cursor.execute(query)
        return cursor.fetchall()
    elif students:
        query = '''SELECT last_name, first_name, middle_name FROM MainT'''
    elif passwords:
        query = '''SELECT password FROM MainT'''
    elif ids:
        query = '''SELECT user_id FROM MainT'''

    cursor.execute(query)
    users = cursor.fetchall()

    cursor.close()
    conn.close()
    return [' '.join(k) for k in users]

def update_db(): # deletes table
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    query = """DROP TABLE MainT"""
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

students = get_all_(students=True)
passwords = get_all_(passwords=True)


USERS = {
    students[i]: passwords[i] for i in range(len(students))
}

url = 'http://studstat.dgu.ru/login.aspx?ReturnUrl=%2Fstat.aspx&cookieCheck=true'


def get_student(username):
    """
        Getting full name of student by first name and last name
    """
    for student in USERS.keys():
        if username.lower() in student.lower():
            return student
    else:
        return -1

def make_query(username, custom_password = False):
    """
        Sending query to page, where we wanna get marks of modules
    """

    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66",
    }

    url = 'http://studstat.dgu.ru/login.aspx?ReturnUrl=%2Fstat.aspx&cookieCheck=true'
    session = requests.Session()
    # print('1')
    data = session.get(url, headers=headers)
    # print('2')
    soup = bs(data.content, "lxml")

    last_name, first_name, middle_name = username.split()
    if custom_password:
        password = custom_password
    else:
        password = USERS[username]

    login_data = {
        "__EVENTTARGET": "EnterBtn",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": soup.find(id="__VIEWSTATE").get("value"),
        "__VIEWSTATEGENERATOR": soup.find(id="__VIEWSTATEGENERATOR").get("value"),
        "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION").get("value"),
        "LNameTxt": last_name,
        "FNameTxt": first_name,
        "PatrTxt": middle_name,
        "NZachKnTxt": password,
    }

    session.post(url, login_data, headers=headers)
    new_acc = session.get("http://studstat.dgu.ru/stat.aspx")

    return new_acc

def generate_response(username: str) -> dict:
    """
        # output dict --> Subject: (marks: list)
        фишка аргумента на 68 строчке, где нету зависимости в имени, фамилии или отчества. 
        просится просто что-то одно из (имени, фамилии или отчества) и затем это просто ищется
        Generates full dictionary with form <subject>:<his_marks>
    """
    resp = get_student(username)
    if resp != -1:
        account = make_query(resp)
    else:
        return {}

    soup = bs(account.text, "lxml")

    # Subject, marks: list
    formulate = {}

    try:
        found = soup.find("body").find("table", id="ContentPlaceHolder1_ModGrid").find_all("tr")
        found = found[1::]
    except AttributeError:
        return {}
    
    for current_subject in found:
        marks = []

        for mark in current_subject.find_all('td')[1::]:
            marks.append(mark.text.strip())


        this_subject = current_subject.find("td").text.strip()
        formulate.update({this_subject: marks})

    account.close()
    return formulate


def correct_show(data: dict):
    if not isinstance(data, dict):
        return data
    # translater dictionary into string view
    output_string = ""
    for key in data.keys():
        output_string += key + ": " + str(data[key]) + '\n'

    return output_string


if __name__ == '__main__':
    # my_id = '749909723'
    # print(make_query("Махмудов Омар Махмудович", "01420") == '')
    print(get_all_(True, True, True))
    # conn = sqlite3.connect('main.db')
    # cursor = conn.cursor()
    # update_db()
# 
# print(correct_show(generate_response("Азаев Якуб")))
# print(generate_response("Азаев Якуб"))
# print(USERS[get_student("Алиасхабов Ахмед")])
