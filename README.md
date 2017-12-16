# Pi Garden

![Harvest moon logo](harvest-moon-logo.jpg)

## Features!
* communicates with arduino through serial to receive analog sensor data
* Django app with sensor data and graphs

TODO:
* Django app with sensor data
    * view last photo taken along with data
* python irrigation script in crontab
    * Scheduled every afternoon
    * [Twitter API integration](https://github.com/bear/python-twitter)
    * [Facebook API integration](http://nodotcom.org/python-facebook-tutorial.html)
    * OPTIONAL to water the plants if i send a tweet
* another python script to sense when the plants are thirsty
    * should also send tweets about it
* Script to save sensor data in a database
* Graph sensor data history with [django graphos](https://github.com/agiliq/django-graphos)
* Push notifications via [pushover](https://pushover.net/)

-------

## Instalation

* `sudo -H pip3 install virtualenv`
* `sudo -H pip3 install virtualenvwrapper`
* `nano .bashrc` (or .zshrc) and add to the end of the file:
```sh
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
source /usr/local/bin/virtualenvwrapper.sh
export WORKON_HOME=$HOME/.virtualenvs
```
* `mkvirtualenv <project's name>` to create a virtual environment to host all our python libraries
* `workon <project's name>`
    * `deactivate` to exit the virtual environment
* once in the virtual environment run `pip3 install -r requirements.txt`