# Ryanair

Unfortunately I didn't manage to get the test running in a docker container. Lack of knowledge about docker and time 
pressure got the best of me.

To run the tests you have to set up a virtual env and install a couple of things, also make sure that you have chrome 
installed on your local machine.

Download the repo or just the test file `test_booking_a_flight.py`

1.Open terminal in the same folder where you have download the file
2. `pipenv shell`
3. `pipenv install selenium, pytest, pytest-selenium`
4. `pipenv run python -m pytest`

The test is set to run not in the headless mode, I used that to see how to the test is executed. The test is also
set to maximise the browser because it sometimes can't seem to locate certain elements.

Here are some of the resources I used :
`https://hub.docker.com/
https://docs.docker.com/engine/reference/commandline/build/
https://selenium-python.readthedocs.io/index.html`

I tried to create a docker file and run the test inside, I managed to get as far as a sample pytest but not a 
selenium pytest. The pytest working dockerfile is in the repo, to run that you have to execute the following command
from the terminal where the docker file is located:
`docker build -t selenium_docker .
`It runs on python 2.7 which is not ideal.

The docker file is a combinations of things that I found online and modified but I couldn't fully figure
it out. The initial setup is quiet long and large.

I was thinking about using this docker hub image for my docker 
`https://hub.docker.com/_/alpine`
simply because of it's size
or 
`https://hub.docker.com/_/ubuntu`
