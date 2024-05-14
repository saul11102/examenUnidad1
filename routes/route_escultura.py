from flask import Blueprint, jsonify, make_response, request
from flask_expects_json import expects_json
from control.control_escultura import EsculturaControl
from routes.schemas.schema_escultura import save_escultura, modify_state
from control.utils.errors import Errors
from control.Authenticate import token_required
from control.control_escultura import EsculturaControl

api_escultura = Blueprint('api_escultura_escultura', __name__)

esculturaC = EsculturaControl()


@api_escultura.route('/escultura')
@token_required
def home():
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "datos" : ([i.serialize for i in esculturaC.listar()])}), 
        200
    )


@api_escultura.route('/escultura/guardar/<external_id_persona>'   , methods = ["POST"])
@token_required
@expects_json(save_escultura)
def guardar_escultura(external_id_persona):
    data = request.json 
    id = esculturaC.guardarEscultura(external_id_persona, data = data)
    if(id >= 0):
        return make_response(
                jsonify({"msg" : "OK", "code" : 200, "datos" : {"tag" : "datos guardados"}}), 
                200
        )
    else:
        return make_response(
                jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Errors.error[str(id)]}}), 
                400
    )

@api_escultura.route('/escultura/modificar/<external_id_persona>'   , methods = ["POST"])
@token_required
@expects_json(save_escultura)
def modificar_escultura(external_id_persona):
    data = request.json 
    id = esculturaC.modificarEscultura(external_id_persona, data = data)
    if(id >= 0):
        return make_response(
                jsonify({"msg" : "OK", "code" : 200, "datos" : {"tag" : "datos guardados"}}), 
                200
        )
    else:
        return make_response(
                jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Errors.error[str(id)]}}), 
                400
    )

@api_escultura.route('/escultura/cambiar/estado/<external_id_persona>'   , methods = ["POST"])
@token_required
@expects_json(modify_state)
def cambiar_estado_escultura(external_id_persona):
    data = request.json 
    id = esculturaC.cambiarEstadoEscultura(external_id_persona, data)
    if(id >= 0):
        return make_response(
                jsonify({"msg" : "OK", "code" : 200, "datos" : {"tag" : "datos guardados"}}), 
                200
        )
    else:
        return make_response(
                jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Errors.error[str(id)]}}), 
                400
    )