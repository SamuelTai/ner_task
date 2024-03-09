
# Web Application with Docker Image

## Overview
This project consists of a web application built using FastAPI and Dockerized for easy deployment. The application extracts dates from text inputs using natural language processing (NLP) techniques.

## File Structure

```
project/
.venv/
src/
    ├── __init__.py   
    ├── api.py                 # Module containing FastAPI application definition
    ├── date_formatter.py      # Module for formatting extracted dates
    ├── extract_date_model.py  # Module for extracting dates using NLP
    ├── main.py                # Main script to run the FastAPI server
    ├── preprocess.py          # Module for text preprocessing
tests/
    ├── test_api.py            # Unit tests for the API module
    ├── test_date_formatter.py # Unit tests for the date formatting module
    ├── test_extract_date_model.py  # Unit tests for the date extraction module
    ├── test_main.py           # Unit tests for the main script
    └── test_preprocess.py     # Unit tests for the preprocessing module
Dockerfile                     # Dockerfile for building the Docker image
requirements.txt               # File listing Python dependencies
README.md                      # This README file
```

## How to Execute

1. **Set Up Environment**: Make sure you have Python and Docker installed on your system.

2. **Clone the Repository**: Clone this repository to your local machine.

3. **Install Dependencies**: Navigate to the project directory and install the Python dependencies using the following command:
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Build Docker Image**: Build the Docker image using the Dockerfile provided in the project directory. Run the following command:

   ```bash
   docker build -t my-web-service .
   ```

5. **Run Docker Container**: Run the Docker container using the built image. Specify the port mapping to expose the container's port 8000 to the host system. Execute the following command:

   ```bash
   docker run -d -p 8000:8000 my-web-service
   ```

6. **Access the Web Application**: Access the web application by navigating to `http://localhost:8000` in your web browser.

## Workflow

- **Development**: Develop the web application and its components in the `src` directory. Write unit tests for each module in the `tests` directory to ensure code quality and reliability.

- **Dockerization**: Dockerize the application by writing a Dockerfile to package the application and its dependencies into a Docker image. This allows for easy deployment and ensures consistency across different environments.

- **Testing**: Execute unit tests using a testing framework like pytest to verify the functionality of individual modules. Integration tests can also be performed to test the application as a whole.

- **Deployment**: Deploy the Dockerized web application to production or staging environments. Use container orchestration tools like Docker Compose or Kubernetes for managing and scaling the application.

## Architecture Benefits

- **Maintainability**: The modular structure of the codebase allows for easier maintenance and updates. Each component is separated into its own module, making it simpler to understand and modify.

- **Modularity**: The application follows a modular design, with distinct components responsible for specific tasks such as preprocessing, date extraction, and API handling. This promotes code reusability and flexibility.

- **Testing**: The codebase is designed with testing in mind, with separate unit tests for each module. This facilitates thorough testing of individual components and ensures the reliability of the application.

- **Dockerization**: Dockerizing the application provides numerous benefits, including portability, scalability, and consistency. It allows the application to run in any environment without worrying about dependencies or configuration issues.
