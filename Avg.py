number = 0.0
total = 0.0
avg = 0.0
checkfloat = 0  #檢查是否為小數點 ＃0:不是
string = '-1'
stringend = 'end' ##結束程式

while(1):
    checkfloat=0
    print('Please input your score :')
    grade=str(input())
    number+=1
    lenght=len(grade);
    if(grade==stringend):
        break
        
    for i in range(0,lenght-1):
        if(grade[i]=='.'):
            print('illegal input, ending the program...')
            total=0.0
            number=0.0
            checkfloat=1
            
    if(checkfloat==0):       
        
        if(int(grade)>=0 and int(grade)<=100):
            
            total+=int(grade)
            
        elif(grade==string):
            avg=total/(number-1)
            print('Your average score is :',end = '')
            print(avg)
            total=0.0
            number=0.0
            
        else:
            print('llegal input, ending the program...'); 
            total=0.0
            number=0.0
      
