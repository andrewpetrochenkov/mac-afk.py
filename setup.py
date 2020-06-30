import setuptools

setuptools.setup(
    name='mac-afk',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/afk']
)
