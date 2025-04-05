class MyClass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"_value is {self._value}")

    @property
    def ten_value(self):
        return self._value * 10

    @ten_value.setter
    def ten_value(self, new_value):
        # Update _value based on the new_value divided by 10
        self._value = new_value / 10


obj = MyClass(10)
# This will raise an error because we are trying to assign a value to a method call
# obj.show() = 40

# obj.ten_value= 40  # This will raise an error because ten_value is a property, not a setter method
print(obj.ten_value)

obj.ten_value = 40  # This will raise an error because ten_value is a property, not a setter method

print(obj.ten_value)  # This will raise an error because ten_value is a property, not a setter method
obj.show()  # This will raise an error because ten_value is a property, not a setter method