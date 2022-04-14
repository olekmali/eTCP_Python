# Simple introduction of 1D lists
days_of_the_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

print( days_of_the_week )
print( sorted(days_of_the_week) )
print( sorted(days_of_the_week, reverse=True) )

print( "We have eTCP/IP lectures on " + days_of_the_week[1].title() + " and " + days_of_the_week[3].title() + "." )

days_of_the_week.remove('sunday')
print( "We work hard on " + str(days_of_the_week).title() + "." )

days_of_the_week.append('domingo')
print( "Here are the days of the week again: " + str(days_of_the_week).title() + "." )
