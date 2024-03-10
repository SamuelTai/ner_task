
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

# Date Extraction Process

## Overview
This document outlines the process of extracting dates from a string using the provided web service. The process involves several modules working together to preprocess the input text, extract dates, standardize them, and obtain the final response from the API.

## Step-by-Step Process

1. **Preprocessing Module**:
   - The input text containing dates undergoes preprocessing to remove any special characters and normalize the text.
   - Example: Input text: "The policy provides cover from 30th June 2019 to 1st July 2022 inclusive"
   - After preprocessing: "The policy provides cover from 30th June 2019 to 1st July 2022 inclusive"

2. **Extract Date Model Module**:
   - The preprocessed text is passed to the date extraction model, which utilizes natural language processing (NLP) techniques to identify and extract dates.
   - Example: Extracted dates: ["30th June 2019"]

3. **Date Formatting Module**:
   - The extracted dates are standardized into a consistent format (e.g., dd/mm/yyyy).
   - Example: Standardized dates: ["30/06/2019"]

4. **API Endpoint**:
   - The standardized dates are sent to the API endpoint as a POST request.
   - Example request payload:
     ```json
     {
       "text": "The policy provides cover from 30th June 2019 to 1st July 2022 inclusive"
     }
     ```
   
5. **API Response**:
   - The API processes the request, performs any necessary validation, and returns the response.
   - Example response:
     ```json
     {
       "dates": ["30/06/2019"],
       "message": "Success"
     }
     ```

## Conclusion
The date extraction process involves preprocessing the input text, extracting dates using NLP techniques, standardizing the extracted dates, and obtaining the final response from the API. 


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

6. **Access the Web Service**: Access the web service by navigating to `http://localhost:8000` in your web browser.

## Workflow

- **Development**: Develop the web application and its components in the `src` directory. Write unit tests for each module in the `tests` directory to ensure code quality and reliability.

- **Dockerization**: Dockerize the application by writing a Dockerfile to package the application and its dependencies into a Docker image. This allows for easy deployment and ensures consistency across different environments.

- **Testing**: Execute unit tests using a testing framework like pytest to verify the functionality of individual modules. Integration tests can also be performed to test the application as a whole.

- **Deployment**: Deploy the Dockerized web service to production or staging environments. Use container orchestration tools like Docker Compose or Kubernetes for managing and scaling the application.

## Architecture Benefits

- **Maintainability**: The modular structure of the codebase allows for easier maintenance and updates. Each component is separated into its own module, making it simpler to understand and modify.

- **Modularity**: The application follows a modular design, with distinct components responsible for specific tasks such as preprocessing, date extraction, and API handling. Moreover, it offers the flexibility to seamlessly swap out the date extraction model with custom models, thereby enhancing code reusability and adaptability.

- **Testing**: The codebase is designed with testing in mind, with separate unit tests for each module. This facilitates thorough testing of individual components and ensures the reliability of the application.

- **Dockerization**: Dockerizing the application provides numerous benefits, including portability, scalability, and consistency. It allows the application to run in any environment without worrying about dependencies or configuration issues.
