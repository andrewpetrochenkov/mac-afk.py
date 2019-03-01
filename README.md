[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-afk.svg?longCache=True)](https://pypi.org/project/mac-afk/)
[![](https://img.shields.io/pypi/v/mac-afk.svg?maxAge=3600)](https://pypi.org/project/mac-afk/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-afk.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-afk.py/)

#### Install
```bash
$ [sudo] pip install mac-afk
```

#### Functions
function|`__doc__`
-|-
`mac_afk.days()`|afk time in days
`mac_afk.hours()`|afk time in hours
`mac_afk.minutes()`|afk time in minutes
`mac_afk.seconds()`|afk time in seconds

#### CLI
usage|`__doc__`
-|-
`python -m mac_afk.days`|MacOS afk time in days
`python -m mac_afk.hours`|MacOS afk time in hours
`python -m mac_afk.minutes`|MacOS afk time in minutes
`python -m mac_afk.seconds`|MacOS afk time in seconds

#### Examples
```python
>>> import mac_afk
>>> import time
>>> time.sleep(2); mac_afk.seconds()
2
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>