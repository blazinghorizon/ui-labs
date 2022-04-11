def converison(value: float, from_metric: str, to_metric: str):
    # F to F, C to C, K to K
    if from_metric == to_metric:
        return value

    if from_metric == 'F':
        if to_metric == 'C': # F to C
            return float((value - 32) * 5 / 9)
        elif to_metric == 'K': # F to K
            return float((32 * value - 32) * 5 / 9 + 273.15)

    if from_metric == 'C':
        if to_metric == 'F': # C to F
            return float(value * 9 / 5 - 32)
        elif to_metric == 'K': # C to K
            return float(value + 273.15)

    if from_metric == 'K':
        if to_metric == 'F': # K to F
            return float(9 / 5 * (value - 273.15) + 32) 
        elif to_metric == 'C': # K to C
            return float(value - 273.15)

    return 0