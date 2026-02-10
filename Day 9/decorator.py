def admin_only(func):
    def wrapper(username):
        if username == "admin":
            func(username)
        else:
            print("Access Denied")
    return wrapper


@admin_only
def dashboard(username):
    print("Welcome to the Admin Dashboard")



dashboard("admin")   
dashboard("user")    
