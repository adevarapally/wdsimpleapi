# WD Sample API

## Prerequisites

You need Python 3.6 or later.

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3.6 python3-pip python3.6-venv python3.6-dev

Recommended to update before running the above command.

    $ sudo apt-get update

For other Linux flavors, OS X and Windows, packages are available at

http://www.python.org/getit/

Once you're done installing Python 3, check that it install correctly.

    $ python --version
    Python 3.6

Check that PIP is install as well

    $ pip3 --version
    pip 20.0.2 from /usr/local/lib/python3.6/site-packages/pip (python 3.6)

If its not installed you can run: 

    $ sudo apt-get python3-pip

### Create Python Virtual Environment

    $ python3.6 -m venv venv

### Load Python Virtual Environment

    $ source venv/bin/activate

## Installation

    $ pip install -r requirements.txt

# Run the API

    $ python run.py
    
    By default the API uses the port 5000

# Run Test

    $ python -m unittest logic_test.py
