from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import re


app = FastAPI()

class response_schema(BaseModel):
    slackUsername : str
    backend: bool
    age : int
    bio: str

class arithemetic_schema(BaseModel):
    operation_type : str
    x : Optional[int] = None 
    y : Optional[int] = None  

    

class arithemetic_response(BaseModel):
    slackUsername: str
    operation_type: str
    result : int


@app.get('/', response_model=response_schema)
def request():
    return {"slackUsername": "shakzy", "backend": True, "age": 19, "bio": "I am a Software Engineer, with a love for Problem Solving and Building Thngs"}

@app.post('/operation')
def arithemetic(operation:arithemetic_schema):
    add = ["add", "addition", "+"]
    sub = ["subtract", "sub", "subtraction", "-", "minus", "reduce"]
    multiply = ["multiply", "product", "x", "*" , ""]
    find_number = [int(x) for x in re.findall(r'\d+', operation.operation_type)]
    operation_type = operation.operation_type
    x = operation.x
    y = operation.y 
    if x and y == None and find_number == []:
        return {'message': 'You need to input integers for operation or define your operation properly'}
    if operation_type in add:
        result =  x + y
        return {"slackUsername": "shakzy", "operation" : operation_type, "result":result }
    if operation_type in sub:
        result = x - y
        return {"slackUsername": "shakzy", "operation" : operation_type, "result":result }
    if operation_type in multiply:
        result = x*y
        return {"slackUsername": "shakzy", "operation" : operation_type, "result":result }
    elif x or y == None:
        if find_number == []:
            return {'message' : 'Invalid Operation'}
        for i in operation_type.split():
            if i in add:
                result = find_number[0] + find_number[1]
                operation_type = "addition"
                return {"slackUsername": "shakzy", "operation" : operation_type, "result":result }
            if i in sub:
                result = find_number[0] - find_number[1]
                operation_type = "substraction"
                return {"slackUsername": "shakzy", "operation" : operation_type, "result":result }
            if i in multiply:
                result = find_number[0] * find_number[1]
                operation_type = "multiplication"
                return {"slackUsername": "shakzy", "operation" : operation_type, "result":result }