def count_in_list(items, arg) -> int:
    '''
    Count occurrences of argumnet "arg" in collection "items",
    returning number of counted matches
    '''
    res = 0
    for x in items:
        res += 1 if x == arg else 0
    return res
