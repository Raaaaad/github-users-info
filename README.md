## Description
This projected was developed in 2022 for Allegro as a part of internship recruitment. It allows user to perform the following actions:
* listing repositories,
* checking the sum of stars for all repositories,
* listing the most popular languages

<a/>
for any Github user.
	
## Setup
 1. Choose a folder and clone this repository:<br />
    ``git clone <https://github.com/Raaaaad/github-user-info>``
 2. Create virtual environment for python:<br />
    ``python -m venv venv``
 3. Launch virtual environment:<br />
    * ``. venv/bin/activate `` - Mac, Linux <br />
    * ``venv\Scripts\activate`` - Windows
 4. Install required tools: <br />
    ``pip install -r requirements.txt``
 5. Launch application: <br />
    ``python app.py``
 6. Launch tests: <br />
    ``pytest``    

    <a/>
By default, the application works on localhost:5000. Address http://localhost:5000/apidocs/ uses Swagger and can be used to test all endpoints.

## Further development
Features that can be added to the application:
* Endpoints can also have a token param, which would be used for authentication to increase number of request per hour (GitHub has some limitations)
* More endpoints can be added, for example an endpoint returning info about languages used by followers.

## Conclusions
* App could be used by recruiters to determine to which project assign programmer to (for example if a person mostly uses Java, then she/he should be assigned to a Java project).
* Machine learning can be applied to for example determine if a person who mostly uses Java has followers who also mostly use this language.

