def normalization(data):
    x = min(data)
    y = max(data)
    data = (data - x)/(y - x)
    average = sum(data)/len(data)
    return average
