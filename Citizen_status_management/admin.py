from __future__ import print_function
from account import *
import datetime as lk


today = lk.datetime.now()
my_cursor = my_db.cursor()


add_admin = ("INSERT INTO super_admin "
             "(FirstName, LastName, email, address, telephone, password, date)"
             "VALUES (%s, %s, %s, %s, %s, %s, %s)")
add_manager = ("INSERT INTO manager "
               "(Admin_id, FirstName, LastName, email, address, telephone, password)"
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
add_secretary = ("INSERT INTO secretary "
                 "(Man_id,FirstName, LastName, email, address, telephone, password)"
                 "VALUES (%s, %s, %s, %s, %s, %s, %s)")
add_manages = ("INSERT INTO manages"
               "(Admin_id, Man_id, date)"
               "VALUES (%s, %s, %s)")

add_supervising = ("INSERT INTO supervise"
                   "(Man_id,Sec_id,date)"
                   "VALUES (%s, %s, %s)"
                   )


def successful(f_name, l_name, counting, password, local, mail, tel):
    # success in creating a user account
    print('First Name: ' + f_name + ' ,Last Name: ' + l_name)
    print('Account Id: ' + str(counting) + '\n' + 'Password: ' + password)
    print('Location:' + local + '\n' 'Email: ' + mail + '\n' 'Contact: ' + str(tel))
    print('Please keep your credentials (Account Id) safe.')


class Admin(Staff):

    def __init__(self):
        super().__init__()

    def create_admin(self):
        try:
            # creating the admin account in the system
            self.f_name += input('first name: ').title()
            self.l_name += input('last name: ').title()
            self.email += input('email: ')
            self.address += input('location: ').title()
            self.telephone = int(input('contact: '))
            self.password += input("input your password: ")
            data_admin = (self.f_name, self.l_name, self.email, self.address, self.telephone, self.password,
                          today)
            my_cursor.execute(add_admin, data_admin)
            ad = my_cursor.lastrowid
            successful(self.f_name, self.l_name, ad, self.password, self.address, self.email, self.telephone)
            my_db.commit()
            print(my_cursor.rowcount, "row updated successfully")
        except TypeError or ValueError:
            my_db.rollback()

    def create_manager_acc(self):
        try:
            # creating the manager account in the system
            self.f_name += input('first name: ').title()
            self.l_name += input('last name: ').title()
            self.email += input('email: ')
            self.address += input('location: ').title()
            self.telephone = int(input('contact: '))
            self.password += input("password: ")
            admin_number = int(input("Admin id number:"))
            data_manager = (admin_number, self.f_name, self.l_name, self.email, self.address, self.telephone,
                            self.password)
            my_cursor.execute(add_manager, data_manager)
            add = my_cursor.lastrowid
            data_manages = (admin_number, add, today)
            my_cursor.execute(add_manages, data_manages)
            successful(self.f_name, self.l_name, add, self.password, self.address, self.email, self.telephone)
            my_db.commit()
            print(my_cursor.rowcount, "row updated successfully")
        except ValueError or TypeError:
            my_db.rollback()

    def create_secretary(self):
        try:
            # creating the secretary account in the system
            self.f_name += input('first name: ').title()
            self.l_name += input('last name: ').title()
            self.email += input('email: ')
            self.address += input('location: ').title()
            self.telephone = int(input('contact: '))
            self.password += input("password: ")
            manager_number = int(input("manager id number: "))
            data_secretary = (manager_number, self.f_name, self.l_name, self.email, self.address,
                              self.telephone, self.password)
            my_cursor.execute(add_secretary, data_secretary)
            addd = my_cursor.lastrowid
            data_supervise = (manager_number, addd, today)
            my_cursor.execute(add_supervising, data_supervise)
            successful(self.f_name, self.l_name, addd, self.password, self.address, self.email, self.telephone)
            my_db.commit()
            print(my_cursor.rowcount, "row updated successfully")
        except TypeError or ValueError:
            my_db.rollback()

    def delete_secretary(self):
        try:
            # deleting a secretary from the system
            self.f_name += input('first name: ').title()
            self.l_name += input('last name: ').title()
            number_id = int(input("secretary id number: "))
            del_secretary = (f"Delete from secretary where (Sec_id = \"{number_id}\") and "
                             f"(firstName = \"{self.f_name}\" and lastName = \"{self.l_name}\")")
            my_cursor.execute(del_secretary)
            my_db.commit()
            print(my_cursor.rowcount, "row deleted successfully")
        except ValueError or TypeError:
            my_db.rollback()

    def delete_manager(self):
        try:
            # deleting a manager from the system
            self.f_name += input('first name: ').title()
            self.l_name += input('last name: ').title()
            number_id = int(input("manager id number: "))
            del_manager = (f" Delete from manager where (Man_id = \"{number_id}\") and "
                           f"(firstName = \"{self.f_name}\" and lastName = \"{self.l_name}\")")
            my_cursor.execute(del_manager)
            my_db.commit()
            print(my_cursor.rowcount, "row deleted successfully")
        except ValueError or TypeError:
            my_db.rollback()

    def login(self):
        try:
            id_num = int(input("Enter your identification number: "))
            password = input("Enter your password: ")
            my_cursor.execute(f"select * from Super_admin where Admin_id =\"{id_num}\"")
            result1 = my_cursor.fetchall()
            if password != result1[3]:
                print('invalid password,try again')
                self.login()
            else:
                print('Welcome back ', result1[1] + " " + result1[2])
        except TypeError or ValueError:
            print("incorrect entry...")

    def supervise(self):
        my_cursor.execute('select * from supervise')
        all_sec1 = my_cursor.fetchall()
        print(all_sec1)
