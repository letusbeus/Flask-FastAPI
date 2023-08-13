from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Task(BaseModel):
    title: str
    description: str
    status: str


tasks = []


@app.get('/')
async def root():
    return {"message": "Welcome to Task Manager!"}


@app.get('/tasks/', response_model=List[Task])
async def get_tasks():
    if len(tasks) != 0:
        return tasks
    else:
        raise HTTPException(status_code=404, detail='Tasklist is empty')


@app.get('/tasks/{task_id}', response_model=Task)
async def get_task(task_id: int):
    task_id -= 1
    if 0 <= task_id < len(tasks):
        return tasks[task_id]
    raise HTTPException(status_code=404, detail='Task not found')


@app.post('/tasks/', response_model=Task)
async def create_task(task: Task):
    tasks.append(task)
    return task


@app.put('/tasks/{task_id}', response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    task_id -= 1
    if 0 <= task_id < len(tasks):
        tasks[task_id] = updated_task
        return updated_task
    raise HTTPException(status_code=404, detail='Task not found')


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    task_id -= 1
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
        return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail='Task not found')
