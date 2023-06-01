def study_schedule(permanence_period, target_time):
    if not target_time or type(target_time) != int:
        return None

    count = 0

    for period in permanence_period:
        if (
            type(period) != tuple
            or type(period[0]) != int
            or type(period[1]) != int
            or len(period) != 2
            or period[0] < 0
            or period[1] < 0
            or period[0] > period[1]
        ):
            return None
        if period[0] <= target_time <= period[1]:
            count += 1

    return count
