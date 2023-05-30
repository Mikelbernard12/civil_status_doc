from account import *
from admin import successful
import datetime as lk


today = lk.datetime.now()
add_secretary = ("INSERT INTO citizen "
                 "(Sec_id, FirstName, LastName, password, address, telephone, email, photo, date)"
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
add_record = ("INSERT INTO record "
              "(Sec_id, cit_id)"
              "VALUES (%s, %s)")


def insert_img(filepath):
    with open(filepath, "rb") as file:
        bin_data = file.read()
    return bin_data


def retrieve_data(id_number):
    sql_statement = "select photo from citizen where cit_id = '{0}'"
    my_cursor.execute(sql_statement.format(str(id_number)))
    result = my_cursor.fetchone()[0]
    store_filepath = "Images_output/img{0}.jpeg".format(str(id_number))
    with open(store_filepath, 'wb') as file:
        file.write(result)
        file.close()


class Secretary(Staff):

    def __init__(self):
        super().__init__()

    def change_password(self):
        self.f_name += input('first name: ').title()
        self.l_name += input('last name: ').title()
        number_id = int(input("Id number: "))
        password = input("Old password: ")
        new_password = input('New password: ')
        my_cursor.execute(f"update secretary set password = \"{new_password}\" "
                          f"where (Sec_id =\"{number_id}\" and Password =\"{password}\") "
                          f"and (FirstName = \"{self.f_name}\" and LastName = \"{self.l_name}\")")
        my_db.commit()

    def login(self):
        try:
            id_num = int(input("Enter your identification number: "))
            password = input("Enter your password: ")
            my_cursor.execute(f"select * from secretary where Sec_id =\"{id_num}\"")
            result1 = my_cursor.fetchall()
            if password != result1[5]:
                print('invalid password,try again')
                self.login()
            else:
                print('Welcome back ', result1[3] + " " + result1[4])
        except TypeError or ValueError:
            print("incorrect entry...")

    def record_user(self):
        # here the secretary saves the client's records in the database
        # a client records is saved in db.
        self.f_name += input('first name: ').title()
        self.l_name += input('last name: ').title()
        self.email += input('email: ')
        self.address += input('location: ').title()
        self.telephone = int(input('contact: '))
        self.password += input("password: ")
        sec_number = int(input("secretary id number: "))
        img = insert_img(input('Filepath: '))
        data_secretary = (sec_number, self.f_name, self.l_name, self.email, self.address,
                          self.telephone, self.password, img, today)
        my_cursor.execute(add_secretary, data_secretary)
        addd = my_cursor.lastrowid
        data_records = (sec_number, addd)
        my_cursor.execute(add_record, data_records)
        successful(self.f_name, self.l_name, addd, self.password, self.address, self.email, self.telephone)
        my_db.commit()

    def get_data(self):
        number_id = int(input("Id number: "))
        retrieve_data(number_id)
