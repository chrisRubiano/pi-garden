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
