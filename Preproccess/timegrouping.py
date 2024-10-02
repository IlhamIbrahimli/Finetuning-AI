from datetime import datetime
filename = input("AAA>")
file = open(filename, "r+")

lines = file.read().splitlines()
def get_time(message_line):
    dt, msg = message_line.split(" - ")
    user, message = msg.split(":")

    dt_obj = datetime.strptime(dt, "%d/%m/%Y, %I:%M %p")
    print(dt_obj)
    return dt_obj, user

reverselines = lines[::-1]
def merge_multilines(rlines1):
    rlines = rlines1
    count=0
    while count != len(rlines):
        c=0
        count=0
        for i in rlines:
            if " - " not in i:

                rlines[c+1] += f"\n{i}"
                rlines.remove(i)
            else:
                count += 1
            c+=1
    return rlines
    
reverselines = merge_multilines(reverselines)

lines = reverselines[::-1]
#print(lines)
for i in range(len(lines)):
    if "am" in lines[i]:
        lines[i] = lines[i].replace("am","AM",1)
    else:
        lines[i] = lines[i].replace("pm","PM",1)
print(lines)
## Remove Links and media
for i in lines:

    if "http" in i:
        lines.remove(i)
    get_time(i)
for c,i in enumerate(lines):

    if "<This message was edited>" in i:
        temp = i.split("<")
        lines[c] = temp[0]
for c,i in enumerate(lines):

    if "<Media omitted>" in i:
        temp = i.split("<")
        lines[c] = temp[0]

## Group by time
for i in range(len(lines)):
    time,user = get_time(lines)
    


#print(lines)


