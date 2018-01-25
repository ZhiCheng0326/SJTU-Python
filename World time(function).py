
def getTimeCity():
    hour = input("Current HOUR of Beijing Time:")
    minute = input("Current MINUTE of Beijing Time:")
    second = input("Current SECOND of Beijing Time:")
    city = raw_input("City:")
    return hour,minute,second,city
    
def timeConversion(city,hour,minute):
    city1 = ["London","Madrid","Paris","Istanbul","Moscow","Abu Dhabi","Dhaka","Bangkok","Buenos Aires","New York","Chicago","Los Angles"]
    diff_minus = [8, 7, 7, 5, 5, 4, 2, 1, 11, 12, 13, 15]
    city2 = ["Tokyo", "Melbourne"]
    diff_add = [1,3]
    minute_new = minute
    for i in range(len(city1)):
        if city == city1[i]:
            hour_new = hour - diff_minus[i]
    for j in range(len(city2)):
        if city == city2[j]:
            hour_new = hour + diff_add[j]
    if city == "New Delhi":
        hour_new = hour - 2
        minute_new = minute - 30
    return hour_new, minute_new

def increment(hour_new,minute_new):
    minute_new2 = minute_new
    if minute_new < 0:
        minute_new2 = minute_new + 60
        hour_new -= 1
    return hour_new,minute_new2

def determineDay(hour):
    if hour < 0:
        hour += 24
        print "It's one day before Beijing Day."

    elif hour > 24:
        hour -= 24
        print "It's one day after Beijing Day."
    return hour
                
def print_time(city,hour_new,minute_new,second):
    print "%s is %.2d:%.2d:%.2d now." % (city,hour_new,minute_new,second)

def main():
    hour,minute,second,city = getTimeCity()
    hour_new, minute_new = timeConversion(city,hour,minute)
    a,b = increment(hour_new,minute_new)
    c = determineDay(a)
    print_time(city,c,b,second)
    
main()
    
