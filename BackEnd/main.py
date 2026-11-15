from fastapi import FastAPI
import uvicorn
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

if __name__ == "__main_cd _":
    uvicorn.run("main:klu", host="127.0.0.1", port=2027, reload=True)
        