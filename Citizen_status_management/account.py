import mysql.connector


my_db = mysql.connector.connect(
    host='localhost',
    user="root",
    passwd="michaelbernard12",
    database="citizen_management",
    auth_plugin='mysql_native_password'
)


my_cursor = my_db.cursor()


class Staff:

    def __init__(self):
        self.f_name = ''
        self.l_name = ''
        self.email = ''
        self.telephone = ''
        self.password = ''
        self.address = ''
