from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from evento_online import EventoOnline

ev1 = EventoOnline("Live de Python")
ev2 = EventoOnline("Live de Javascript")
ev3 = EventoOnline("Live dos Paranauê")
eventos = [ev1, ev2, ev3]

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('👻')

        if self.path == '/':
            data = f"""
                <html>
                    <head>
                        <title>😀</title>
                    </head>
                    <body>
                        <section>
                            <div>
                                😀 Olá from {self.path}
                            </div>
                        </section>
                    </body>
                <html>
            """.encode()
        

            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('X-TESTE', 'teste')
            self.end_headers()
            self.wfile.write(data)
        elif self.path == '/eventos':
            css = """
                <style>
                    table {
                        border-collapse: collapse;
                    }
                    table th:first-of-type {
                        width: 10%;
                    }
                    table th:nth-of-type(2) {
                        width: 10%;
                    }
                    table th:nth-of-type(3) {
                        width: 50%;
                    }
                    table th:nth-of-type(4) {
                        width: 30%;
                    }
                    td {
                        text-align: center;
                        border: 1px solid #3e3e3e40
                    }
                </style>
            """
            tbody_content_eventos = ''

            for ev in eventos:
                tbody_content_eventos += f"""
                    <tr>
                        <td>{ev.id}</td><td>{ev.nome}</td><td>{ev.local}</td>
                    </tr>\n
                """
            data = f"""
                <html>
                    <head>
                        <title>Eventos</title>
                    </head>
                    <body>
                        {css}
                        <section>
                            <div style="display:flex; flex-direction: column; align-items:center; justify-content:center">
                                <table>
                                    <thead>
                                        <tr>
                                            <th>ID</th><th>Nome</th><th>Link</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {tbody_content_eventos}
                                    </tbody>
                                </table>
                            </div>
                        </section>
                    </body>
                <html>
            """.encode()

            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(data)
        elif self.path == '/api/eventos':
            lista_dict_eventos = []
            for ev in eventos:
                lista_dict_eventos.append({
                    "id": ev.id,
                    "nome": ev.nome,
                    "local": ev.local
                })

            data = json.dumps(lista_dict_eventos).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(data)
            
server = HTTPServer(('localhost', 8000), SimpleHandler)
server.serve_forever()