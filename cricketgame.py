import random
import os
import sys
import math
from time import sleep
print('welcome to IPL')
print('there is total 8 teams you can choose one from totals team')
DC=['Shikhar Dhawan(captain)', 'Amit Mishra', 'Avesh Khan', 'Chris Morris',' Colin Munro',' Harshal Patel', 'Jayant Yadav',' Kagiso Rabada',' Manjot Kalra',' Prithvi Shaw']
MI=['Rohit Sharma (captain)', 'Quinton de Kock', 'Rahul Chahar', 'Siddhesh Lad', 'Suryakumar Yadav', 'Alzarri Joseph ',' Aditya Tare',' Anukul Roy', 'Ben Cutting', 'Evin Lewis', 'Hardik Pandya']
CSK =['MS Dhoni (captain)', 'Ambati Rayudu', 'Chaitanya Bishno','Deepak Chahar', 'Dhruv Shorey', 'Dwayne Bravo',' Faf du Plessis', 'Harbhajan Singh', 'Imran Tahir',' Karn Sharma']
KKR=['Dinesh Karthik(captain)',' Andre Russell', 'Chris Lynn', 'Kuldeep Yadav', 'Nitish Rana', 'Piyush Chawla', 'Prasidh Krishna', 'Rinku Singh',' Robin Uthappa', 'KC Cariappa',]
SRH=['basil Thampi',' Bhuvneshwar Kumar', 'Billy Stanlake', 'David Warner', 'Deepak Hooda', 'Kane Williamson', 'Khaleel Ahmed', 'Manish Pandey', 'Mohammad Nabi','Rashid Khan']
KXIP=['Andrew Tye', 'Ankit Rajpoot', 'Chris Gayle', 'David Miller', 'Karun Nair','Lokesh Rahul', 'Mayank Agarwal', 'Mujeeb Ur Rahman',' Ravichandran Ashwin', 'Mandeep Singh']
RCB =['Virat Kohli (captain)', 'AB de Villiers', 'Colin de Grandhomme', 'Kulwant Khejroliya', 'Moeen Ali', 'Mohammed Siraj', 'Nathan Coulter-Nile', 'Navdeep Saini', 'Parthiv Patel',' Pawan Negi']
RR=['Ajinkya Rahane', 'Aryaman Birla', 'Ben Stokes', 'Dhawal Kulkarni', 'Ish Sodhi', 'Jofra Archer', 'Jos Buttler',' Krishnappa Gowtham', 'Mahipal Lomror', 'Prashant Chopra']
teams =[DC,MI,CSK,KKR,SRH,KXIP,RCB,RR] 
#for i in enumerate(team):
 # print(i)
team =int(input('choose your team with given numerical no:0|1|2|3|4|5|6|7'))#user selecting the team
dict={0:'DC',1:'MI',2:'CSK',3:'KKR',4:'SRH',5:'KXIP',6:'RCB',7:'RR'}#creating a dict to store the names of the team
dict1={0:DC,1:MI,2:CSK,3:KKR,4:SRH,5:KXIP,6:RCB,7:RR}# creating a dict to store the players in that team
teamchoosen =dict[team]
teamplayers=dict1[team]

