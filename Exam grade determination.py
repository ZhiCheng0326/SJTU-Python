# -*- coding: utf-8 -*-
def main():
    while True:
        x = input("u请输入分数(0~100): ")
        if x < 0:
            print "Must be bigger number"
        elif x < 60:
            print "E"
        elif x< 70:
            print "D"
        elif x < 80:
            print "C"
        elif x < 90:
            print "B"
        elif x <=100:
            print "A"
        else:
            print "Must be small number"
        
main()
