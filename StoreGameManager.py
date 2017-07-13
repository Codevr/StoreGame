print("version 1.3")
print("Whats new:")
print("Added Super Dollars (SD)")
print("Started to use the Whats new screen")
print("-----------------Start--------------------")
import unittest
#aa1 = open("account1.txt","a")
#aa2 = open("account2.txt","a")
#aa3 = open("account3.txt","a")
#aa4 = open("account4.txt","a")
#ra1 = open("account1.txt","r")
#ra2 = open("account2.txt","r")
#ra3 = open("account3.txt","r")
#ra4 = open("account4.txt","r")
#ready = False
startOfBuy = 0
endOfBuy = 0

#while not ready:
#   newOrOldFile = input("continue? yes or no ")
#    if newOrOldFile == "yes" or newOrOldFile == "no":
#       readyb = False
#      while not readyb:
#         if newOrOldFile  == "no":
a1 = input("account 1 name: ")
a2 = input("account 2 name: ")
a3 = input("account 3 name: ")
a4 = input("account 4 name: ")
#        readyb = True
#       ready = True
#if newOrOldFile == "no":
#    wa1 = open("account1.txt","w")
#   wa2 = open("account2.txt","w")
#   wa3 = open("account3.txt","w")
#  wa4 = open("account4.txt","w")
# lines1 = [a1,"100"]
#lines2 = [a1,"100"]
#    lines3 = [a1,"100"]
#   lines4 = [a1,"100"]
a1m = 1000
a2m = 1000
a3m = 1000
a4m = 1000
a1sd = 3
a2sd = 3
a3sd = 3
a4sd = 3
d1 = 0
d2 = 0
d3 = 0
d4 = 0
#  wa1.writelines(lines1)
# wa2.writelines(lines2)
#    wa3.writelines(lines3)
#   wa4.writelines(lines4)
    
