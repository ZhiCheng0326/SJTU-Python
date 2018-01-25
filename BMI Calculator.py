# -*- coding: utf-8 -*-
# 12

def main():
    
        height, weight = input("请输入身高(meter), 体重(kg):")
        
        a = weight / height ** 2
        
        print "Your BMI is %0.2f" % (a)
    
        if a < 19:
            print "轻体重"
        elif a < 25:
            print "健康体重"
        elif a < 28:
            print "超重"
        else:
            print "肥胖"

main()
