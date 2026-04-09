from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import wikipedia

app = FastAPI()

wikipedia.set_lang("ru") 

class pattern(BaseModel):
    title: str
    summary: str
    url: str 

@app.get("/name/{name}", response_model = pattern)
def get_summary(name: str):
    page = wikipedia.page(name)  
    summary = wikipedia.summary(name, sentences = 4)
    return pattern(
            title = page.title,
            summary = summary,
            url = page.url
    )

@app.get("/name_query", response_model = pattern)
def get_summary(name: str):
    page = wikipedia.page(name)  
    summary = wikipedia.summary(name, sentences = 4)
    return pattern(
            title = page.title,
            summary = summary,
            url = page.url
    )

class request(BaseModel):
    name: str = Field(..., min_length = 1, description = "Название статьи Wikipedia")

@app.post("/articale", response_model = pattern, status_code = 201)
def get_article_by_post(request: request):
    name = request.name
    page = wikipedia.page(name)
    summary = wikipedia.summary(name, sentences = 4)
    return pattern(
        title = page.title, 
        summary = summary, 
        url = page.url
    )


