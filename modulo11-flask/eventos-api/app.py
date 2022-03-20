from http import HTTPStatus
import json
from flask import Flask, jsonify, abort, make_response, request
from evento import Evento
from evento_online import EventoOnline

app = Flask(__name__)
# app.config['TRAP_HTTP_EXCEPTIONS']=True

ev1 = Evento("Aula de Python")
ev1.imprime_informacaoes()
ev2 = Evento("Aula de Javascript", "Florianópolis")
ev2.imprime_informacaoes()

ev1_online = EventoOnline("Live de Python")
ev1_online.imprime_informacaoes()

ev2_online = EventoOnline("Live de Javascript")
ev2_online.imprime_informacaoes()

eventos = [ev1, ev2, ev1_online, ev2_online]

find = lambda func, elements: next((element for element in elements if func(element)), None)
findall = lambda func, elements: [element for element in elements if func(element)]


@app.route("/")
def index():
    return "<h1>Flask successfully installed! 😎</h1>"

@app.route("/api/eventos/")
def listar_eventos():
    eventos_dict = []

    for ev in eventos:
        eventos_dict.append(ev.__dict__)

    return jsonify(eventos_dict)
    
# @app.route("/api/eventos/<int:id>/")
# def detalhar_evento(id):
#     for ev in eventos:
#         if ev.id == id:
#             return jsonify(ev.__dict__)

@app.errorhandler(HTTPStatus.NOT_FOUND)
def not_found(error_msg):
    return (jsonify(error=str(error_msg)), HTTPStatus.NOT_FOUND)

@app.errorhandler(HTTPStatus.BAD_REQUEST)
def not_found(error_msg):
    return (jsonify(error=str(error_msg)), HTTPStatus.BAD_REQUEST)

# @app.errorhandler(Exception)
# def handle_error(e):
#     try:
#         error_msg = "teste"
#         if e.code == HTTPStatus.NOT_FOUND:
#             return (jsonify(error=str(error_msg)), HTTPStatus.NOT_FOUND)
#         elif e.code == HTTPStatus.BAD_REQUEST:
#             return (jsonify(error=str(error_msg)), HTTPStatus.BAD_REQUEST)
#         raise e
#     except:
#         return (jsonify(error="Something went wrong"), HTTPStatus.INTERNAL_SERVER_ERROR)

@app.route("/api/eventos/<int:id>/")
def detalhar_evento(id):
    try:
        evento = find(lambda ev: ev.id == id, eventos)

        return jsonify(evento.__dict__)
    except AttributeError:
        abort(HTTPStatus.NOT_FOUND, f"Event id {id} not found!")
        
        # Como definimos o @app.errorhandler(404) podemos deixas apenas o abort, pois o Flask cuida dessas execeções e quando for um erro 404 irá passar pela função que definimos em @app.errorhandler(404)
        # data = { "error": f"Event id {id} not found!" }
        # return make_response(jsonify(data), HTTPStatus.NOT_FOUND)

@app.route("/api/eventos/", methods=["POST"])
def criar_evento():
    data = json.loads(request.data)
    nome = data.get("nome")
    local = data.get("local")

    if not nome:
        abort(HTTPStatus.BAD_REQUEST, "Property 'nome' is required!")

    if local:
        evento = Evento(nome=nome, local=local)
    else:
        evento = EventoOnline(nome=nome)

    eventos.append(evento)
    
    return {
        "id": evento.id,
        "url": f"/api/eventos/{evento.id}"
    }
    
@app.route("/api/eventos/<int:id>", methods=["DELETE"])
def deletar_evento(id):
    try:
        evento = find(lambda ev: ev.id == id, eventos)
        
        if not evento:
            abort(HTTPStatus.NOT_FOUND, f"Event id {id} not found!")
        
        eventos.remove(evento)

        return jsonify({
            "id":id,
            "message": "Evento successfully deleted"
        })
    except AttributeError:
        abort(HTTPStatus.NOT_FOUND, f"Event id {id} not found!")