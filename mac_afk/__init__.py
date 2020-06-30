__all__ = ['seconds', 'minutes', 'hours', 'days']


import os


def seconds():
    """afk time in seconds"""
    cmd = """
/usr/sbin/ioreg -c IOHIDSystem | /usr/bin/perl -ane 'if (/Idle/) {$idle=(pop @F)/1000000000; print $idle,"\n"; last}'
"""
    LC_ALL = os.environ.get("LC_ALL", None)
    try:
        os.environ["LC_ALL"] = "C"
        out = os.popen(cmd).read().strip()
        return int(float(out.strip()))
    finally:
        if LC_ALL:
            os.environ["LC_ALL"] = LC_ALL
        else:
            del os.environ["LC_ALL"]


def minutes():
    """afk time in minutes"""
    return seconds() % 60


def hours():
    """afk time in hours"""
    return minutes() % 60


def days():
    """afk time in days"""
    return hours() % 24
