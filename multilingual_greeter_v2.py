from typing import Dict

mode_options = {1: "Admin", 2: "User"}
admin_mode_options = {1: "Add language", 2: "Edit greeting"}
user_select_mode = input("Select mode " + str(mode_options))

if user_select_mode == 1:
    print("Admin Mode")
         admin_Operations()

else:
    print("User MOde")


def admin_Operations():
    user_inp = input("Language Change options " + admin_mode_options)
    if user_inp == 1:
     add_languages()
    elif user_inp == 2:
        edit_greetings()


def users_Operations():


    def add_languages(*args):


def edit_greetings(*args):


 if __name__ == '__main__':

