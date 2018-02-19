days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print( days_of_the_week )

work_days = days_of_the_week
work_days.remove('saturday')
work_days.remove('sunday')
print( work_days )
print( days_of_the_week )
print("Something went wrong?\nLet's try again!")

days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print( days_of_the_week )

work_days = days_of_the_week[:]
work_days.remove('saturday')
work_days.remove('sunday')
print( work_days )
print( days_of_the_week )


print( days_of_the_week[1:6] )
print( days_of_the_week[:1] )
print( days_of_the_week[6:] )
