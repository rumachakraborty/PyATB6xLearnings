def add_security(func):
    def wrapper():
        print("1.before the function called")
        print("2.helmet,dashcash,gloves,knee guard")
        func()
        print("3.after the function called")
        print("4.secure driving,leave all items")
    return wrapper()
@add_security
def drive_ola_scoter():
    print("driving ola scoter")

@add_security
def drive_zip_scoter():
    print("driving zip scoter")

@add_security
def drive_namma_scoter():
        print("driving nammayatri scoter")
