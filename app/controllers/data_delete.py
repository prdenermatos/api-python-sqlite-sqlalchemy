
from flask import Flask, render_template, redirect, request, make_response, jsonify
from app import app, db
from app.models.tables import data
from app.models.dataMocado import DataMocado

#dados mocados
dataSetMocado = DataMocado.dataSetMocado


@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id: int):
    try: 
        del dataSetMocado[id-1]
        return make_response(jsonify( {"sucess": f"Registro com ID {id} deletado"}))
    except:
        return make_response(jsonify({
                "error": f"Não foi possível deletar o dado referente ao ID {id}"
                }))
    
