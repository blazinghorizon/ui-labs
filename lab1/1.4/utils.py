def converison(value: float, from_metric: str, to_metric: str):
    # F to F, C to C, K to K
    if from_metric == to_metric:
        return value

    # TODO: write converison formulas
    if from_metric == 'F':
        if to_metric == 'C':
            pass
        elif to_metric == 'K':
            pass
    if from_metric == 'C':
        if to_metric == 'F':
            pass
        elif to_metric == 'K':
            pass
    if from_metric == 'K':
        if to_metric == 'F':
            pass
        elif to_metric == 'C':
            pass

    print(from_metric, to_metric)