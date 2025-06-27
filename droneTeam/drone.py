totalLeds = 100
onLeds = 99

color = "b"

leds = ""
for i in range(totalLeds):
    if i < onLeds:
       leds += "p"
    else:
       leds += "0"
print(leds)