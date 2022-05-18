# CMPE 131 Website Project
- Brian Pham (@BP2470) Team Lead
    - Worked on implementation of account creation/deletion,login,logout, and adding pictures to items
- Andrew Chau (@AndrewC04)
    - Worked on implementation of adding items, finding items, and user rating
- Alexander Iakovlev (@alexander-iakovlev)
    - Worked on implmentation of seeing all available items from user sellers, buying/bidding/finding items, and adding items to seller store
- Wen Luo (@simonluo345)
    - Worked on implementation of adding items, splash page, user profile, and user rating

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

* `pip install Python` - This ensures an installation of Python on your IDE
* `pip install Flask` - This ensures an installation of Flask on your IDE
* `pip install Flask-Wtf` - This ensures an installation of Flask WTForms extension on your IDE
* `pip install Flask-SQLAlchemy` - This ensures an installation of Flask-SQLAlchemy extension on your IDE
* `py run.py` - This starts the website launch on your local computer. Check notes at bottom of page below.

## Starting Website

The website should be self-explanatory by going through the home screen and signing up/logging in.
* Access splash home screen
    * Sign Up for website
        * Log in the website
            * Add item posts/search for item/sign out/delete account
                * Add to cart/Bid for item/Buy item
                    * Buy item

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
