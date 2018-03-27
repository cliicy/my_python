import shelve
import pprint

def enter_command():
    cmd=input('Enter command(? for help): ')
    cmd=cmd.strip().lower()
    return cmd

def store_person(db):
    pid=input('Enter unique ID number: ')
    person={}
    person['name']=input('Enter name: ')
    person['age']=input('Enter age: ')
    person['phone']=input('Enter phone number: ')
    db[pid]=person


def lookup_person(db):
    pid=input('Enter ID number: ')
    field=input('what would you like to know? (name,age,phone) ')
    field=field.strip().lower()
    print(field.capitalize()+':', db[pid][field])

def print_help():
    print('The avaiable commands are:')
    print('store : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quit : Save changes and exit')
    print('? : Prints this message')


def main():
    database=shelve.open('database\Mydabase.bat')
    for item in database.items():
        print(item)
    try:
        while True:
            cmd=enter_command()
            if cmd=='store':
                store_person(database)
            elif cmd=='lookup':
                lookup_person(database)
            elif cmd=='?':
                print_help()
            elif cmd=='quit':
                return
    finally:
        database.close()


if __name__ == '__main__':
    main()



