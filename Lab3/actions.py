import sqlite3


def print_all_students():
    con = sqlite3.connect("Lab3/university.db")
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM student ORDER BY lastName"):
        print(row)


def print_students_from_group():
    con = sqlite3.connect("Lab3/university.db")
    cur = con.cursor()
    print("Choose faculty. Available options:")
    for row in cur.execute("SELECT groupID, faculty FROM studentGroup"):
        print(row)
    groupID = input("groupID: ")
    rows = cur.execute("SELECT firstName, lastName, mail, groupID FROM student WHERE groupID = ? ORDER BY lastName", (groupID,))
    for row in rows:
        print(row)


def print_students_with_grade_higher_or_equal_to_grade():
    con = sqlite3.connect("Lab3/university.db")
    cur = con.cursor()
    print("Choose grade. Available options:")
    for row in cur.execute("SELECT * FROM grade"):
        print(row)

    gradeID = input("gradeID: ")
    rows = cur.execute("""
    SELECT S.albumNumber, S.firstName, S.lastName, 
    SU.name, SU.typeOfExam, G.grade 
    FROM studentGrade AS SG 
    JOIN student AS S 
    ON SG.albumNumber = S.albumNumber 
    JOIN grade AS G 
    ON SG.gradeID = G.gradeID 
    JOIN lecturer AS L 
    ON L.lecturerID = SG.lecturerID 
    JOIN subject AS SU 
    ON SU.subjectID = L.subjectID WHERE G.gradeID >= ?;
    """, (gradeID, ))
    for row in rows:
        print(row)


def print_lecturers_and_their_subjects():
    con = sqlite3.connect("Lab3/university.db")
    cur = con.cursor()
    rows = cur.execute("""
    SELECT L.scienceTitle, L.firstName, 
    L.lastName, L.mail, SU.name
    FROM lecturer AS L 
    JOIN subject AS SU 
    ON SU.subjectID = L.subjectID;
    """)
    for row in rows:
        print(row)


def print_departments():
    con = sqlite3.connect("Lab3/university.db")
    cur = con.cursor()
    rows = cur.execute("""
        SELECT D.name, S.groupID, S.faculty 
        FROM `department` AS D 
        JOIN studentGroup AS S 
        ON D.departmentID = S.departmentID 
        ORDER BY D.name;
        """)
    for row in rows:
        print(row)


def print_avg_grade():
    con = sqlite3.connect("Lab3/university.db")
    cur = con.cursor()
    rows = cur.execute("""
        SELECT S.albumNumber, S.firstName, 
        S.lastName, AVG(G.grade) 
        FROM student AS S 
        JOIN studentGrade AS SG 
        ON S.albumNumber = SG.albumNumber 
        JOIN grade AS G ON 
        G.gradeID = SG.gradeID 
        GROUP BY S.lastName;
        """)
    for row in rows:
        print(row)
