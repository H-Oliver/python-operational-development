import time,os
user,passwd ="alex","abc123"
def auth(auth_type):
    #print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            #print("wrapper func:", *args,**kwargs)
            if auth_type == "local":
                username = input("username:").strip()
                password = input("password:").strip()

                if user == username and passwd ==password:
                    print("\033[32;1mUser has passwd authentication\033[0m")
                    res = func(*args,**kwargs)
                    print("----after authenticaion----")
                    return  res
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type == "ldap":
                print("还没有配置ldap")

        return wrapper
    return outer_wrapper

def index():
    print("welcome to index page")

@auth(auth_type="local") #home = auth()
def home():
    print("welcome to home page")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page")

index()
home()
bbs()