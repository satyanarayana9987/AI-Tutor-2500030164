from fastapi import FastAPI

klu = FastAPI(title="AI-Tutor",
              description ="AI Tutor Pbl Project",
              version="1.0.0")


@klu.get("/")
def home():
    return {"message":"welcome to AI Tutor Project"}

@klu.get("/demo")
def demo():
    return {"message":"KLUNIVERSITY"}

@klu.get("/askquestion")
def ask():
    return{"message":"what is LLm","Answer":"large language Model"}

@klu.get("/emp")
def emp():
    return{"id":"1","name":"satya","gender":"male","course":"DSA"}

@klu.get("/students")
def getstudents():
    return[{"id":"1","name":"satya","gender":"male","course":"DSA"},
           {"id":"1","name":"teja","gender":"male","course":"DSA"},
           {"id":"1","name":"sameer","gender":"male","course":"DSA"}
           ]

        