# ILLEGAL AS OF 31/12/2020; DO NOT USE
# Raid analyser program
# Originally made by cipher, cleaned up by cg

import random
import sys

while True:
    random.seed() # initialise random number generator
    occ, srv = 0, 0
    atk = rtatk = int(input("Please enter offensive force (relative). "))
    dfc = rtdfc = int(input("Please enter defensive force (relative). "))
    dlevel = input("Please enter simulation depth parameters. Enter F for fast setting, S for standard, and D for deep. ").lower()

    if dlevel == "f":
        iterations = 2 ** 12
    elif dlevel == "s":
        iterations = 2 ** 14
    elif dlevel == "d":
        iterations = 2 ** 16
    else:
        iterations = 2 ** 12
        print("Parameters invalid. Defaulting to fast simulation.")

    while occ + srv <= iterations:
        if dfc < 1:
            occ += 1
            atk, dfc = rtatk, rtdfc
        elif atk < 1:
            srv += 1
            atk, dfc = rtatk, rtdfc
        else:
            if atk >= 3:
                if dfc >= 2:
                    rll = random.randint(1, 7776)
                    if rll <= 2890:
                        dfc -= 2
                    elif rll <= 5165:
                        atk -= 2
                    else:
                        dfc -= 1
                        atk -= 1
                else:
                    rll = random.randint(1, 1296)
                    if rll <= 885:
                        dfc -= 2
                    else:
                        atk -= 2
            elif atk == 2:
                if dfc >= 2:
                    rll = random.randint(1, 1296)
                    if rll <= 295 :
                        dfc -= 2
                    elif rll <= 876:
                        atk -= 2
                    else:
                        dfc -= 1
                        atk -= 1
                else:
                    rll = random.randint(1, 216)
                    if rll <= 125:
                        dfc -= 2
                    else:
                        atk -= 2
            else:
                if dfc >= 2:
                    rll = random.randint(1, 216)
                    if rll <= 55:
                        dfc -= 2
                    else:
                        atk -= 2
                else:
                    rll = random.randint(1, 36)
                    if rll <= 15:
                        dfc -= 2
                    else:
                        atk -= 2

    print("Analysis complete.")
    print(f"Probability of attacker victory: {occ / (iterations / 100)}%. Probability of defender victory: {srv / (iterations / 100)}%.")
