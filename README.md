# EMR System API

API for the Electronic Medical Records (EMR) system with JWT authentication. The project is launched using Docker Compose.

---

## Quick Start

1. Clone the repository:
   ```bash
   git clone git@github.com:LanaRemenyuk/task1-emr_system-.git
   cd emr-system
  

2. Create a `.env` file in the root of the project (details will be provided with the assignment).

3. Start the project:

```bash

docker-compose up --build
```


- The server will be available at: [http://localhost:8000](http://localhost:8000).

## Endpoints

1. */login*: Obtain a JWT token.

2. */patients*: List of patients (accessible only to users with the role of doctor).

## API Documentation

1. Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

2. ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## Using the API

### Obtaining a JWT Token

Send a POST request to `/login` with the username and password. You can use the test data created by Docker Compose:

- *Username*: `admin`, `doctor`
- *Password*: `admin12adm`, `doctor12pass`

- Test data for the administrator can also be used to access the admin panel.

### Obtaining the List of Patients

Send a GET request to `/patients` with the JWT token in the header.

## Project Structure

- *code_dir/*:  
  Main application code.

- *tests/*:  
  Tests with coverage > 80%.

- *docker/*:  
  Dockerfile and docker-compose.yaml.

- *migrations/*:  
  Database migration files.

- *.env*:  
  File with environment variables.


## Made by: 
- Lana Remenyuk