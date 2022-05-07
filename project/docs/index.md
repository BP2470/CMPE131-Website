# CMPE 131 Project Index

A simple rundown of starting the website

## Installation

An installation of Python and IDE is needed to start up the website.

Visit [Python](python.org) for the latest installment of Python for your operating system.

Recommended IDEs to use: 
[Visual Studio Code](code.visualstudio.com) or [Ubuntu Desktop](ubuntu.com)

Once installed, make sure to download or clone a copy of the repository of the `project` folder to use for the IDE.

## Commands to Start

Through your IDE's terminal run the following commands:

* `pip install python` - This ensures an installation of Python on your IDE
* `pip install flask` - This ensures an installation of Flask on your IDE
* `py run.py` - This starts the website launch on your local computer. Check notes at bottom of page below.

## Project layout

    project/
        run.py    # The initialization of the website
        app/  # The documentation homepage.
        ...       # Other minor documentations/config files
            __init__.py # Constructor for initialization
            models.py # Class constructor for objects in database
            routes.py # Code for html directors and other class constructors
            app.db # The database for the website
            ... # Other constructing files used by routes.py and models.py for building the website

## Notes

* The command `py run.py` must be run in the same directory of the project which is located ../project/
    * Make sure to use `cd` to get here first.
        Example : `cd Whereverthisfileis/project/`
