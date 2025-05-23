def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

    print("get total_score: {}, total_count: {}".format(total_score, total_count))
    if total_count == 0:
        print("total_count is zero!")
        return 0.0
    return round(total_score / total_count, 2)
