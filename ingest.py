with open("RightEarFB.txt", "r") as f:
    curr_line = f.readline()
    count = 10
    ans = []
    temp = {}

    for curr_line in f:
        if curr_line == "-":
            break

        # newline
        if count == 11:
            continue
        # accelerometer 1, 16 bit signed int, range +- 16G
        if count == 10:
            temp["x_accel_one"] = (int(curr_line)*16/2**16)
        elif count == 9:
            temp["y_accel_one"] = (int(curr_line)*16/2**16)
        elif count == 8:
            temp["z_accel_one"] = (int(curr_line)*16/2**16)
        # gyro, 16 bit signed int, range +- 125 deg/sec 
        elif count == 7:
            temp["x_gyro"] = (int(curr_line)*125/2**16)
        elif count == 6:
            temp["y_gyro"] = (int(curr_line)*125/2**16)
        elif count == 5:
            temp["z_gyro"] = (int(curr_line)*125/2**16)
        #raw temp, 12 bit signed int, range -40 to +85, 0 is at 25
        elif count == 4:
            temperature = 25+int(curr_line)/16
            temp["temp"] = temperature
            if temperature < -40 or temperature > 85:
                print("Error")
        # accelerometer 2, 16 bit signed int, range +- 2G
        elif count == 3:
            temp["x_accel_two"] = (int(curr_line)*2/2**16)
        elif count == 2:
            temp["y_accel_two"] = (int(curr_line)*2/2**16)
        elif count == 1:
            temp["z_accel_two"] = (int(curr_line)*2/2**16)
        else:
            ans.append(temp)
            temp = {}
            count = 11
        count -= 1
    
for item in ans:
    print(item, "\n")