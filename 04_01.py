def hello_world():
    print("Hello world")

def hello_user(name):
    print("Hello, " + name)

def get_name():
    name = input("Name:")
    print("Ahoj uzivateli: " + name)

hello_user("Michal")
hello_user("Olga")
hello_user("Martin")

hello_user(input("Name: "))
get_name()

hello_world()
hello_world()
hello_world()
hello_world()