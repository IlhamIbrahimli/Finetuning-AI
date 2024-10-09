from datetime import datetime
from datetime import timedelta
filename = input("AAA>")
file = open(filename, "r+")

lines = file.read().splitlines()
def get_time(message_line):
    #print(message_line)
    dt, msg = message_line.split(" - ",1)
    #print(msg)
    user, message = msg.split(":" , 1)

    dt_obj = datetime.strptime(dt, "%d/%m/%Y, %I:%M %p")
    #print(dt_obj)
    return dt_obj, user, message

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
#print(lines)
## Remove Links and media
for i in lines:

    if "https" in i:
        lines.remove(i)
    #get_time(i)
for c,i in enumerate(lines):

    if "<This message was edited>" in i:
        temp = i.split("<")
        lines[c] = temp[0]
for c,i in enumerate(lines):

    if "<Media omitted>" in i:
        temp = i.split("<")
        lines[c] = temp[0]

## Group by time + user
for i in range(len(lines)-2, -1, -1):
    time,user,msg = get_time(lines[i])
    new_time, new_user, new_msg = get_time(lines[i+1])
    #print(lines[i])
    if time  + timedelta(seconds=300) >= new_time and user == new_user:
        lines.pop(i+1)
        lines[i] = lines[i] + "\n" + new_msg
        
convo_lines = []
for i in range(len(lines)):
    convo_lines.append([lines[i]])
#print(convo_lines)
for i in range(len(convo_lines)-2, -1, -1):
    #print(convo_lines[i])
    time,user,msg = get_time(convo_lines[i][-1])
    new_time, new_user, new_msg = get_time(convo_lines[i+1][-1])
    #print(convo_lines[i])
    if time  + timedelta(hours=1) >= new_time:
        
        convo_lines[i] = convo_lines[i] + convo_lines[i+1]
        convo_lines.pop(i+1)


    


print(convo_lines)


