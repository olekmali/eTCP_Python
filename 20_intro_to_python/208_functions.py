# Functions
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print(b, end=', ')
        a, b = b, a+b
    print()

fib(5000)
# print( a )    # Note: a and b are local variables!
f = fib
f(10000)



def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return(result)

r = fib2(100000)
print( r[:10], "...", r[-1] )
print( str(r[:10])[:-1], "...", r[-1], "]" )



def fn_arguments_n_defaults(x=101, y=102, z=103):
    print( "x=", x, ", y=", y, ", z=", z )

fn_arguments_n_defaults()
fn_arguments_n_defaults(0)
fn_arguments_n_defaults(1, y=2)
fn_arguments_n_defaults(1, z=3)
fn_arguments_n_defaults(1, z=2, y=3)
fn_arguments_n_defaults(z=2, y=3)



def empty_function():
    pass

empty_function()
