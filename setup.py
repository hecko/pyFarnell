from setuptools import setup, find_packages
 
setup(
    name='pyFarnell',
    version='0.1.0.dev7',
    description='Connect to Farnell REST API from Python. This is absolutely NOT OFFICIAL package!!',
    url='http://www.github.com/hecko/pyFarnell',
    author='Marcel Hecko',
    author_email='maco@blava.net',
    classifiers=[
                  'Development Status :: 3 - Alpha',
                  'Programming Language :: Python :: 2.7',
                ],
    packages=find_packages(),
    install_requires=['requests'],
)
