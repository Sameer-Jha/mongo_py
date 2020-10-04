#!/usr/bin/env python3
import pymongo

'''
    This is a pymongo python mongoDb driver program
'''

def init_db(db_name):
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    dbList = client.list_database_names()

    if db_name in dbList:
        mydb = client[db_name]
        cols = mydb.list_collection_names()
        if "user_data" in cols:
            col = mydb["user_data"]
    else:
        perm = input(f'Database {db_name} not found want to create ?(Y/n): ')
        if perm[0].lower() == 'y':
            mydb = client[db_name]
            col = mydb["user_data"]
        else:
            print('Aborting.....')
    return col


def add_single_user(collection, data):
    x = collection.insert_one(data)
    print(x.inserted_id)


def add_multi_user(collection, data):
    x = collection.insert_many(data)
    print(x.inserted_ids)


def find_user(collection, key):
    x = collection.find_one(key)
    print(x)


def delete_user(collection, key):
    collection.delete_one(key)


def update_user(collection, key, data):
    collection.update_one(key, data)


def driver(choice, col):
    ''' Driver Program '''
    if choice == '1':
        username = input('Enter Data\n----- ----\nusername: ')
        fullName = input('full name: ')
        password = input('password: ')
        age = int(input('age: '))
        data = {'username':username, 'password':password, 'age':age, 'fullname': fullName}
        add_single_user(col, data)

    elif choice == '2':
        n = int(input('No of entries: '))
        data = []
        for _ in range(n):
            username = input('Enter Data\n----- ----\nusername: ')
            fullName = input('full name: ')
            password = input('password: ')
            age = int(input('age: '))
            data.append({'username':username, 'password':password, 'age':age, 'fullname': fullName})
        add_multi_user(col,data)

    elif choice == '3':
        kv_legend = {1:'username', 2:'password', 3:'age', 4:'fullName'}
        key = kv_legend[int(input(
            '''
            val     key
            ---     ---
             1.      username
             2.      password
             3.      age
             4.      fullName
            '''
        ))]
        search_kwd = input(f'Search value for {key}: ')
        search_query = {key: search_kwd}
        find_user(col, search_query)

    elif choice == '4':
        kv_legend = {1:'username', 2:'password', 3:'age', 4:'fullName'}
        key = kv_legend[int(input(
            '''
            val     key
            ---     ---
             1.      username
             2.      password
             3.      age
             4.      fullName
            '''
        ))]
        delete_kwd = input(f'Search value for {key}: ')
        delete_query = {key: delete_kwd}
        delete_user(col, delete_query)

    elif choice == '5':
        kv_legend = {1:'username', 2:'password', 3:'age', 4:'fullName'}
        key = kv_legend[int(input(
            '''
            val     key
            ---     ---
             1.      username
             2.      password
             3.      age
             4.      fullName
            '''
        ))]
        update_kwd = input(f'Search value for {key}: ')
        update_query = {key: update_kwd}
        update_key = kv_legend[int(input(
            '''
            val     key
            ---     ---
             1.      username
             2.      password
             3.      age
             4.      fullName
            '''
        ))]
        update_data = input(f'Enter update data for {update_key}: ')
        update_user(col, update_query, update_data)

    elif choice == '0':
        x = col.find()
        for entry in x:
            print(entry)


def main():
    db_name = input('Enter DB_Name to operate: ')
    col = init_db(db_name)
    ip = [str(i) for i in range(0,6)]
    while(True):
        choice = input(f'''
           Enter opertaion code for {db_name}

            code    operation
            ----    ---------
             0.      Show data
             1.      Add User
             2.      Add multiple Users
             3.      Find user
             4.      Delete user
             5.      Update User

        --> ''')

        if choice in ip:
            driver(choice, col)
        else:
            print("Invalid Input")
            continue


if __name__ == '__main__':
    main()