# -*- coding: utf-8 -*-


def groupInfoSorter(a, b):
    # TODO: Move to Group Membership
    assert hasattr(a, 'name')
    assert hasattr(b, 'name')

    aname = a.name.lower()
    bname = b.name.lower()
    if (aname < bname):
        retval = -1
    elif (aname == bname):
        retval = 0
    else:  # aname > bname
        retval = 1

    assert retval in (-1, 0, 1)
    return retval
