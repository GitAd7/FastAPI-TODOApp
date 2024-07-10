from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date
import logging

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Task model
class Task(BaseModel):
    id: int 
    title: str
    description: str
    due_date: date
    priority: int
    completed: bool

# In-memory list to store tasks
tasks = []
task_id_counter = 1

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    global task_id_counter

    # Log received task details
    logging.debug(f"Received task: {task}")

    try:
        task.id = task_id_counter
        task_id_counter += 1
        tasks.append(task.model_dump())  
        return task
    except Exception as e:
        # Log the error
        logging.error(f"Error creating task: {e}")
        # Raise an HTTP exception with a 500 status code and include the error message
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/task/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task Not Found")

@app.put("/task/id={task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            updated_task.id = task_id  # Ensure ID remains unchanged
            return updated_task
    raise HTTPException(status_code=404, detail="Task Not Found")

@app.delete("/task/{task_id}")
def del_task(task_id:int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"Status":"task Deleted Successfully"}
    raise HTTPException(status_code=404, detail="Task Not Found")

@app.get("/tasks/due/{due_date}", response_model=List[Task])
def get_tasks_by_due_date(due_date: date):
    tasks_due = [task for task in tasks if task.due_date == due_date]
    return tasks_due

@app.get("/tasks/priority/{priority}", response_model=List[Task])
def get_tasks_by_priority(priority: int):
    tasks_with_priority = [task for task in tasks if task.priority == priority]
    return tasks_with_priority

# GET endpoint to check the current tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks
