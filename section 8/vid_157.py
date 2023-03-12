# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True # changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if user1['valid'] is True:
            print(f"{user1['name']} is authenticated")
            fn(*args, **kwargs)
        else:
            print(f"{user1['name']} is NOT authenticated")
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
