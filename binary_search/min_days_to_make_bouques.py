def min_days(bloomDay, reqBouq, noOfFlowersInEachBouque):
    def countBouque(bloomDay, noOfFlowersInEachBouque, currNoOfDays):
        consec = 0
        noOfBouque = 0

        for days in bloomDay:
            if currNoOfDays >= days:
                consec += 1
                if consec == noOfFlowersInEachBouque:
                    noOfBouque += 1
                    consec = 0
            else:
                consec = 0

        return noOfBouque

    if reqBouq * noOfFlowersInEachBouque > len(bloomDay):
        return -1
    
    l, r = 0, max(bloomDay)

    ans = -1

    while l <= r:
        m = (l + r) // 2

        noOfBouque = countBouque(bloomDay, noOfFlowersInEachBouque, m)

        if noOfBouque >= m:
            ans = m
            r = m - 1
        else:
            l = m + 1
    
    return ans

