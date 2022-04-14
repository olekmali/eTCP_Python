# Error Handling

print("Input loop")
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except KeyboardInterrupt:
        print("Ctrl+C? No Way!  Try again...")
    except:
        print("Oops!  Unexpected error happened.  Try again...")
    finally:
        pass

print("Computation attempt")
try:
    if x<0:
        raise
    print( "1 / ", x, " = ", (1/x) )
except ZeroDivisionError:
    print("Oops!  That was division by zero.")
except:
    print("Oops!  Unexpected error happened.")
finally:
    print("Thank you")
