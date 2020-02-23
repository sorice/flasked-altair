# flasked-dashboard

- Tools to build simple dashboard/webapp with Flask and Altair! 
- Original inspired by Plotly's Dash

## Installation

All the code and examples were tested on Python 3.5. Older versions of Python
including 2.7 will likely work as well.

As usual, create a virtual environment and install the requirements with pip.

    pip install -r requirements.txt

## Running

The application uses Flask-Script to simplify common tasks such as starting
a development server. To run the application run the following command:

    python manage.py runserver

You can add `--help` to see what other start up options are available.

##  Usage

That application allows multiple users to chat online. You can launch the
application on your browser by typing `http://127.0.0.1:5000` on the address
bar.

## Known Issues

- Tooltips don't work yet. If your Altair chart has tooltips, it will raise an error when trying to export as JSON configuration for vega-lite.

## Aknowledgment

This project was originally forked from [flasked-altair](https://github.com/dushyantkhosla/flasked-altair.git)
The API, and authentication ideas, blueprint uses, and so on, were taken from [Miguel Grinberg tutorial PyCon 2016](https://github.com/miguelgrinberg/flack.git)
