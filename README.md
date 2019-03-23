<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-afk.svg?longCache=True)](https://pypi.org/project/mac-afk/)
[![](https://img.shields.io/pypi/v/mac-afk.svg?maxAge=3600)](https://pypi.org/project/mac-afk/)
[![](https://img.shields.io/npm/v/mac-afk.svg?maxAge=3600)](https://www.npmjs.com/package/mac-afk)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-afk.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-afk.py/)

#### Installation
```bash
$ [sudo] npm i -g mac-afk
```
```bash
$ [sudo] pip install mac-afk
```

#### CLI
usage|`__doc__`
-|-
`python -m mac_afk.days` |macOS afk time in days
`python -m mac_afk.hours` |macOS afk time in hours
`python -m mac_afk.minutes` |macOS afk time in minutes
`python -m mac_afk.seconds` |macOS afk time in seconds

```bash
usage: afk
```

#### Examples
```python
>>> import mac_afk
>>> import time
>>> time.sleep(2); mac_afk.seconds()
2
```

```bash
$ sleep 3 && afk
3
```

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>