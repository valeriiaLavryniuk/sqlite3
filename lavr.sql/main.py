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
    con.close()

def fill_questions(path_to_db):
    n - inp(input("Введіть кількість запитань: "))
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()

    for i in range(n):
        question = input(f"Введіть питання під номером {i}: ")
        answer = input(f"Введіть правильну відповідь: ")
        wrong1 = input(f"Введіть першу неправильну відповідь: ")
        wrong2 = input(f"Введіть другу неправильну відповідь: ")
        wrong3 = input(f"Введіть третю неправильну відповідь: ")

        cur.execute('''INSERT INTO questions (question, wrong_answer_1, wrong_answer_2, wrong_answer_3) VALUES (?,?,?,?,?)''', [question, wrong1, wrong2, wrong3])
        conn.commit()
    con.close()



