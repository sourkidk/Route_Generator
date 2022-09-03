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

def time_formatting(time_in_minutes):
    return f'{int(time_in_minutes / 60)}:{(int(time_in_minutes) % 60):02}'


