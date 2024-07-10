# FastAPI To-Do Application

## Overview
This project implements a simple To-Do application using FastAPI. It allows managing tasks with features like creating, updating, retrieving by ID, deleting, and filtering tasks by due date or priority.

## Prerequisites
- Python 3.9 or higher installed.
- Docker (optional, for containerization).

## Installation
1. Clone the repository:
git clone https://github.com/GitAd7/FastAPI-TODOApp.git
cd FastAPI-TODOApp


2. Set up a virtual environment (optional but recommended):

3. Install dependencies:
pip install -r requirements.txt


## Running the Application

### Without Docker
1. Start the FastAPI server:
uvicorn main
--reload


2. Access the API documentation:
Open your web browser and go to `http://localhost:8001/docs`.

### With Docker
1. Build the Docker image:
docker build -t todoapp .

2. Run the Docker container:
docker run -d -p 8001:8000 todoapp


3. Access the API documentation:
Open your web browser and go to `http://localhost:8001/docs`.

## API Endpoints
- `GET /tasks`: Retrieve all tasks.
- `POST /tasks`: Create a new task.
- `GET /tasks/{task_id}`: Retrieve details of a task by ID.
- `PUT /tasks/{task_id}`: Update a task by ID.
- `DELETE /tasks/{task_id}`: Delete a task by ID.
- `GET /tasks/due/{due_date}`: Retrieve tasks due on a specific date.
- `GET /tasks/priority/{priority}`: Retrieve tasks with a specific priority.

## Testing
Use tools like `curl` or Postman to interact with the API endpoints for testing purposes.

## Contact
For any issues or questions, please contact me at [adesht15@.com].
