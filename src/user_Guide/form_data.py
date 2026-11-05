# When I need to receive from fields instead of JSON, I can use Form

from typing import Annotated, Literal
from fastapi import FastAPI, Form, status
from pydantic import BaseModel

app = FastAPI()

@app.post("/login/", status_code=status.HTTP_201_CREATED)
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()], subscribe: Annotated[bool, Form()] = False):
     return {"username":username, "password":password, "subscribe":subscribe}

# Pydantic Models for Forms - I just need to declare a Pydantic model with the fields  want to receive as form fields, and then declare the parameter as Form

class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"} # forbid any extra fields

@app.post("/loginAsFormData/")
async def login_as_form_data(data: Annotated[FormData, Form()]):
     return data 

# Combine Form Models

class Profile(BaseModel):
    name: str
    age: str
    
class Preferences(BaseModel):
     tags:list[str]=[]


@app.post("/profiles/")
async def create_profile(
    profile: Annotated[Profile, Form()],
    preference:Annotated[Preferences, Form()],
    token: Annotated[str | None, Form()] = None
):
    return {"profile":profile, "preference": preference, "token": token}

# Combine Unions of Form Models

class Person(BaseModel):
    contact_type: Literal["person"]
    name: str


class Company(BaseModel):
    contact_type: Literal["company"]
    company_name: str


class Email(BaseModel):
    notification_type: Literal["email"]
    email: str


class SMS(BaseModel):
    notification_type: Literal["sms"]
    phone: str

@app.post("/contacts/")
async def create_contact(
    contact: Annotated[Person | Company, Form(discriminator="contact_type")],
    token: Annotated[str, Form()],
    notification: Annotated[
        Email | SMS | None, Form(discriminator="notification_type")
    ] = None,
):
    return {"contact": contact, "notification": notification, "token": token}