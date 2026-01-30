def min_capacity(weights, days):
    def daysToShipAll(weights, maxCapcity):
        # if the max-weight is 3 and maxCap is 2 -> at a point the nested while condition will go into infinite loop
        if max(weights) > maxCapcity:
            return float("inf")
        
        days = 0
        i = 0
        while i < len(weights):
            j = i
            total = 0
            while j < len(weights) and total + weights[j] <= maxCapcity:
                total += weights[j]
                j += 1
            days += 1
            i = j 
        
        return days
    
    l, r = 1, sum(weights)

    ans = r
    
    while l <= r:
        m = (l + r) // 2

        curDays = daysToShipAll(weights, m)

        if curDays <= days:
            ans = m
            r = m - 1
        else:
            l = m + 1

    return ans 


print(min_capacity([1,2,3,4,5,6,7,8,9,10], 5))