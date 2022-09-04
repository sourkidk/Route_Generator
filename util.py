# This function iterates through the address and replaces any occurence of an address spelled out with it's single
# letter abbreviation.
def harmonize_directions(address)->str:
    directions = ['north', 'east', 'south', 'west', 'North', 'East', 'South', 'West']
    abbrev = ['N', 'E', 'S', 'W']
    temp = address
    for d in range(0, len(directions)):
        if directions[d] in address:
            temp = temp.replace(directions[d], abbrev[d%4])
        else:
            temp = temp
    return temp

# Converts minutes to time format HH:MM
def minutes_to_time(time_in_minutes):
    return f'{int(time_in_minutes / 60)}:{(int(time_in_minutes) % 60):02}'

# Converts time format HH:MM to minutes
def time_to_minutes(time: str):
    list = time.split(':')
    total = (int)(list[0]) * 60 + (int)(list[1])
    return total

# displays header infomation
def print_introduction():
    print('Western Goverornors University - Parcel Service')
    print('-----------------------------------------------')




