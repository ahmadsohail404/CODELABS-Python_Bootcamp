# **args

def save_user(**user):
    print(user["name"])


save_user(id=1, name='Sohail', email='something@gmail.com')
# arbitrary keyword arguments instead of arbitrary arguments
# o/p -> {'id': 1, 'name': 'Sohail', 'email': 'something@gmail.com'} -> key : value
# the object we see here is called dictionary
