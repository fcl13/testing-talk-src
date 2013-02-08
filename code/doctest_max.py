def my_max(iterable):
    """ find the maximum in an iterable

    >>> my_max([1])
    1
    >>> my_max([1, 2])
    2
    >>> my_max([-1, -2])
    -1
    """
    best = iterable[0]
    for i in iterable[1:]:
        if i > best:
            best = i
    return best

