import math
def add_time(start, duration, day=False):
    time = start.split(" ")  
    timestamp = time[0].split(":")
    addtimestamp = duration.split(":")
    text = ""

    if int(addtimestamp[0]) > 24: 
        durationdays = math.ceil(int(addtimestamp[0]) / 24)
    duarationremtime = int(addtimestamp[0]) % 24

    newtime = 0
    day_list=["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]
    if day:
        index = day_list.index(day.capitalize())

    newtimemin = int(timestamp[1]) + int(addtimestamp[1]) 
    newtimehr = int(timestamp[0]) + int(duarationremtime)
    if newtimemin >= 60:
        newtimemin = newtimemin - 60
        newtimehr = newtimehr + 1

    if int(addtimestamp[0]) < 24:
        if time[1] == "AM":
            if newtimehr >= 12:
                time[1] = "PM"
                newtimehr = newtimehr - 12
        elif time[1] == "PM":
            if newtimehr >= 12:
                time[1] = "AM"
                text = "(next day)"
                newtimehr = newtimehr - 12
                if day:
                    index += 1 
                    if index > len(day_list):
                        index -= 7
    elif int(addtimestamp[0]) == 24:
        text = "(next day)"
        if day: 
            index += 1
            if index > len(day_list):
                index -= 7
        if newtimehr == 12:
            text = "(2 days later)"
            if day: 
                index += 1
                if index > len(day_list):
                    index -= 7
        if int(timestamp[1]) + int(addtimestamp[1]) > 60:
            if time[1] == "PM":
                time[1] = "AM"
            else:
                time[1] = "PM"
    else:
        newtimehr = newtimehr - 12
        num = int(addtimestamp[0]) // 12
        if num % 2 == 0:
            if time[1] == "AM":
                time[1] = "PM"
            else:
                time[1] = "AM"
        else:
            if time[1] == "PM":
                time[1] = "AM"
            else:
                time[1] = "PM"
        if day: 
            index += durationdays
            if index > len(day_list):
                index = index % 7
        text = f"({durationdays} days later)"

    if newtimehr == 0:
        newtimehr = 12

    if len(str(newtimemin)) == 1:
        if text:
            if day:
                newtime = f"{newtimehr}:0{newtimemin} {time[1]}, {day_list[index]} {text}"
            else:
                newtime = f"{newtimehr}:0{newtimemin} {time[1]} {text}"
        else :
            if day:
                newtime = f"{newtimehr}:0{newtimemin} {time[1]}, {day_list[index]}"
            else:
                newtime = f"{newtimehr}:0{newtimemin} {time[1]}"
    elif len(str(newtimemin)) == 2:
        if day:
            newtime = f"{newtimehr}:{newtimemin} {time[1]}, {day_list[index]} {text}"
        else:
            newtime = f"{newtimehr}:{newtimemin} {time[1]} {text}"

    return newtime.strip()