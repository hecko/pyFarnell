# pyFarnell - access Farnell information using Farnell REST API

[![Documentation Status](https://readthedocs.org/projects/pyfarnell/badge/?version=latest)](http://pyfarnell.readthedocs.io/en/latest/?badge=latest)

## Install

    pip install pyFarnell

## Use example

    #!/usr/bin/python
    from pprint import pprint
    import pyFarnell

    # the following is a Farnell API key
    f = pyFarnell.Farnell('asdfghjklusditmeshdoctis')
    pprint(f.get_part_number('2507703'))
