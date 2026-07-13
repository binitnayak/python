n= int(input(" enter a number "))
table =[n*i for i in  range(1,11)]
with open("table.txt","a") as f:
    f.write(f"table of {n} :{str(table)}+\n")