print(teamchoosen)
print('the team what you have choosen is',teamchoosen )
print('if player want to play against specific team type',' 1 =specific team','2= random team')
oppositionchoice =int(input('choose the opposition:1|2'))
if oppositionchoice ==1:
    oppositionteam =str(input('enter the team name'))
    if not  oppositionteam in teams:
         print('spelling error choose correctly the team name')
         print(teams)

    else:
          print('succesfully choosen opposite team',oppositionchoice)
          print('toss time')
          print('head =1','tail =0')
          toss =[1,0]
          head=1
          tail =0
          teamcall =int(input('enter the side of the coin you want:1|0'))
          if toss.choice == teamcall:
             user =int(input('you have won the toss what you want to decide','batting =1','bowling =0','enter the choice:1|0'))
             if user ==1:
                 print('team has choosen batting')
                 print('game start in 5 second')
                 for i in range(5):
                     pass
                 print('HOME TEAM FOR TODAY MATCH')
                 print(teamplayers)
                 print('AWAY TEAM FOR TODAY MATCH')
                 print('the opposite team is',oppositionchoice)
                 print('match has started all the best')
                 while 1:
                     (over1,over2,over3,over4,over5)=(6,6,6,6,6)
                     runs=[0,1,2,3,4,5,6,noball,out]
                     totalballs =len(over1)+len(over2)+len(over3)+len(over4)+len(over5)          
                     runsored=0
                     playerout=0
              
                     for k in (1,totalballs):
              
                        eachrun=random.choice(runs)
                 
                        if (eachrun ==0 or eachrun==1 or eachrun==2 or eachrun==3 or eachrun==4 or eachrun==5 or eachrun==6) and playerout<11:
                            runscored+=eachrun
                        elif:
                             if eachrun==noball and playerout<11:
                               runscored+=1+eachrun
                           
                               if eachrun ==0 or eachrun==1 or eachrun==2 or eachrun==3 or eachrun==4 or eachrun==5 or eachrun==6:
                                  runscored+=eachrun
                                  if eachrun==noball:
                                      print('after bowling two succesive no ball the bolwer got change')
                                      runscored+=eachrun+1
                        elif eachrun==out and playerout<11:
                             playerout+=1
                        else:
                            keyboardInterupt
            
              
              
              print('the final score card is ',runscored,'-',playerout ,end= '')
              if playerout<11 and k<30:
                break
                       
                
        
    else:
        print('team has choosen bowling')
        print('game start in 5 second')
        for i in range(5):
              pass
        print('match has started all the best')
        print('HOME TEAM FOR TODAY MATCH')
        print(teamplayers)
        print('AWAY TEAM FOR TODAY MATCH')
        print(oppositeteamplayer)
        print('match has started all the best')
        while True:
              (over1,over2,over3,over4,over5)=(6,6,6,6,6)
              runs=[0,1,2,3,4,5,6,noball,out]
              totalballs =len(over1)+len(over2)+len(over3)+len(over4)+len(over5)          
              oppositionscore=0
              playerout=0
              
              for j in (1,totalballs):
              
                  eachrun=random.choice(runs)
                 
                  if (eachrun ==0 or eachrun==1 or eachrun==2 or eachrun==3 or eachrun==4 or eachrun==5 or eachrun==6) and playerout<11:
                       oppositionscored+=eachrun
                  elif:
                       if eachrun==noball and playerout<11:
                          oppositionscored+=1+eachrun
                           
                           if eachrun ==0 or eachrun==1 or eachrun==2 or eachrun==3 or eachrun==4 or eachrun==5 or eachrun==6:
                               oppositionscored+=eachrun
                               if eachrun==noball:
                                   print('after bowling two succesive no ball the bolwer got change')
                                   oppositionscored+=eachrun+1
                  elif eachrun==out and playerout<11:
                        playerout+=1
                  else:
                      Keyboardinterupt
            
              
              
              print('the final score card for opposition team is  ',oppositionscored,'-',playerout ,end= '')
              if playerout<11 and k<30:
                break
            
        
if runscored> oppositionscored:
    print('YOU HAVE WON THE GAME')
elif oppositionscored >runscored:
    print('YOU HAVE LOST THE GAME')
    print('BETTER LUCK NEXT TIME')
elif oppositionscored==runscored:
    print('ITS A DRAW')
else:
    KeyboardInterupt
                         
          
          
               
