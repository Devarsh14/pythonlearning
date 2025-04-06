from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List,Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
# this will create tables in PostgreSQL database
models.Base.metadata.create_all(bind=engine)

# debug configuration
#https://www.jetbrains.com/help/pycharm/fastapi-project.html#run-debug-configuration
# https://fastapi.tiangolo.com/tutorial/debugging/#about-__name__-__main__

@app.get("/")
async def root():
    number = 5 + 7
    return {"message": f"Hello World{number}"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

# create dictionary of books with title as key for faster lookup
BOOKS_DICT = {book['title']: book for book in BOOKS}
@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/title/{title}")
async def get_book_by_title(title:str):
    for book in BOOKS:
        if book["title"].lower() == title.lower():
            return book
    return {"error": "Book not found"}



class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_depend = Annotated[Session, Depends(get_db)]

@app.post("/questions/")
async def create_question(question: QuestionBase, db: db_depend):
    db_question = models.Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    for choice in question.choices:
        db_choice = models.Choices(
            choice_text=choice.choice_text,
            is_correct=choice.is_correct,
            question_id=db_question.id
        )
        db.add(db_choice)

    db.commit()
    return {"question": db_question, "choices": question.choices}


