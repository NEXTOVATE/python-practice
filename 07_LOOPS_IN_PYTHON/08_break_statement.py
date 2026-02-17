# #the break statement
for i in range(30):
    if(i == 15):
        break       #exit form loop
    print(i)        #display 0 to 14
    

l = ["aman",12,"sagar",34,0,122,"sagar",343]
for i in l:
    if i == "sagar":        #break on sagar and stop the loop
        break
    print(i)

# is break and continue statement work only in for loop?