#if newOrOldFile == "yes":
#    a1 = ra1.readline()
#    a1m = ra1.readline(2)
#    a2 = ra2.readline()
#    a2m = ra2.readline(2)
#    a3 = ra3.readline()
#    a3m = ra3.readline(2)
#    a4 = ra4.readline()
#    a4m = ra4.readline(2)
while True:
    total = a1m + a2m + a3m + a4m + ((a1sd + a2sd + a3sd + a4sd) * 300)
    p1 = round((a1m + (a1sd * 300)) / total, 3)
    p2 = round((a2m + (a2sd * 300)) / total, 3)
    p3 = round((a3m + (a3sd * 300)) / total, 3)
    p4 = round((a4m + (a4sd * 300)) / total, 3)
    print("hello, " + str(a1) + " you have: $" + str(round(a1m,2)) + " " + " *" + str(a1sd) + str(p1*100) + "%")
    print("hello, " + str(a2) + " you have: $" + str(round(a2m,2)) + " " + " *" + str(a2sd) + str(p2*100) + "%")
    print("hello, " + str(a3) + " you have: $" + str(round(a3m,2)) + " " + " *" + str(a3sd) + str(p3*100) + "%")
    print("hello, " + str(a4) + " you have: $" + str(round(a4m,2)) + " " + " *" + str(a4sd) + str(p4*100) + "%")
    goOn= False
    choicelv1 = 0
    while not goOn:
        choicelv1 = input("Buy,Exit,Give ")
        if choicelv1 == "Buy" or choicelv1 == "Give" or choicelv1 == "Exit":
            if choicelv1 == "Exit":
                quit()
            goOn = True
    seller = 0
    monSeller = 0
    consumer = 0
    monConsumer = 0
    conDiscount = 0
    discount = 0
    buy = 0
    cost = 0
    if choicelv1 == "Buy":
        goOn = False
        while not goOn:
            seller = input("who is the seller? ")
            if seller == a1 or seller == a2 or seller == a3 or seller == a4:
                goOn = True
        goOn = False
        while not goOn:
            consumer = input("who is the customer? ")
            if consumer == a1 or consumer == a2 or consumer == a3 or consumer == a4:
                goOn = True
        goOn = False
        while not goOn:
            discount = input("store discount? ")
            if float(discount) >= 0 and float(discount) <= 100 - int(conDiscount):
                 
                goOn = True
        goOn = False
        while not goOn:
           buy = input("Items,Currency,Discount-Points ")
           if buy == "Items" or buy == "Discount-Points":
               goOn = True
        if buy == "Items" or buy == "Currency":
            currency = "unknown"
            goOn = False
            while not goOn:
                currency = input("What currency? SD (*) Money ($)")
                if currency == "SD" or currency == "Money":
                    if currency == "SD":
                        if consumer == a1:
                            conDiscount = d1
                            monConsumer = a1sd
                        elif consumer == a2:
                            conDiscount = d2
                            monConsumer = a2sd
                        elif consumer == a3:
                            conDiscount = d3
                            monConsumer = a3sd
                        elif consumer == a4:
                            conDiscount = d4
                            monConsumer = a4sd
                        if seller == a1:
                            monSeller = a1sd
                        elif seller == a2:
                            monSeller = a2sd
                        elif seller == a3:
                            monSeller = a3sd
                        elif seller == a4:
                            monSeller = a4sd
                    if currency == "Money":
                        if consumer == a1:
                            conDiscount = d1
                            monConsumer = a1m
                        elif consumer == a2:
                            conDiscount = d2
                            monConsumer = a2m
                        elif consumer == a3:
                            conDiscount = d3
                            monConsumer = a3m
                        elif consumer == a4:
                            conDiscount = d4
                            monConsumer = a4m
                        if seller == a1:
                            monSeller = a1m
                        elif seller == a2:
                            monSeller = a2m
                        elif seller == a3:
                            monSeller = a3m
                        elif seller == a4:
                            monSeller = a4m
                    goOn = True

            goOn = False
            while not goOn:
                cost = input("how much money or SD is the item? ")
                discount = float(discount) + float(conDiscount)
                if monConsumer-(float(cost)*((100-float(discount))*0.01)) >= 0:
                    print(consumer + " has enough money =]")
                    if currency == "Money":
                        print("it cost $" + str(float(cost)*((100-float(discount)))*0.01))
                        monConsumer = monConsumer-(float(cost)*((100-float(discount))*0.01))
                        monSeller = monSeller+(float(cost)*((100-float(discount))*0.01))
                        if consumer == a1:
                            a1m = monConsumer
                            d1 -= 1
                        elif consumer == a2:
                            a2m = monConsumer
                            d2 -= 1
                        elif consumer == a3:
                            a3m = monConsumer
                            d3 -= 1
                        elif consumer == a4:
                            a4m = monConsumer
                            d4 -= 1
                        if seller == a1:
                            a1m = monSeller
                        elif seller == a2:
                            a2m = monSeller
                        elif seller == a3:
                            a3m = monSeller
                        elif seller == a4:
                            a4m = monSeller
                    else:
                        print("it cost *" + str(float(cost)*((100-float(discount)))*0.01))
                        monConsumer = monConsumer-(float(cost)*((100-float(discount))*0.01))
                        monSeller = monSeller+(float(cost)*((100-float(discount))*0.01))
                        if consumer == a1:
                            a1sd = monConsumer
                            d1 -= 1
                        elif consumer == a2:
                            a2sd = monConsumer
                            d2 -= 1
                        elif consumer == a3:
                            a3sd = monConsumer
                            d3 -= 1
                        elif consumer == a4:
                            a4sd = monConsumer
                            d4 -= 1
                        if seller == a1:
                            a1sd = monSeller
                        elif seller == a2:
                            a2sd = monSeller
                        elif seller == a3:
                            a3sd = monSeller
                        elif seller == a4:
                            a4sd = monSeller
                    goOn = True
                else:
                    print(consumer + " dosent have enough money ")
                    goOn = True
        elif buy == "Discount-Points":
            goOn = False
            while not goOn:
                confirm = input("do you want to buy a discount point for $40? ")
                if confirm == "yes":
                    cost = 40
                    if monConsumer-(float(cost)*((100-float(discount))*0.01)) >= 0:
                        print(consumer + " has enough money =]")
                        print("it cost $" + str(float(cost)*((100-float(discount)))*0.01))
                        monConsumer = monConsumer-(float(cost)*((100-float(discount))*0.01))
                        monSeller = monSeller+(float(cost)*((100-float(discount))*0.01))
                        if consumer == a1:
                            a1m = monConsumer
                            d1 += 1
                        elif consumer == a2:
                            a2m = monConsumer
                            d2 += 1
                        elif consumer == a3:
                            a3m = monConsumer
                            d3 += 1
                        elif consumer == a4:
                            a4m = monConsumer
                            d4 += 1
                        if seller == a1:
                            a1m = monSeller
                        elif seller == a2:
                            a2m = monSeller
                        elif seller == a3:
                            a3m = monSeller
                        elif seller == a4:
                            a4m = monSeller
                        goOn = True
    if choicelv1 == "Give":
        goOn = False
        From = 0
        to = 0
        money = 0
        while not goOn:
            From = input("who is giving a gift? " + a1 + a2 + a3 + a4 + " or the bank ")
            to = input("who to? " + a1 + a2 + a3 + a4 + " or Everyone " )
            if From == "bank" or From == a1 or From == a2 or From == a3 or From == a4:
                if From == a1:
                    if not a1m - money >= 0:
                        print(a1 + " dosent have enough money =[")
                        goOn = True
                elif From == a2:
                    if not a2m - money >= 0:
                        print(a2 + " dosent have enough money =[")
                        goOn = True
                elif From == a3:
                    if not a3m - money >= 0:
                        print(a4 + " dosent have enough money =[")
                        goOn = True
                elif From == a4:
                    if not a4m - money >= 0:
                        print(a4 + " dosent have enough money =[")
                        goOn = True
                money = input ("how much? ")
                if to  == "Everyone" or to == a1 or to == a2 or to == a3 or to == a4:
                    if not From == "bank" or to == "Everyone" or From == "bank" and to == "Everyone":
                        if From == a1:
                            a1m -= float(money)
                        elif From == a2:
                            a2m -= float(money)
                        elif From == a3:
                            a3m -= float(money)
                        elif From == a4:
                            a4m -= float(money)
                        if to == a1:
                            a1m += float(money)
                        elif to == a2:
                            a2m += float(money)
                        elif to == a3:
                            a3m += float(money)
                        elif to == a4:
                            a4m += float(money)
                    if From == "bank":
                        if to == a1:
                            a1m += float(money)
                        elif to == a2:
                            a2m += float(money)
                        elif to == a3:
                            a3m += float(money)
                        elif to == a4:
                            a4m += float(money)
                    if to == "Everyone" and not From == "bank":
                        if From == a1:
                            a1m -= float(money)
                            money =float(float(money) / 3)
                            a2m += float(money)
                            a3m += float(money)
                            a4m += float(money)
                        if From == a2:
                            a2m -= float(money)
                            money =float(float(money) / 3)
                            a1m += float(money)
                            a3m += float(money)
                            a4m += float(money)
                        if From == a3:
                            a3m -= float(money)
                            money =float(float(money)  / 3)
                            a1m += float(money)
                            a2m += float(money)
                            a4m += float(money)
                        if From == a4:
                            a4m -= float(money)
                            money =float(float(money) / 3)
                            a1m += float(money)
                            a2m += float(money)
                            a3m += float(money)
                    if From == "bank" and to == "Everyone":
                        a1m += float(money)
                        a2m += float(money)
                        a3m += float(money)
                        a4m += float(money)
                    print(str(From) + " Gave " + str(to) + " " + str(money) + " dollars!")
                    goOn = True
                        
                        
                            
                        
                        
            
    

