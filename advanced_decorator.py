

## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        # use first positional argument instead of user variable, since it's the same thing.
        if args[0].is_logged_in == True:
            # if the user is logged in then call the function using their name to print it out
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Angela")
new_user.is_logged_in = True
create_blog_post(new_user)

new_user2 = User("Bobby")