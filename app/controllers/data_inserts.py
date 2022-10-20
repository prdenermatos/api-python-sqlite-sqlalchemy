
from operator import index
from flask import Flask, render_template, redirect, request, Response, json
from app import app, db
from app.models.tables import data
from app.models.dataMocado import DataMocado

#dados mocados
dataSetMocado = DataMocado.dataSetMocado

@app.route('/')
@app.route('/documentation')
def documentation():
    return 'Documentação API - DNA Empresarial'

@app.route('/insert-data', methods=["POST"])
def insert_data():
    index_finish_data =  dataSetMocado.index(dataSetMocado[-1])
    body = request.json
    body["id"] = index_finish_data + 3
    dataSetMocado.append(body)
    
    return body


