import pymysql
import pymysql.cursors
from rotation import rotate
try:
    connection = pymysql.connect(user="root", password="password",
                            host="127.0.0.1",
                            database="IMPACT")
    cursor = connection.cursor()
except pymysql.InternalError as error:
    print("Connection Failed")
    print(error)

with open("Trial_1.log", "r") as f:
    curr_line = f.readline()
    count = 10
    ans = []
    temp = {}

    last_x_gyro = 0
    last_y_gyro = 0
    last_z_gyro = 0

    for curr_line in f:
        if curr_line == "-":
            ans.append(temp)
            temp = rotate(temp)

            insert = ("INSERT INTO `sensor_raw_one` (x_accel_one, y_accel_one, z_accel_one, x_gyro, y_gyro, z_gyro, temperature, x_accel_two, y_accel_two, z_accel_two, timestamp, x_angular_accel, y_angular_accel, z_angular_accel) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            try:
                cursor.execute(insert, (float(temp["x_accel_one"]), float(temp["y_accel_one"]), float(temp["z_accel_one"]), float(temp["x_gyro"]), float(temp["y_gyro"]), float(temp["z_gyro"]), float(temp["temp"]), float(temp["x_accel_two"]), float(temp["y_accel_two"]), float(temp["z_accel_two"]), float(temp["timestamp"]), float((float(temp["x_gyro"]) - last_x_gyro)/2), float((float(temp["y_gyro"]) - last_y_gyro)/2), float((float(temp["z_gyro"]) - last_z_gyro)/2)))
                cursor.execute("COMMIT")
            except pymysql.IntegrityError:
                print("Error. Username must be unique")
                print(temp)

            temp = {}
            count = 11
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
        # accelerometer 2, 16 bit signed int, range +- 16G
        elif count == 3:
            temp["x_accel_two"] = (int(curr_line)*16/2**16)
        elif count == 2:
            temp["y_accel_two"] = (int(curr_line)*16/2**16)
        elif count == 1:
            temp["z_accel_two"] = (int(curr_line)*16/2**16)
        elif count == 0:
            temp["timestamp"] = int(curr_line)
        else:
            ans.append(temp)
            temp = rotate(temp)

            insert = ("INSERT INTO `sensor_raw_one` (x_accel_one, y_accel_one, z_accel_one, x_gyro, y_gyro, z_gyro, temperature, x_accel_two, y_accel_two, z_accel_two, timestamp, x_angular_accel, y_angular_accel, z_angular_accel) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            try:
                cursor.execute(insert, (float(temp["x_accel_one"]), float(temp["y_accel_one"]), float(temp["z_accel_one"]), float(temp["x_gyro"]), float(temp["y_gyro"]), float(temp["z_gyro"]), float(temp["temp"]), float(temp["x_accel_two"]), float(temp["y_accel_two"]), float(temp["z_accel_two"]), float(temp["timestamp"]), float((float(temp["x_gyro"]) - last_x_gyro)/2), float((float(temp["y_gyro"]) - last_y_gyro)/2), float((float(temp["z_gyro"]) - last_z_gyro)/2)))
                cursor.execute("COMMIT")
            except pymysql.IntegrityError:
                print("Error. Username must be unique")
                print(temp)

            temp = {}
            count = 11
        count -= 1
    
for item in ans:
    print(item, "\n")