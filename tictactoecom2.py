print("""                          ---------------TIC TAC TOE GAME---------------     
""")

import random

name=""

n=input("--> Enter your name= ")
name=name+n.upper()
print("----------------------------------------------------------------")
print("""RULES:
1. Your turn will be first and you will be "X".
2. Opponent will be "*".
3. If you enter the position which is already filled, your turn will be passed.""")
print("----------------------------------------------------------------")
per=input(f"--> Hi, {name} , Can we start the game? Type-Yes/No---")
print("----------------------------------------------------------------")

v=[]
onvalue=0
turn=1

#----------Displaying Tic Tac Toe Board---------->

def structure(xvalue,ovalue):
    pvalue=""
    if xvalue != 0 or ovalue != 0:
        for x in range(1,10):
            if x == xvalue or x == ovalue:
                if v[x] != "X" and v[x] != "*":
                    if xvalue != 0 and ovalue == 0:
                        pvalue=pvalue+"X"
                        v[x]=pvalue
                    else:
                        pvalue=pvalue+"*"
                        v[x]=pvalue
                else:
                    print("This space is full, try another one next time")

    else:
        y=1
        for x in range(10):
            v[x:y+1]=str(x)
            

    print()
    print("               "+f"{v[1]} | {v[2]} | {v[3]}")
    print("               "+"---------")
    print("               "+f"{v[4]} | {v[5]} | {v[6]}")
    print("               "+"---------")
    print("               "+f"{v[7]} | {v[8]} | {v[9]}")    

#----------Game Code ---------->

def startgame():
    global turn
    global name
    xvalue=0
    ovalue=0
    oposition=0
    emptypositionlist=[]
    xchoice=[]
    ochoice=[]
    
    while True:

#---Diplaying Board for the first time--->
        if turn == 1:
            structure(0,0)

        winarray=[[f"{v[1]}", f"{v[2]}", f"{v[3]}"], [f"{v[4]}", f"{v[5]}", f"{v[6]}" ], [f"{v[7]}", f"{v[8]}", f"{v[9]}" ], [f"{v[1]}", f"{v[4]}", f"{v[7]}" ], [f"{v[2]}", f"{v[5]}", f"{v[8]}"], [f"{v[3]}", f"{v[6]}", f"{v[9]}"], [f"{v[1]}", f"{v[5]}", f"{v[9]}"], [f"{v[3]}", f"{v[5]}", f"{v[7]}"]]
        
#---Taking input from User--->
        if turn % 2 != 0 :
            print()
            print(f"Your Turn {name}")
            print()
            xvalue=int(input("Enter The Position = "))
            if xvalue < 1 or xvalue > 10:
                print("INVALID INPUT")
                break
            xchoice.append(xvalue)
            structure(xvalue,0)

#---To check User has won or not
            if turn > 2:
                if v[1] == v[2] == v[3] or v[4] == v[5] == v[6] or v[7] == v[8] == v[9] or v[1] == v[4] == v[7] or v[2] == v[5] == v[8] or v[3] == v[6] == v[9] or v[1] == v[5] == v[9] or v[3] == v[5] == v[7]: 
                    print()
                    print("-------------------------GAME OVER-------------------------\n")
                    print("-------------------CONGRATULATIONS-------------------")
                    print(f"---------------YOU WON THE GAME, {name}---------------")
                    break 
        else:
#---Code to make the computer decide the correct position-->
            print()
            print("--Opponent's Turn--")
            print()

            lenxchoice=len(xchoice)-1
            lenochoice=len(ochoice)-1
            
            positionarray=[f"{v[1]}" , f"{v[2]}" , f"{v[3]}" , f"{v[4]}" , f"{v[5]}" , f"{v[6]}" , f"{v[7]}" , f"{v[8]}" , f"{v[9]}"]

            for x in range(9):
                if positionarray[x] != "X" and positionarray[x] != "*":
                    emptypositionlist.append(x+1)
                        

