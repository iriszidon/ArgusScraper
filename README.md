# ArgusScraper

## Synopsis
This tool scrapes (a tiny part of) Github, stores the scraped data, verifies the validity of URLs, and verifies the performance.
Excercise for Argus

## Motivation
This is an exercise that demonstrates python code capabilities in a variety of technologies such as: Selenuim driver, docker and Mongo DB.

## Contributors
### Python
1. If you are new to python and pycharm, please see take this course https://www.udemy.com/pythonautomation/learn/v4/content.
This course contains a step-by-step instructions on how to set up an env to develop python from scratch! 
(You only need to view the first short videos, don't worry, it's not that long until you get productive.)
### Docker
1. If you are new to python and pycharm, I recommend taking this course  https://www.udemy.com/docker-flask-course/learn/v4/content. It teaches you dockers from scratch.

## Installation
### Selenuim Installation
1. Go to https://www.seleniumhq.org/download/ and install Selenuim Webdriver. (I am using chrome driver).
2. MUST!!! Place your cromedriver.exe file locally under the C:\Users\yourUserNameInYourMachine\ directory.
3. If you do not know your username do the following:
  * Type Windows key, then type cmd (Open a command prompt)
  * Type 'set' in the black command window
  * The value of the 'USERPROFILE' variable is where you should place cromedriver.exe
  
### RoboMongo client and Docker Installation
If you have OS Windows Home you cannot install Docker, in that case install Docker tool box.
1. Install Docker Toolbox. See how here: https://docs.docker.com/toolbox/toolbox_install_windows/#looking-for-troubleshooting-help
2. Robomongo client is available from https://robomongo.org/download. I used Robo 3T. All instructions are right there.

### Pycharm Installation
1. Pycharm is available at https://www.jetbrains.com/pycharm-edu/download/#section=windows
2. I am using Pycharm of Jetbrains. Pycharm has a terminal that allows to install python libraries.
3. In the Pycharm terminal type 'pip install pymongo' to use the mongo API in your python file.
4. In the Pycharm terminal type 'pip install selenium' to use the selenium functionality.
5. In the Pycharm terminal type 'pip install docker' to use the docker functionality.
6. In the Pycharm terminal type 'pip install flask' for the creation of the docker.

## How to run the Scraper
1. Open a python project and add the files from this repository (Put the files init.py, models, viewes under a subfolder named 'counter')
2. Open a Docker console, Go to the directory where you stored the scraper files.
3. Type into the docker console the following: docker-compose build
4. Type into the docker console the following: docker-compose up
2. The main class is Argus.py, please run only this file.
3. The functionality of the web page I scrape is in a saparate class, GitHubPgae.py. No need to run it.
4. Connect to Robomongo Client. Click the green triangle icon to fetch changes.

Enjoy!
Iris.
