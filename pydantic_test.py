# python trend는 데이터타입 검사를 강하게 하는 추세... pydantic

from pydantic import BaseModel

# class User(BaseModel):  # 타입 강건한 모델로 만든다
#     def __init__(self,id:int,name:str) -> None: # pydandic의 타입검사, 자동파싱 기능을깨버림       
#         self.id = id
#         self.name   = name 


class User(BaseModel):
    id:int
    name:str


def main():
    u1 = User(id=1.5, name='홍길동')    
    print(u1.id, u1.name)

if __name__ =='__main__':
    main()
