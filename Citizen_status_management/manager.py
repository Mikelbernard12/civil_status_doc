from account import *


class Manager(Staff):

    def __init__(self):
        super().__init__()

    def change_password(self):
        self.f_name += input('first name: ').title()
        self.l_name += input('last name: ').title()
        number_id = int(input("Id number: "))
        password = input("Old password: ")
        new_password = input('New password: ')
        my_cursor.execute(f"update manager set password = \"{new_password}\" "
                          f"where (Man_id =\"{number_id}\" and Password =\"{password}\") "
                          f"and (FirstName = \"{self.f_name}\" and LastName = \"{self.l_name}\")")
        my_db.commit()

    def login(self):
        try:
            id_num = int(input("Enter your identification number: "))
            password = input("Enter your password: ")
            my_cursor.execute(f"select * from manager where Man_id =\"{id_num}\"")
            result1 = my_cursor.fetchall()
            if password != result1[4]:
                print('invalid password,try again...')
                self.login()
            else:
                print('Welcome back ', result1[2] + " " + result1[3])
        except TypeError or ValueError:
            print("incorrect entry...")

    def manage_sec_rec(self):
        my_cursor.execute('select * from record')
        all_sec = my_cursor.fetchall()
        print(all_sec)

    def manage_sec(self):
        my_cursor.execute('select * from secretary')
        all_sec1 = my_cursor.fetchall()
        print(all_sec1)

