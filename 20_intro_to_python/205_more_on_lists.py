# More on lists

# pointer/alias to existing list demonstrated
days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print( days_of_the_week )
work_days = days_of_the_week
work_days.remove('Saturday')
work_days.remove('Sunday')
print( work_days )
print( days_of_the_week )
print("Something went wrong?\nLet's try again!")


# list copied to a new list demonstrated
days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print( days_of_the_week )
work_days = days_of_the_week[:]
work_days.remove('Saturday')
work_days.remove('Sunday')
#work_days.remove('Sunday')    # removing non-existing element causes a runtime error
print( work_days )
print( days_of_the_week )

# accessing by index works the same as accessing characters in a string
print( days_of_the_week[1:6] )
print( days_of_the_week[:1] )
print( days_of_the_week[6:] )
print( days_of_the_week[-2:] )
