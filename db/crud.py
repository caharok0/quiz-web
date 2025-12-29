import sqlite3

DB_NAME = 'quizes.db'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

def close():
    global conn, cursor
    cursor.close()
    conn.close()

def create_tables():
    open()

    cursor.execute('''CREATE TABLE IF NOT EXISTS quiz (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR,
    description TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question VARCHAR,
    answer VARCHAR,
    wrong1 VARCHAR,
    wrong2 VARCHAR,
    wrong3 VARCHAR
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS quiz_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_id INTEGER,
    question_id INTEGER,
    FOREIGN KEY (quiz_id) REFERENCES quiz (id),
    FOREIGN KEY (question_id) REFERENCES questions (id)
    )''')

    conn.commit()
    close()

def add_quizes():
    open()

    quizes = [
        ("Винаходи", "Перевір, наскільки добре ти знаєш відкриття, що змінили світ — від колеса до ШІ."),
        ("Космос", "Заглибся у загадки планет, зірок і чорних дір. Факт чи фантастика — вирішуй сам."),
        ("Кіно", "Від класики до сучасних блокбастерів — перевір свої знання про кіно та акторів."),
        ("IT", "Тест для ґіків: мови програмування, стартапи, кібератаки й тренди технологій."),
        ("Міфи", "Древні боги, герої й монстри — дізнайся, наскільки добре ти знаєш міфологію."),
    ]

    cursor.executemany('''INSERT INTO quiz (title, description) VALUES (?, ?)''', quizes)
    conn.commit()
    close()

def add_questions():
    open()

    questions = [
            ("Хто винайшов електричну лампочку?", "Томас Едісон", "Нікола Тесла", "Олександр Белл", "Ісаак Ньютон"),
            ("Який винахід вважають найважливішим у розвитку транспорту?", "Колесо", "Двигун внутрішнього згоряння",
             "Кермо", "Гальма"),
            ("Хто створив перший телефон?", "Олександр Белл", "Грем Белл", "Томас Морзе", "Нікола Тесла"),
            ("Яка країна запустила перший штучний супутник Землі?", "СРСР", "США", "Китай", "Німеччина"),
            ("Хто винайшов Інтернет?", "Тім Бернерс-Лі", "Стів Джобс", "Білл Гейтс", "Марк Цукерберг"),

            ("Яка планета найбільша в Сонячній системі?", "Юпітер", "Сатурн", "Марс", "Уран"),
            ("Як називається наш супутник?", "Місяць", "Європа", "Фобос", "Іо"),
            ("Що таке чорна діра?", "Об'єкт, з якого не може втекти навіть світло", "Порожнеча у космосі", "Астероїд",
             "Зірка, що вибухнула"),
            ("Який космічний апарат першим висадив людину на Місяць?", "Apollo 11", "Voyager 1", "Sputnik 1", "Luna 2"),
            ("Хто був першим космонавтом?", "Юрій Гагарін", "Ніл Армстронг", "Алан Шепард", "Базз Олдрін"),

            ("Хто зняв фільм 'Початок' (Inception)?", "Крістофер Нолан", "Стівен Спілберг", "Джеймс Кемерон",
             "Рідлі Скотт"),
            ("У якому фільмі звучить фраза 'I’ll be back'?", "Термінатор", "Матриця", "Хижак", "Робокоп"),
            ("Який фільм отримав Оскар за найкращий фільм у 1998 році?", "Титанік", "Форрест Гамп", "Матриця",
             "Гладіатор"),
            ("Як звали головного героя у 'Матриці'?", "Нео", "Морфеус", "Трініті", "Сміт"),
            ("Який мультфільм студії Pixar був першим?", "Історія іграшок", "У пошуках Немо", "Корпорація монстрів",
             "Вгору"),

            ("Хто створив мову Python?", "Гвідо ван Россум", "Денніс Річі", "Джеймс Гослінг", "Лінус Торвальдс"),
            ("Який протокол використовується для передачі вебсторінок?", "HTTP", "FTP", "SMTP", "SSH"),
            ("Що означає HTML?", "HyperText Markup Language", "HighText Machine Language",
             "HyperTransfer Main Language", "Hyper Tool Multi Language"),
            ("Яка компанія створила операційну систему Android?", "Google", "Microsoft", "Apple", "Samsung"),
            ("Який фреймворк використовують для Python веб-розробки?", "Django", "React", "Laravel", "Spring"),

            ("Хто був богом грому в грецькій міфології?", "Зевс", "Аполлон", "Посейдон", "Арес"),
            ("Як звали героя, що переміг Мінотавра?", "Тесей", "Персей", "Одіссей", "Ахілл"),
            ("Яка річка відділяла світ живих від мертвих у міфах?", "Стікс", "Лета", "Ахерон", "Флегетон"),
            ("У якому місті стояв Троянський кінь?", "Троя", "Афіни", "Спарта", "Рим"),
            ("Хто був богом війни у Римі?", "Марс", "Юпітер", "Меркурій", "Нептун"),
    ]


    cursor.executemany('''INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES (?, ?, ?, ?, ?)''',
                       questions)
    conn.commit()
    close()

def add_links():
    open()
    cursor.execute("PRAGMA foreign_keys=on")
    action = input("Додати звʼязок? (y/n)")
    while action != "n":
        quiz_id = int(input("Введіть номер вікторини"))
        question_id = int(input("Введіть номер запитання"))
        cursor.execute("""INSERT INTO quiz_questions (quiz_id, question_id) VALUES (?, ?)""", [quiz_id, question_id])
        conn.commit()
        action = input("Додати звʼязок? (y/n)")
    close()

def get_quizes():
    open()
    cursor.execute("SELECT * FROM quiz")
    quizes = cursor.fetchall()
    close()
    return quizes

def get_question_after(quiz_id=1, question_id=0):
    '''Повертає наступне питання до вибраної вікторини'''
    open()
    cursor.execute("""SELECT questions.id, questions.question, questions.answer, questions.wrong1, questions.wrong2, questions.wrong3
                   FROM questions, quiz_questions
                   WHERE quiz_questions.quiz_id = ? AND
                   quiz_questions.question_id > ? AND
                   quiz_questions.question_id = questions.id
                   ORDER BY quiz_questions.id""", (quiz_id, question_id))
    
    question = cursor.fetchone()
    close()
    return question

def check_right_answer(question_id, selected_answer):
    open()
    cursor.execute('''SELECT answer FROM questions WHERE id = ?''', [question_id])
    right_answer = cursor.fetchone()[0]
    close()
    if selected_answer == right_answer:
        return True
    else:
        return False

def create_quiz_db(title, description):
    open()
    cursor.execute('INSERT INTO quiz (title, description) VALUES (?, ?)', [title, description])
    conn.commit()
    close()

def main():
    # create_tables()
    # add_quizes()
    # add_questions()
    add_links()














