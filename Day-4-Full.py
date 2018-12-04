import datetime
from itertools import *
from collections import *
import re

with open('input.txt') as f:    
    a = f.read().splitlines()

#------------------------------Part 1 Start --------------------------------
dpat = re.compile(r"\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\]")
lines = []
c = Counter()
for line in a:
    date = map(int,dpat.search(line).groups())
    d = datetime.datetime(*date)
    lines.append((d,line[19:]))
lines = sorted(lines)

perminute = defaultdict(lambda: defaultdict(int))
for d, line in lines:
    shift = re.findall(r'\d+', line)

    if shift:
        i_schleep = False
        guard = int(shift[0])
    i_schleep = 'asleep' in line
    woke = 'wakes up' in line
    if i_schleep:
        sleepstart = d
    
    if woke:                
        for minute in range(sleepstart.minute, d.minute):            
            c[guard]+=1
            perminute[guard][minute]+=1

guard_most_sleep = max(c.items(),key=lambda c: c[1])[0]
slept_min = max(perminute[guard_most_sleep].items(), key=lambda c: c[1])[0]

print(guard_most_sleep * slept_min)
#------------------------------Part 1 End ----------------------------------

#------------------------------Part 2 Start --------------------------------
times = 0
for guard in perminute:
    minutes = perminute[guard]
    slept_min = max(minutes.items(), key = lambda t: t[1])

    g_time = slept_min[1]
    big_minute = slept_min[0]
    
    if g_time >= times:
        times = g_time
        min = big_minute
        mr_g = guard

print(min*mr_g)
#------------------------------Part 2 End ----------------------------------
#Credit goes out to u/pythondevgb on reddit for being an indirect source of help