#---When turn == 2
            if turn == 2:
                if xvalue in (2,4,6,8):
                    ovalue = 5

                elif xvalue == 5:
                    choices=[9,7,3,1]
                    ovalue=random.choice(choices)
                    choices=[]

                elif xvalue == 1:
                    ovalue = 9

                elif xvalue == 3:
                    ovalue = 7

                elif xvalue == 7:
                    ovalue=3

                elif xvalue == 9:
                    ovalue = 1

                print("-Opponent choosed position-> ",ovalue)    
                print("----------------------------------------")

#---When turn == 4               
            if turn == 4:

                #---function for calculating the position for stoping user to win
                def xwinning():
                    losing=0
                    winarrayvaluesx=0
                    winarrayvaluesnotx=[]
                    winarrayvaluesnotx1=[]
                    winarrayvalues=[]    
                    for i in range(len(winarray)):
                        winarrayvalues.append(winarray[i])
                        if "*" not in winarrayvalues[0] and "X" in winarrayvalues[0]:
                            for x in range(1):
                                for y in range(3):
                                    if winarrayvalues[x][y] == "X":
                                        winarrayvaluesx += 1
                                    else:
                                        winarrayvaluesnotx.append(winarrayvalues[x][y])
                                
                                if winarrayvaluesx  == 2:
                                    losing += 1
                                    winarrayvaluesnotx1.append(winarrayvaluesnotx[0])

                                winarrayvaluesnotx=[]
                                winarrayvaluesx=0
                                winarrayvalues=[]       

                        winarrayvalues=[]

                    if len(winarrayvaluesnotx1) > 0:
                        if len(winarrayvaluesnotx1) == 1:
                                xwinningoposition = int(winarrayvaluesnotx1[0])
                        else:
                                xwinningoposition = int(random.choice(winarrayvaluesnotx1))

                    else:
                        xwinningoposition = 0

                    if losing > 0:
                        ovalue1= xwinningoposition
                        losing = 0
                        xwinningoposition = 0
                    else:
                        ovalue1=0

                    return ovalue1


                #---If X is not winning then,
                ovalue2 = xwinning()
                
                if ovalue2 != 0:
                    ovalue = ovalue2

                #---If X value was 5 in round 1
                elif ovalue2 == 0:
                    if xchoice[0] == 5:
                        for i in [1,3,7,9]:
                            if f"{v[i]}" == "*":
                                oposition += i

                        if oposition == 1:
                            ovalue = 3

                        elif oposition == 3:
                            ovalue = 1

                        elif oposition == 7:
                            ovalue = 9

                        elif oposition == 9:
                            ovalue = 7

                # if xvalue was [2,4,6,8] in round 1     
                    elif xchoice[0] in [2,4,6,8]:
                        if f"{v[2]}" == "X" and f"{v[8]}" == "X" or f"{v[4]}" == "X" and f"{v[6]}" == "X":
                            if f"{v[2]}" == "X" and f"{v[8]}" == "X":
                                choices = [1,4,7,3,6,9]
                                ovalue=int(random.choice(choices))
                                choices=[]

                            elif f"{v[4]}" == "X" and f"{v[6]}" == "X":
                                choices = [1,2,3,7,8,9]
                                ovalue=int(random.choice(choices))
                                choices=[]
                
                        else:

                            if xchoice[lenxchoice-1] == 2: 
                                if xchoice[lenxchoice] in [4,7]:
                                    ovalue = 1
                            
                                elif xchoice[lenxchoice] in [6,9]:
                                    ovalue = 3                 

                            if xchoice[lenxchoice-1] == 4: 
                                if xchoice[lenxchoice] in [2,3]:
                                    ovalue = 1
                            
                                elif xchoice[lenxchoice] in [8,9]:
                                    ovalue = 7

                            if xchoice[lenxchoice-1] == 6: 
                                if xchoice[lenxchoice] in [1,2]:
                                    ovalue = 3
                            
                                elif xchoice[lenxchoice] in [7,8]:
                                    ovalue = 9                                  

                            if xchoice[lenxchoice-1] == 8: 
                                if xchoice[lenxchoice] in [1,4]:
                                    ovalue = 7
                            
                                elif xchoice[lenxchoice] in [3,6]:
                                    ovalue = 9  

                # if xvalue was 1379 in round 1                               

                    elif xchoice[lenxchoice-1] in [1,3,7,9]:
                        if xchoice[lenxchoice] == 5:
                            if ochoice[lenochoice] == 1:
                                choices=[2,3,4,7]
                                ovalue=int(random.choice(choices))
                                choices=[]

                            elif ochoice[lenochoice] == 3:
                                choices=[1,2,6,9]
                                ovalue=int(random.choice(choices))
                                choices=[]

                            elif ochoice[lenochoice] == 7:
                                choices=[1,4,8,9]
                                ovalue=int(random.choice(choices))
                                choices=[]

                            elif ochoice[lenochoice] == 9:
                                choices=[3,6,7,8]
                                ovalue=int(random.choice(choices))
                                choices=[]

                        else:
                            ovalue = 5   

                ovalue2 = 0
                print("-Opponent choosed position-> ",ovalue)    
                print("----------------------------------------")


