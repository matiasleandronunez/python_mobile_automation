# python_mobile_automation
Boilerplate python mobile automation project using behave, appium and docker containers.

## REQUIREMENTS
Android emulator requires kernel support for virtualization. This can be a problem when using a windows host (code was built and tested in Ubuntu 20.10)
To check if your linux distribution is supported:
```
sudo apt install cpu-checker
kvm-ok
```

## SOLUTION

Code is structured as follows:

```
python_mobile_automation
|
|- images: Samples to build custom nodes and connect them to the selenium hub.
|   |-android8.1: Emulator based on Android 8.1, including installation of the sample application to test
|
|- src_code: Base directory containing the actual test code
|   |- context
|   |     |- config.py: Singleton to easily access settings
|   |     |- driver.py: Instantiates the driver according to settings/scenario or feature tags
|   |     |- testsettings.json: Settings used to run the tests.
|   |
|   |- features: files containing the definition of feature and scenarios in gherkin
|   |     |...
|   |
|   |- pages: Contains the page objects representing different pages or sections of the apk
|   |     |- basePage.py: base page object from which all other PO inherit
|   |     |....
|   |
|   |- steps: Bindings that match each of the steps defined in the feature files. 
|   |     |- article_lookup.py
|   |
|   |- Dockerfile: docker file with the instruction on how to build a python container image fit to run these tests
|   |- environment.py: Hooks, methods to be triggered at certain points of the scenario/feature execution
|   |- main.py: simple script that runs tests using behave
|   |- requirements.txt: list of project dependencies, in order to quick install with pip
|
|- .gitignore
|- docker-compose.yml: A docker compose file, to quickly bring up the infrastructure.
|- launch.sh: A bash script that brings the test grid up, and installs the sample app. 
|- README.md

```

## DEPLOY & RUN

### The environment

Consists of a series of docker containers: 
* One group including the selenium (v3) grid hub
* A docker container with an Android Emulator with appium server connected to the selenium-hub
* A docker container based in a python3.8 image with tty where to run the tests from.

Deploy the whole environment simply by running:
```
launch.sh
```

Once up you can check the status of the grid by checking:
http://localhost:4444/grid/console

And the android emulator, that has noVNC support, at:
http://localhost:6080/


To run the tests, tty to the docker container named 'tests' and execute:

```
python3 main.py
```
