from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 라우터
@app.get("/hello")
def say_hello(name:str,age:int):
    return {"message":f'hello {name}! age {age}'}

@app.get("/board")
def showBoard():
    return {"body":f'게시판을 보여주는 화면 입니다.'}


# 포스트 방식은 data body 필요 --> From 
class Item(BaseModel):
    name : str
    price : float
    is_offer : bool = False #할인여부

@app.post('/items/')
def create_item(item:Item):
    return {'received_item' : item}