def merge(intervals):
    intervals.sort(key=lambda i: i[0])
    output = [intervals[0]]
    for s, e in intervals[1:]:
        l = output[-1][1]  # end value of last interval
        if s <= l:
            output[-1][1] = max(l, e)
        else:
            output.append([s, e])

    return output
