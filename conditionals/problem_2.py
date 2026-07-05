m1=int(input('enter a marks for math '))
m2=int(input('enter a marks for science '))
m3=int(input('enter a marks for hindi '))

percentage=(m1+m2+m3)/3
if(m1<33 or m2<33 or m3<33):
    print('fail')
elif(percentage<40):
    print('fail')
else:
    print("pass")

