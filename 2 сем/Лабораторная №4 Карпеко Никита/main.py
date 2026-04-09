from fastapi import FastAPI, Path, Query, HTTPException
import pyjokes
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/", status_code=200) 
def joke():
    return pyjokes.get_joke()

@app.get("/friend/{friend}", status_code=200)
def friends_joke(friend: str = Path(..., min_length=2)):
    return friend + " tells his joke:" + pyjokes.get_joke()

@app.get("/multi/{friend}", status_code=200)
def multi_friends_joke(
    friend: str = Path(..., min_length=2),          
    jokes_number: int = Query(...)                  
):
    if jokes_number < 1 or jokes_number > 10:
        raise HTTPException(
            status_code=400,
            detail=f"Parameter 'jokes_number' must be between 1 and 10. You provided {jokes_number}."
        )
    
    result = ""
    for i in range(jokes_number):
        result += friend + f" tells his joke #{i + 1}: " + pyjokes.get_joke() + " "
    return result

class Joke(BaseModel): 
    friend: str
    joke: str

class JokeInput(BaseModel): 
    friend: str = Field(..., min_length=2)

@app.post("/", response_model=Joke, status_code=201) 
def create_joke(joke_input: JokeInput):
    """Создание шутки"""
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke())


#для задания 4

# Path те URL
@app.get("/joke-path/{friend}", status_code=200)
def joke_by_path(friend: str):
    return f"{friend} says with path: {pyjokes.get_joke()}"

# Query те ?*
@app.get("/joke-query", status_code=200)
def joke_by_query(friend: str):
    return f"{friend} says with query: {pyjokes.get_joke()}"