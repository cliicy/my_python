

people = {
    'Alice':{
        'phone':'2341',
        'addr':'Foo drive 23'
    },
    'Beth':{
        'phone':'9102',
        'addr':'Bar street 42'
    },
    'Cecil':{
        'phone':'3158',
        'addr':'Baz avenue 90'
    }
}

labels={
    'phone':'phone number',
    'addr':'address'
}

name = input('Name: ')
request = input('Request: ')

if request =='p':
    key ='phone'
if request =='a':
    key = 'addr'




if __name__ == '__main__':
    if name in people:
        print(name,"'s",labels[key],people[name][key])