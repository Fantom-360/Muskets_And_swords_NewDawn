playlist = [
    ["Shape of You", "Ed Sheeran", "03:54"],
    ["Perfect", "Ed Sheeran", "04:40"],
    ["Blinding Lights", "The Weeknd", "03:20"],
    ["Bohemian Rhapsody", "Queen", "05:55"],
    ["Bad Guy", "Billie Eilish", "03:14"],
    ["Hallelujah", "Leonard Cohen", "04:39"]
]
p0 = playlist[0]
p1 = playlist[1]
p2 = playlist[2]
p3 = playlist[3]
p4 = playlist[4]
p5 = playlist[5]
c0 = str(p0[2])
cp0 = c0.split(":")
c1 = str(p1[2])
cp1 = c1.split(":")
c2 = str(p2[2])
cp2 = c2.split(":")
c3 = str(p3[2])
cp3 = c3.split(":")
c4 = str(p4[2])
cp4 = c4.split(":")
c5 = str(p5[2])
cp5 = c5.split(":")
sec = int(cp5[1]) + int(cp4[1]) + int(cp3[1]) + int(cp2[1]) + int(cp1[1]) + int(cp0[1]) 
min = int(cp5[0]) + int(cp4[0]) + int(cp3[0]) + int(cp2[0]) + int(cp1[0]) + int(cp0[0]) 
minplus = 0
while 60 < sec:
    sec = sec - 60
    minplus = minplus + 1
min = min + minplus
print("{}:{}".format(min, sec))

ps0 = int(cp0[0])60 + int(cp0[1])
ps1 = int(cp1[0])60 + int(cp1[1])
ps2 = int(cp2[0])60 + int(cp2[1])
ps3 = int(cp3[0])60 + int(cp3[1])
ps4 = int(cp4[0])60 + int(cp4[1])
ps5 = int(cp5[0])60 + int(cp5[1])
if ps0 > ps1:
    if ps0 > ps2:
        if ps0 > ps3:
            if ps0 > ps4:
                if ps0 > ps5:
                    print("ps0 je big")
                else:
                    print("ps5 je big")
            if ps4 > ps5:
                print("ps4 je big")
            else:
                print("ps5 je big")
        else:
            if ps3 > ps4:
                if ps3 > ps5:
                    print(playlist[3])
                else:
                    print("ps5 is big")
            else:
                if ps4 > ps5:
                    print("ps4 is big")
                else:
                    print("ps5 is big")
    else:
        if ps2 > ps3:
            if ps2 > ps4:
                if ps2 > ps5:
                    print("ps2 is big")
                else:
                    print("ps5 is big")
            else:
                if ps4 > ps5:
                    print("ps4 is big")
                else:
                    print("ps5 is big")
        else:
            if ps3 > ps4:
                if ps3 > ps5:
                    print(playlist[3])
                else:
                    print("ps5 is big")
            else:
                if ps4 > ps5:
                    print("ps4 is big")
                else:
                    print("ps5 is big")
else:
    if ps1 > ps2:
        if ps1 > ps3:
            if ps1 > ps4:
                if ps1 > ps5:
                    print("ps1 is big")
                else:
                    print("ps5 is big")
            else:
                if ps4 > ps5:
                    print("ps4 is big")
                else:
                    print("ps5 is big")
        else:
            if ps3 > ps4:
                if ps3 > ps5:
                    print(playlist[3])
                else:
                    print("ps5 is big")
            else:
                if ps4 > ps5:
                    print("ps4 is big")
                else:
                    print("ps5 is bigga")
    else:
        if ps2 > ps3:
            if ps2 > ps4:
                if ps2 > ps5:
                    print("ps2 is big")
                else:
                    print("ps5 is big")
            else:
                if ps4 > ps5:
                    print("ps4 si bigger")
                else:
                    print("ps5 is bigger")
        else:
            if ps3 > ps4:
                if ps3 > ps5:
                    print(playlist[3])
                else:
                    print("ps5 is bigger")
            else:
                if ps4 > ps5:
                    print("ps4 is bigger")
                else:
                    print("ps5 is bigger")