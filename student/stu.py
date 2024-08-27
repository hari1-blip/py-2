import sqlite3

def init_database():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   age INTEGER NOT NULL,
                   reg_no INTEGER NOT NULL,
                   major TEXT NOT NULL
                   )

''')
    conn.commit()
    conn.close()



def add_stu():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
         
    name = input('name of the student:')
    age = input('age of the student:')
    reg_no = input('register no of student:')
    major = input("student's major:")

    cursor.execute('INSERT INTO student(name, age, reg_no, major) VALUES (?,?,?,?) ',(name,age,reg_no,major))

    

    conn.commit()
    conn.close()
    print ('student added succesfully \n')


def view_all():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    input('Press enter to view the students')

    cursor.execute('SELECT * FROM student')
    items = cursor.fetchall()

    if items:
        for stu in items:
            print((f'id:{stu[0]},  name:{stu[1]},  age:{stu[2]},  reg_no{stu[3]},  major:{stu[4]}'))
    else:
        print('cannot fetch any student details, try adding one!\n')

    conn.close()


def view_specific():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    majors = input('enter the major:')

    cursor.execute('SELECT * FROM student WHERE major = (?)',(majors,))

    student = cursor.fetchall()
    if student:
        for stu in student:
            print((f'id:{stu[0]},  name:{stu[1]},  age:{stu[2]},  reg_no{stu[3]},  major:{stu[4]}'))
    else:
        print('cannot fetch any student details, try adding one!\n')

    conn.close()

def delete_stu():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    student_id = int(input('enter student id:'))

    cursor.execute("SELECT * FROM student WHERE id = ?",(student_id,))

    s_id = cursor.fetchone()
    if s_id:
        cursor.execute(" DELETE FROM student WHERE id = ?",(student_id,))
        conn.commit()
    else:
        print ('no student found try adding one!')

    conn.close()

    print('item deleted succesfully!')

def display_menu():
    print('STUDENTS DETAIL MANAGMENT SYSTEM:')
    print('1.Add student')
    print('2.View all student')
    print('3.View students by major')
    print('4.Delete student')

def main():
    while True:
        init_database()
        display_menu()
        choice = input('enter what you want to do (or) press 5 to exit ')

        if choice == '1':
            add_stu()

        elif choice == '2':
            view_all()

        elif choice == '3':
            view_specific()

        elif choice == '4':
            delete_stu()

        elif choice == '5':
            print('exiting.....')
            break

        else :
            print('enter any valid input:')

if __name__ == '__main__':
    main()


