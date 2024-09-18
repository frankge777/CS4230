# Hello All

# Globals
OXY_LIST = []
OXY_ZERO = 0

def BloodOxygen(percent):
    global OXY_ZERO
    total = 0
    alarm = 0

    if percent > 99.9 or percent < 0:
        pass
    # Adds the new reading and gets rid of the oldest one
    if len(OXY_LIST) >= 6:
        OXY_LIST.pop(0)
        OXY_LIST.append(percent)
    else:
        OXY_LIST.append(percent)

    # Used for checking if the oxygen reader fell off the finger
    if percent == 0:
        OXY_ZERO += 1
    else:
        OXY_ZERO = 0
    if OXY_ZERO >= 3:
        i = 0
        for x in range(len(OXY_LIST)):
            if OXY_LIST[x] != 0:
                total += OXY_LIST[x]
            else:
                i += 1
        avg = total / i
        print("equipment fell off finger")
        return avg


    # Adds up the readinggs and gets the avereage
    for x in range(len(OXY_LIST)):
        total += OXY_LIST[x]
    avg = total / len(OXY_LIST)

    if percent <= 50:
        alarm = 3
    elif percent <= 80:
        alarm = 2
    elif percent <= 85:
        alarm = 1
    return (avg, alarm)


def main():
    pass


if __name__ == "__main__":
    main()