#---When turn == 6
#                
            if turn ==  6:

#---Function to check if computer is winning

                def owinning():
                    winning=0
                    winarrayvalueso=0
                    winarrayvaluesnoto=[]
                    winarrayvaluesnoto1=[]
                    winarrayvalues=[]    
                    for i in range(len(winarray)):
                        winarrayvalues.append(winarray[i])
                        if "X" not in winarrayvalues[0] and "*" in winarrayvalues[0]:
                            for x in range(1):
                                for y in range(3):
                                    if winarrayvalues[x][y] == "*":
                                        winarrayvalueso += 1
                                    else:
                                        winarrayvaluesnoto.append(winarrayvalues[x][y])
                                
                                if winarrayvalueso  == 2:
                                    winning += 1
                                    winarrayvaluesnoto1.append(winarrayvaluesnoto[0])

                                winarrayvaluesnoto=[]
                                winarrayvalueso=0
                                winarrayvalues=[]       

                        winarrayvalues=[]

                    if len(winarrayvaluesnoto1) > 0:
                        if len(winarrayvaluesnoto1) == 1:
                                owinningoposition = int(winarrayvaluesnoto1[0])
                        else:
                                owinningoposition = int(random.choice(winarrayvaluesnoto1))

                    else:
                        owinningoposition = 0

                    if winning > 0:
                        ovalue1= owinningoposition
                        winning = 0
                        owinningoposition = 0
                    else:
                        ovalue1=0

                    return ovalue1
                    

                ovalue2 = owinning()

                if ovalue2 != 0:
                    ovalue = ovalue2

                elif ovalue2 == 0:
                    ovalue3 = xwinning()

                    if ovalue3 != 0:
                        ovalue = ovalue3

                    else:

                        if xchoice[0] == 5:
                            if ochoice[0] == 1 and xchoice[lenxchoice] == 9:
                                if "X" not in [str(f"{v[2]}"),str(f"{v[3]}")]:
                                    ovalue=2

                                elif "X" not in [str(f"{v[4]}"),str(f"{v[7]}")]:
                                    ovalue=4

                            if ochoice[0] == 9 and xchoice[lenxchoice] == 1:
                                if "X" not in [str(f"{v[3]}"),str(f"{v[6]}")]:
                                    ovalue=6
 
                                elif "X" not in [str(f"{v[7]}"),str(f"{v[8]}")]:
                                    ovalue=8

                            if ochoice[0] == 3 and xchoice[lenxchoice] == 7:
                                if "X" not in [str(f"{v[1]}"),str(f"{v[2]}")]:
                                    ovalue=2

                                elif "X" not in [str(f"{v[6]}"),str(f"{v[9]}")]:
                                    ovalue=6

                            if ochoice[0] == 7 and xchoice[lenxchoice] == 3:
                                if "X" not in [str(f"{v[1]}"),str(f"{v[4]}")]:
                                    ovalue=4

                                elif "X" not in [str(f"{v[8]}"),str(f"{v[9]}")]:
                                    ovalue=8

                        elif xchoice[0] in [2,4,6,8]:
                            if ochoice[lenochoice] == 1 and xchoice[lenxchoice] == 9:
                                choices=[3,7]
                                ovalue=int(random.choice(choices))

                            if ochoice[lenochoice] == 3 and xchoice[lenxchoice] == 7:
                                choices=[1,9]
                                ovalue=int(random.choice(choices))

                            if ochoice[lenochoice] == 7 and xchoice[lenxchoice] == 3:
                                choices=[1,9]
                                ovalue=int(random.choice(choices))

                            if ochoice[lenochoice] == 9 and xchoice[lenxchoice] == 1:
                                choices=[3,7]
                                ovalue=int(random.choice(choices))

                        elif xchoice[0] in [1,3,7,9]:
                            if ochoice[lenochoice] == 5:
                                if ochoice[0] == 1:
                                    if xchoice[lenxchoice] in [2,4]:
                                        choices=[3,7]
                                        ovalue=int(random.choice(choices))
                                        choices=[]

                                if ochoice[0] == 9:
                                    if xchoice[lenxchoice] in [6,8]:
                                        choices=[3,7]
                                        ovalue=int(random.choice(choices))
                                        choices=[]

                                if ochoice[0] == 3:
                                    if xchoice[lenxchoice] in [2,6]:
                                        choices=[1,9]
                                        ovalue=int(random.choice(choices))
                                        choices=[]
                            
                                if ochoice[0] == 7:
                                    if xchoice[lenxchoice] in [4,8]:
                                        choices=[1,9]
                                        ovalue=int(random.choice(choices))
                                        choices=[]
                            
                            else:
                                ovalue = 5

                ovalue3 = 0
                print("-Opponent choosed position-> ",ovalue)    
                print("----------------------------------------")

