SPEED_LIMIT = 100

wanted = ["scott mouat", "loshua jin", "kfc", "sam chen", "wilcong"]


def speed_get(speed_text):
    while True:
        try:
            speed = float(input(speed_text))
            if speed < 0:
                print("Please input a positive speed.")
                continue
            return speed
            break
        except ValueError:
            print("Please input a number.")


def speed_test():
    repeat = True
    while repeat:
        speed = speed_get("What is your average speed in km/h? ")
        if speed >= SPEED_LIMIT + 80:
            print("You must go to jail.")
        elif speed >= SPEED_LIMIT + 50:
            over_limit = speed - SPEED_LIMIT
            print("u went over speed limit by {}kmh, rip ur license bro, sry 4 ur lose. no cap :cap:".format(over_limit))
        elif speed > SPEED_LIMIT:
            fine = round(speed - 100)
            print("You went over the speed limit by {}kmh, you have been fined ${}"
                .format(fine, fine * 10))
        else:
            print("Not speeding, well done!")
        again = input("Do you want to enter another Speed? (enter N to exit) ").lower()
        if again == "n":
            repeat = False
            exit()


name = input("What is the name of the person you want to check? ").lower()
if name in wanted:
    print("Should be arrested.")
    exit()


speed_test()
