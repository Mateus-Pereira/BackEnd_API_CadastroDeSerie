"""fazendo os import"""
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Serie
from src.infra.sql.config.database import get_db, criar_bd
from src.infra.sql.repositorios.series import RepositorioSerie

"""Criar a Base de Dados :]"""
criar_bd()

"""Iniciando o App"""
app = FastAPI()

"""Crando as rotas"""
@app.post("/series")
def criar_series(serie: Serie, db: Session = Depends(get_db)):
    serie_criado = RepositorioSerie(db).criar(serie)
    return serie
    
@app.get('/series')
def lista_serie(db: Session = Depends(get_db)):
    return RepositorioSerie(db).listar()

@app.get('/series/{serie_id}')
def obter_serie(serie_id: int, db: Session = Depends(get_db)):
    serie = RepositorioSerie(db).obter(serie_id)
    return serie

@app.delete('/series/{serie_id}')
def obter_serie(serie_id: int, db: Session = Depends(get_db)):
    RepositorioSerie(db).remover(serie_id)
    return{"Mensagem":"Serie foi Removida com Sucesso"}