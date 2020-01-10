
import pymongo
#........................................................................
def login():
    print('Signin')
    user_name=input('User:')
    passcode=input('password')

    #database setting
    connection_string=pymongo.MongoClient() #connection_string
    database_value=connection_string.attendance #database value
    result=database_value.Users.find({'user_name':user_name,'password':passcode})
    for i in result:
        print(i)
        if i['user_name'] ==user_name:
            passcode=input('password')
            if i['password']==passcode:
                print('welcome '+user_name)
                break
        else:
            print('invalid user name')
            login()
    result=database_value.Users.find({'user_name':user_name},{'password':1})
    print("hey")
#..............................   
def signup():
    print('SignUp')
    user_name=input('new user name:')
    passcode=''
    #database setting
    connection_string=pymongo.MongoClient() #connection_string
    database_value=connection_string.attendance #database value
    result=database_value.Users.find({'user_name':user_name},{'user_name':1})
    for i in result:
        duplicate_user=0
        if i['user_name'] ==user_name:
            duplicate_user=1
            break
        else:
            
            passcode=input('password')
    if duplicate_user==1:
        print("user already exit")
        login()
    else:
        database_value.Users.insert_one({'user_name':user_name,'password':passcode})
        print("user created")
    

#......................................................................................

print('-----Attendance Management-----')
print('1.login\n2.new user\n3.exit')

#c={'1':'login()','2':'signup()'}
#result=c.get(choice,'login()')
condition=1
while condition:
    #user choice input
    choice=input('Enter choice')
    #selection
    if choice== '1':
        login() #fucntion call
        condition=0
    elif choice=='2':
        signup() #function call
        condition=0
    else:
        condition=1

        
#..............................    

