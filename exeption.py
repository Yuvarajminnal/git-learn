# excption Handling in python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("You can't divide by Zero")
except Exception:
    print("Something Went Wrong")
finally:
    print("Do some cleanup here")
