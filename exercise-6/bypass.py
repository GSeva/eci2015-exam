
"""
Exercise 6 solution.
"""


def bypass(string):
    """
    Bypass the taint in the string, tainted by taintmode library. Mutes the
    original string.

    Example usage:

    >>> from taintmode import taint, tainted; from bypass import bypass
    >>> foo = taint('foo')
    >>> tainted(foo)
    True
    >>> tainted(bypass(foo))
    False
    >>> tainted(foo)
    False
    """
    if hasattr(string, 'taints'):
        delattr(string, 'taints')
    return string


def bypass_safe(string):
    """
    Bypass the taint in the string, tainted by taintmode library. Doesn't mute
    the original string.

    Example usage:

    >>> from taintmode import taint, tainted; from bypass import bypass_safe
    >>> foo = taint('foo')
    >>> tainted(foo)
    True
    >>> tainted(bypass_safe(foo))
    False
    >>> tainted(foo)
    True
    """
    return str(string)
