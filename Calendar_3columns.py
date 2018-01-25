# -*- coding: utf-8 -*-
def main():		
    year = getYear()	
    w = firstDay(year)	
    printCalendar(year,w)

def getYear():
    print "本程序打印年历. "
    year = input("请输入年份(1900后):")
    return year
    
def firstDay(year):
    k = leapyears(year)
    n = (year-1900) * 365 + k
    return (n + 1) % 7
    
def printCalendar(year,w):
    print
    print "===== " + str(year) + " ===== "
    first = w
    for month in range(0,12,3):
        a = month
        b = month + 1
        c = month + 2
        heading(a,b,c)
        first = oneMonth(year,a,b,c,first)
		
def leapyears(year):
    count = 0
    for y in range(1900,year):
        if y%4 == 0 and (y%100 != 0 or y%400 == 0):
            count = count + 1
    return count
    
def heading(a,b,c):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    print "        %s                           %s                           %s       " % (months[a],months[b],months[c])
    print "Mon Tue Wed Thu Fri Sat Sun Mon Tue Wed Thu Fri Sat Sun Mon Tue Wed Thu Fri Sat Sun"
	
def oneMonth(year,a,b,c,first):
    d1 = days(year,a)
    d2 = days(year,b)
    d3 = days(year,c)
    frame1,frame2,frame3 = layout(first,d1,d2,d3)
    frame = build(frame1,frame2,frame3)
    printMonth(frame)
    return (first + d3) % 7
    
def days(y,m):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    d = month_days[m]
    if (m == 1) and (y%4 == 0 and(y%100 != 0 or y%400 == 0)): 
        d = d + 1
    return d
    
def layout(f,d1,d2,d3):
    frame1 = 42 * [""]
    frame2 = 42 * [""]
    frame3 = 42 * [""]
    if f == 0:
        f = 7
    j = f - 1
    for i in range(1,d1+1):
        frame1[j] = i
        j = j+1
    f = (f+d1)%7
    if f == 0:
        f = 7
    j = f - 1
    for e in range(1,d2+1):
        frame2[j] = e
        j = j+1
    f = (f+d2)%7
    if f == 0:
        f = 7
    j = f - 1
    for k in range(1,d3+1):
        frame3[j] = k
        j = j + 1
    return frame1,frame2,frame3
    
def build(f1,f2,f3):
    j = 0
    k = 0
    l = 0
    z = 126 *['']
    for i in range(0,126):
        if i % 21 <= 6:
            z[i] = f1[j]
            j += 1
        if i % 21 >6 and i%21 <= 13:
            z[i] = f2[k]
            k += 1
        if i % 21> 13 and i % 21 <= 20:
            z[i] = f3[l]
            l +=1
    return z
def printMonth(frame):
    for i in range(126):
	    print "%3s" % frame[i], 
	    if (i+1)%21 == 0:
		    print
main()
