import sys, json, os, random
from bottle import error, route, run, static_file, template, request, response


### Config ###
DATABASE = 'db.json'

if os.path.isfile(DATABASE):
     with open(DATABASE) as DB:
          listado = json.load(DB)
else:
     listado = {}


### Real sh1t ###
@route('/')
def index():
     return static_file('index.html', root='.')

@route('/static/<file:path>')
def static(file):
     return static_file(file, root='./static')

@route('/kart')
def kart():
     return template('kart.html', listado=listado_to_json(listado))

def listado_to_json(cosa):
     for i, item in enumerate(cosa):
          cosa[i] = {
               "nombre": cosa[i]['nombre'],
               "is_ready": str(cosa[i]['is_ready']).lower(),
               "hora": cosa[i]['hora'],
          }
     return str(cosa)


### API ###
@route('/backup', method=['POST'])
def backup():
     print((request.json))
     print(type(request.json))
     global listado
     listado = request.json
     with open(DATABASE, 'w') as DB:
          json.dump(listado, DB)
     return 'listado actualizado'

@route('/new_list', method=['POST'])
def new_list():
     keep_running = True
     while keep_running:
          list_id = str(random.randint(1000, 9999))
          if list_id not in listado.keys():
               listado[list_id] = []
               keep_running = not keep_running
     print(listado)
     return list_id

@route('/check_list', method=['GET'])
def check_list():
     if request.query.id in listado.keys():
          return 'encontrada'
     else:
          return 'inexistente'
### # ###

if __name__ == '__main__':
     if len(sys.argv) != 3: raise Exception('EXPLODE')
     print(f'Running in {sys.argv[1]} mode on port {sys.argv[2]}...')
     if sys.argv[1] == 'dev':
          run(host='0.0.0.0', port=int(sys.argv[2]), debug=True, reloader=True)
     if sys.argv[1] == 'FTW':
          run(host='0.0.0.0', port=int(sys.argv[2]))

#ned
