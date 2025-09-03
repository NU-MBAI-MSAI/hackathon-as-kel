'''Authors: Sneha Basu, Anisha Salunkhe'''

def heatingcooling():
    userTemp = float(input("Enter the average daily temperature: "))
    cool_days= 0
    hot_days = 0
    while(userTemp > -459):
        userTemp = float(input("Enter the average daily temperature: "))
        if userTemp > 80:
            cool_days = cool_days + 1
        elif userTemp < 60 :
            hot_days += 1
    output = "Heating days: "+ str(hot_days)
    output2 = "Cooling days: "+ str(cool_days)
    return output +"\n"+ output2


if __name__ == '__main__':
    print(heatingcooling())


