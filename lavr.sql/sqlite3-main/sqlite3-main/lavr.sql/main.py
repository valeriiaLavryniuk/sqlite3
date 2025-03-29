import sqlite3


def create_table():
    conn = sqlite3.connect("data_base.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS questions (
         id INTEGER PRIMARY KEY,
         question TEXT,
         answer TEXT,
         wrong1 TEXT,
         wrong2 TEXT,
         wrong3 TEXT)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS quiz (
         id INTEGER PRIMARY KEY,
         name TEXT)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS quiz_content (
         id INTEGER PRIMARY KEY,
         quiz_id INTEGER,
         question_id INTEGER,
         FOREIGN KEY (quiz_id) REFERENCES quiz (id),
         FOREIGN KEY (question_id) REFERENCES question (id))''')
    
    conn.commit()
    conn.close()

def fill_questions(path_to_db):
    n = int(input("Введіть кількість запитань: "))
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()

    for i in range(n):
        question = input(f"Введіть питання під номером {i}: ")
        answer = input(f"Введіть правильну відповідь: ")
        wrong1 = input(f"Введіть першу неправильну відповідь: ")
        wrong2 = input(f"Введіть другу неправильну відповідь: ")
        wrong3 = input(f"Введіть третю неправильну відповідь: ")

        cur.execute('''INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)''', [question, answer, wrong1, wrong2, wrong3])
        conn.commit()
    conn.close()


def fill_quiz(path_to_db):
    n = int(input("Введіть кількість тем: "))
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()

    for i in range(n):
        name = input(f"Тема під номером {i}: ")
        cur.execute('''INSERT INTO quiz (name) VALUES (?)''', [name])
        conn.commit()
    conn.close()


def fill_content(path_to_db):
    n = int(input("Введіть кількість id: "))
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()

    for i in range(n):
        quiz_id = input(f"Id вікторини під номером {i+1}: ")
        question_id = input(f"Id питання під номером {i+1}: ")
        cur.execute('''INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)''', [quiz_id, question_id])
        conn.commit()
    conn.close()

create_table()
#fill_questions("data_base.db")
#fill_quiz("data_base.db")
# fill_content("data_base.db")

def print_questions(path_to_db):
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()
    i = 1
    for i in range(3,13):
        cur.execute("SELECT * FROM questions WHERE id == ?", [i])
        data = cur.fetchall()
        print(data)

        conn.commit()
    conn.close()

print_questions("data_base.db")