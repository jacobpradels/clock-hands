import math
rawInput = 0
def runFunction(rawInput):
    realNums = rawInput.split(":")
    hour = float(realNums[0])
    minute = float(realNums[1])
    thetaMinute = 6 * minute
    thetaHour = (0.5 * minute) + (30 * hour)
    #thetaOtherTotal = 360 - abs(thetaMinute - thetaHour)
    thetaTotal = abs(thetaHour - thetaMinute)
    if (thetaTotal > 180):
        thetaTotal = 360 - thetaTotal
    if (rawInput != "0:00"):
        print("%.3f"%(thetaTotal))
    return rawInput


while rawInput != "0:00":
    rawInput = runFunction(input(""))
