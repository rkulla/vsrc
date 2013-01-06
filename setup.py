from distutils.core import setup

setup(
    name='vsrc',
    version='1.1.0',
    author='Ryan Kulla',
    author_email='rkulla@gmail.com',
    packages=['vsrc', 'vsrc.test'],
    url='http://pypi.python.org/pypi/vsrc/',
    license='LICENSE.txt',
    description='Easily find and view a Python module\'s source code',
    long_description=open('README.txt').read(),
    install_requires=[],
)
