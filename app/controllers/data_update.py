from urllib import request
from flask import Flask, make_response, jsonify
from app import app, db
from app.models.tables import data
from app.models.dataMocado import DataMocado

#dados mocados
dataSetMocado = DataMocado.dataSetMocado


@app.route('/data-update/<int:id>', methods= ["PUT"])
def data_update(id: int):
    try:
        body = request.json
        dataSetMocado[id-1] = body
        return make_response(jsonify(dataSetMocado[id-1])) 
    except:
        return make_response(jsonify({
            "bad_request": f" ID {id} não encontrado para atualização"
        }))
