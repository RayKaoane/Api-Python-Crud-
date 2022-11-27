from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import date




app = FastAPI()



class Fila(BaseModel):
    id: Optional [int] = 0
    nome: str = Field (max_length=20)
    prioridade: str = Field (max_length=1)
    posicao:Optional [int] = 0
    data: date
    atendido: Optional [bool] = False

db_fila = [
    Fila(id=1,nome="Rayara",prioridade="N",chegada="",posicao=1,data='2022-05-22',atendido=False) 

]


    

@app.get("/fila")
def listar():
    return {"Fila": db_fila}
 
@app.get("/fila/{id}")
def posicao_cliente(id:int):
    if [fila for fila in db_fila if fila.id==id] == []:
        raise HTTPException(status_code=404, detail="Não existe cliente nessa posição")
    return{"Fila": [fila for fila in db_fila if fila.id==id]}

@app.post("/fila/")
async def criar_fila(fila: Fila):
    if fila.prioridade == 'N'  or  fila.prioridade == 'P':
        fila.id = db_fila[-1].id + 1
        fila.posicao = db_fila[-1].id + 1
        fila.atendido = False
        db_fila.append(fila)
    else:
        raise HTTPException(status_code=404, detail="Prioridade aceita apenas P:Prioridade ou N:Normal")



@app.patch("/fila/{id}/")
def update_fila(id:int, fila:Fila):
    index = [index for index, fila in enumerate(db_fila) if fila.id == id]
    if fila.atendido == True:
        fila.posicao = 0
        #for fila.posicao in db_fila:
            #fila.posicao = db_fila[-1].id + 1
    fila.id = db_fila[index[0]].id
    db_fila[index[0]] = fila
    return{"mensagem" : "Atualizado"}

@app.delete("/fila/{id}")
def deletar_fila(id:int):
    fila = [fila for fila in db_fila if fila.id ==id]
    db_fila.remove(fila[0])
    return()










