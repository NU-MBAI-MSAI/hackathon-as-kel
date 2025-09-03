'''Authors: Sneha Basu, Anisha Salunkhe'''

def speeding_ticket(speed_limit, driving_speed):
    diff = speed_limit - driving_speed
    if speed_limit < 0 or driving_speed < 0:
        return "error, negative speeds"
    if diff > 10:
        return 50
    elif diff >= -20 and diff <= -6:
        return 75
    elif diff >= -40 and diff <= -21:
        return 150
    elif diff < -40 :
        return 300
    else:
        return 0

if __name__ == "__main__":
    #test 1
    speed_limit = -1
    driving_speed = 0
    result = speeding_ticket(speed_limit, driving_speed)
    print(result)

    #test 2
    speed_limit = 10
    driving_speed=0
    result = speeding_ticket(speed_limit, driving_speed)
    print(result)

    #test 3
    speed_limit = "a"
    driving_speed = 20
    result = speeding_ticket(speed_limit, driving_speed)
    print(result)

