from admin import Admin
from manager import Manager
from secretary import Secretary


administrator = Admin()
manager = Manager()
secretary = Secretary()

# here below I was just testing if it was functional
choice = input("enter choice: ").lower()
if choice == "a":
    administrator.create_admin()
elif choice == 'b':
    administrator.create_manager_acc()
elif choice == "c":
    administrator.create_secretary()
elif choice == 'd':
    manager.manage_sec()
elif choice == "f":
    secretary.record_user()
elif choice == 'u':
    manager.login()


