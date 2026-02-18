# After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.
# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.
# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.
# Write a code that gives out the total amount for different days(d).


days = int(input("Enter the number of days :"))
rent_p_day = 40

if days >= 7 :
    print(f"The rent id ${days*rent_p_day} but you got $50 off now your rent is ${(days*rent_p_day)-50}")
elif days >= 3:
    print(f"The rent id ${days*rent_p_day} but you got $20 off now your rent is ${(days*rent_p_day)-20}")
else:
    print(f"The rent id ${days*rent_p_day}")
