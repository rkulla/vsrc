from setuptools import setup

setup(
    name='vsrc',
    version='1.1.1',
    author='Ryan Kulla',
    author_email='rkulla@gmail.com',
    package_dir={'': 'vsrc'},
    py_modules=['vsrc'],
    url='https://github.com/rkulla/vsrc',
    license='LICENSE.txt',
    description='Easily find and view a Python module\'s source code',
    long_description=open('README.txt').read(),
    entry_points={
        'console_scripts': ['vsrc = vsrc:main'],
    },
    install_requires=[],
)