#---When turn == 8
               
            if turn == 8:
                
                ovalue2 = owinning()

                if ovalue2 != 0:
                    ovalue = ovalue2

                elif ovalue2 == 0:
                    ovalue3 = xwinning()

                    if ovalue3 != 0:
                        ovalue = ovalue3

                    else: 
                        ovalue= int(random.choice(emptypositionlist))

                print("-Opponent choosed position-> ",ovalue)    
                print("----------------------------------------")

            emptypositionlist.clear()
            ochoice.append(ovalue)
            structure(0,ovalue)

#---To check Computer has won or not

            if turn > 2:
                if v[1] == v[2] == v[3] or v[4] == v[5] == v[6] or v[7] == v[8] == v[9] or v[1] == v[4] == v[7] or v[2] == v[5] == v[8] or v[3] == v[6] == v[9] or v[1] == v[5] == v[9] or v[3] == v[5] == v[7]: 
                    print()
                    print("-------------------------GAME OVER-------------------------\n")
                    print("--------------------OPPONENT WON THE GAME--------------------\n")
                    break 
                
                
        if turn == 9:
            print("-------------------------GAME OVER-------------------------\n")
            print("--------------- NO ONE WINS ---------------")
            print()
            break

        turn += 1

if per.lower() == "yes":
    startgame()

else:
    print()
    print(f"Nice to meet you {name}, See you next time!")
    print()

if turn == 9:
    while True:
        again=input(f"--> Would you like to play the game again {name}? Type Yes/No---")
        print()
        if again.lower() == "yes":
            turn = 1
            startgame()
        else:
            print(f"          ----------Thank You! Have a nice Day {name}----------")
            break