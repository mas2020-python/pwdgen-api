# Swisscom Tech Assessment

The assesment is a FastAPI Web application able to generate a random password. The format of the generated password
can be decided by the user passing to the web method specific argument (query params).

## Application requirements
The service should follow these requirements:
- Password length (if length is for example 10 it should generate and return random password with length of 10)
- Numbers flag (if enabled it should consider number symbols during password generation, like ‘1’, ‘2’, …, ‘9’)
- Lowercase chars flag (if enabled it should consider lowercase ascii characters also during password generation, like ‘a’, ‘b’, … , ‘z’)
- Uppercase chars flag (if enabled it should consider uppercase ascii characters also during password generation, like ‘A’, ‘B’, … , ‘Z’)
- Special symbols flag (if enabled it should consider special symbols also during password generation, like ‘%’, ‘$’, … , ‘@’)
- Password length is limited to 200 characters max
- It should raise an exception and return formatted response correspondingly in case if user makes request with disabling all features

Default password length and default flags should be configurable from the server.

## Technical considerations

The application will use the following Python libraries:
- `pytest`: in order to make the unit test
- `fastapi`: for the deployment of the Web API service
- 


Locally the libraries will be installed into a virtual environment and each dependencies will be listed
in a `requirements.txt` file.
To reproduce locally you have to follow these steps:
```shell
python3 -m venv .venv --prompt='swisscom-asses'
source .venv/bin/activate
pip3 install -r requirements.txt
```

The application has been developed using Python 3.11.0, a lower version of Python should be ok as well. The application
has not be tested in a multiple env (using `tox` for example) for a matter of timing.

### Folder structure

The service has the following folder structure:

- `src`: it is the folder that contains the application code
- `configs`: it is the folder that contains the configuration files. The config module will expose these values for the entire project.