else:
    values =(0,1,2,3,4,5,6,7)
    oppositionteam =random.choice(values)
    dict3={0:'DC',1:'MI',2:'CSK',3:'KKR',4:'SRH',5:'KXIP',6:'RCB',7:'RR'}#creating a dict to store the names of the team
    dict4={0:DC,1:MI,2:CSK,3:KKR,4:SRH,5:KXIP,6:RCB,7:RR}# creating a dict to store the players in that team
    oppositeteamchoosen=dict3[values]
    oppositeteamplayers=dict4[values]

  
    print('toss time')
    print('head =1','tail =0')
    toss =[1,0]
    head=1
    tail =0
    teamcall =int(input('enter the side of the coin you want:1|0'))
    if toss.choice == teamcall:
       user =int(input('you have won the toss what you want to decide','batting =1','bowling =0','enter the choice:1|0'))
       if user ==1:
           print('team has choosen batting')
           print('game start in 5 second')
           for i in range(5):
               pass
           print('HOME TEAM FOR TODAY MATCH')
           print(teamplayers)
           print('AWAY TEAM FOR TODAY MATCH')
           print(oppositeteamplayer)
           print('match has started all the best')
           while 1:
              (over1,over2,over3,over4,over5)=(6,6,6,6,6)
              runs=[0,1,2,3,4,5,6,noball,out]
              totalballs =len(over1)+len(over2)+len(over3)+len(over4)+len(over5)          
              runsored=0
              playerout=0
              
              for k in (1,totalballs):
              
                  eachrun=random.choice(runs)
                 
                  if (eachrun ==0 or eachrun==1 or eachrun==2 or eachrun==3 or eachrun==4 or eachrun==5 or eachrun==6) and playerout<11:
                       runscored+=eachrun
                  elif:
                       if eachrun==noball and playerout<11:
                           runscored+=1+eachrun
                           
                           if eachrun ==0 or eachrun==1 or eachrun==2 or eachrun==3 or eachrun==4 or eachrun==5 or eachrun==6:
                               runscored+=eachrun
                               if eachrun==noball:
                                   print('after bowling two succesive no ball the bolwer got change')
                                   runscored+=eachrun+1
                   elif eachrun==out and playerout<11:
                         playerout+=1
                    else:
                        Ketboard interupt
            
              
              
              print('the final score card is ',runscored,'-',playerout ,end= '')
              if playerout<11 and k<30:
                break
                       
                
        
    else:
        print('team has choosen bowling')
        print('game start in 5 second')
        for i in range(5):
              pass
        print('match has started all the best')
        print('HOME TEAM FOR TODAY MATCH')
        print(teamplayers)
        print('AWAY TEAM FOR TODAY MATCH')
        print(oppositeteamplayer)
        print('match has started all the best')
        while True:
              runs=[0,1,2,3,4,5,6,noball,out]
              (over1,over2,over3,over4,over5)=(6,6,6,6,6)
              totalballs =len(over1)+len(over2)+len(over3)+len(over4)+len(over5)          
              oppositionscore=0
              playerout=0
              
              for j in (1,totalballs):
              
                  eachrun=random.choice(runs)
                 
                  if (eachrun ==0 or eachrun==1 or eachrun==2 or eachrun==3 or eachrun==4 or eachrun==5 or eachrun==6) and playerout<11:
                       oppositionscored+=eachrun
                  elif:
                       if eachrun==noball and playerout<11:
                          oppositionscored+=1+eachrun
                           
                           if eachrun ==0 or eachrun==1 or eachrun==2 or eachrun==3 or eachrun==4 or eachrun==5 or eachrun==6:
                               oppositionscored+=eachrun
                               if eachrun==noball:
                                   print('after bowling two succesive no ball the bolwer got change')
                                   oppositionscored+=eachrun+1
                  elif eachrun==out and playerout<11:
                             playerout+=1
                  else:
                      Keyboard interupt
            
              
              
              print('the final score card for opposition team is  ',oppositionscored,'-',playerout ,end= '')
              if playerout<11 and k<30:
                break
            
        
if runscored> oppositionscored:
    print('YOU HAVE WON THE GAME')
elif oppositionscored >runscored:
    print('YOU HAVE LOST THE GAME')
    print('BETTER LUCK NEXT TIME')
elif oppositionscored==runscored:
    print('ITS A DRAW')
else:
    KeyboardInterupt
                         
