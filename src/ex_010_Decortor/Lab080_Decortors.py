def before_after_ui_test(func):
    def wrapper():
        print("1.before running code")
        print("Hello everyone")
        func()
        print("after running code")
        print("execution completed and bye")
    return wrapper()

@before_after_ui_test
def test_ui():
    print("Login to page")
