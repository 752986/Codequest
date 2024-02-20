from math import pi

def better_round(val: float, n_digits: int = 0) -> float:
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits

n_cases: int = int(input())
for val in range(n_cases):
    line: str = input().rstrip()
    
    diameter, motorRevs, power, rpm, capacity, voltage, distance = [float(val) for val in line.split(" ")]
    
    wheelCircum = diameter * pi
    wheelRevs = (distance * 100) / wheelCircum
    totalMotorRevs = wheelRevs * motorRevs
    timeTaken = totalMotorRevs / rpm
    powerDrawn = totalMotorRevs * power
    ampage = powerDrawn / voltage
    totalAmpMinutes = ampage * timeTaken
    totalAmpHours = totalAmpMinutes / 60
    missionSuccess = totalAmpHours <= capacity

    if missionSuccess:
        rounded = better_round(timeTaken, 4)
        print(f"Success {rounded:.4f}")
    else:
        print("Fail")
