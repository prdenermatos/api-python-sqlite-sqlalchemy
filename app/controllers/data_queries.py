from flask import Flask, make_response, jsonify, request
from app import app, db
from app.models.tables import data
from app.models.dataMocado import DataMocado


#dados mocados
dataSetMocado = DataMocado.dataSetMocado


@app.route("/find-all/", methods=["GET"])
def find_all():
    return make_response(jsonify(dataSetMocado))



@app.route("/find-one/<int:id>", methods=["GET"])
def find_one(id):
    try:
        return make_response(jsonify(dataSetMocado[id-1])) 
    except:

        return make_response(jsonify({
            "bad_request": f"Não foram encontrados dados para o ID {id}"
        }))

@app.route("/filter", methods=["GET"])
def filter():
    body = request.json
    return body



 