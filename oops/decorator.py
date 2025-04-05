def my_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Goodbye!")
    return wrapper  # <- This ensures the function is returned, not None

@my_decorator
def hello():
    print("Hello from the function!")

# hello()  # This should now work correctly

my_decorator(hello)  # This will also work, but is not necessary due to the @ syntax