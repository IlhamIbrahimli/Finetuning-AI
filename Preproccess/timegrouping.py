filename = input("AAA>")
file = open(filename, "r+")

lines = file.read().splitlines()
def get_time(message_line):
    dt, msg = message_line.split(" - ")
    date,time = dt.split(", ")
    print(date)
    print(time)
reverselines = lines[::-1]
def merge_multilines(rlines1):
    rlines = rlines1
    count=0
    while count != len(rlines):
        c=0
        count=0
        for i in rlines:
            if " - " not in i:
                print(i)
                rlines[c+1] += f"\n{i}"
                rlines.remove(i)
            else:
                count += 1
            c+=1
        print(rlines)
        print(len(rlines))
    return rlines
    
reverselines = merge_multilines(reverselines)

lines = reverselines[::-1]
print(lines)

for i in lines:
    get_time(i)
    if "http" in i:
        lines.remove(i)

