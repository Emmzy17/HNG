from urllib import response
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class response_schema(BaseModel):
    slackUsername : str
    backend: bool
    age : int
    bio: str


@app.get('/', response_model=response_schema)
def request():
    return {"slackUsername": "shakzy", "backend": True, "age": 19, "bio": "I am a Software Engineer, with a love for Problem Solving and Building Thngs"}