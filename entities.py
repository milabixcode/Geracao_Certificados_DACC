from pydantic import BaseModel

class Event(BaseModel):
    name: str
    # e.g. 2022
    year: str

class Activity(BaseModel):
    name: str
    event: Event
    kind: str
    hours_granted: float

class Student(BaseModel):
    name: str
    # AKA matricula
    registration: str

class Certificate(BaseModel):
    student: Student
    activity: Activity
