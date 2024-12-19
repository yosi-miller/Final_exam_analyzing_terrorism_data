Here is a basic `README.md` file for your project:

# Project Title

## Description
This project involves working with a MongoDB database to store and retrieve crash data. It includes functionalities for reading CSV files, populating the database, and running various queries and aggregations on the data.

## Installation
1. Clone the repository:
    ```sh
    git clone <repository_url>
    ```
2. Navigate to the project directory:
    ```sh
    cd <project_directory>
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```

5. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
### Running the Application
1. Ensure MongoDB is running on `localhost:27017`.
2. Run your application as needed.

### Running Tests
#### Run All Tests
To run all tests using `pytest`, execute the following command:
```sh
pytest
```

#### Run a Specific Test File
To run a specific test file, use the following command:
```sh
pytest path/to/test_file.py
```
For example, to run the tests in `test/db_test.py`, use:
```sh
pytest test/db_test.py
```

## Logging
The project includes a logging service located in `services/logger_server.py` for logging errors and information.