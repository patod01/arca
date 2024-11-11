import sys, json, os, random, time, math
from bottle import (
     error,
     redirect,
     request,
     response,
     route,
     run,
     static_file,
     template,
)


### Config ###
def config(module_path):
     global DATABASE_PATH, MODULE_PATH, last_edit, notepad
     MODULE_PATH = module_path
     DATABASE_PATH = '.' + MODULE_PATH + '/db.json'

     if os.path.isfile(DATABASE_PATH):
          with open(DATABASE_PATH) as DB:
               notepad = json.load(DB)
     else:
          notepad = {}

     last_edit = now()

def now():
     return math.floor(time.time())


### Real sh1t ###
@error(404)
def go_default(error):
     return 'notmyproblem .!.'

@route('/')
def index():
     return template('.' + MODULE_PATH + '/index.html', module_path=MODULE_PATH)

@route('/static/<file:path>')
def static(file):
     return static_file(file, root='.'+MODULE_PATH+'/static')

@route('/list/<id_lista:int>')
def kart(id_lista):
     if str(id_lista) not in notepad.keys():
          return redirect('/error')
     else:
          return template(
               '.' + MODULE_PATH + '/kart.html',
               module_path=MODULE_PATH,
               id_lista=id_lista,
               listado=json.dumps(notepad[str(id_lista)]).replace('"', "'"),
               last_server_edit=last_edit
          )


### API ###
@route('/backup', method=['POST'])
def backup():
     global last_edit; last_edit = now()
     # list_id = str(request.json['id_lista'])
     # lista_db = notepad[list_id]
     # lista_web = request.json['listado']
     # for i, item in enumerate(lista_web):
     #      if lista_db[i] != item:
     #           print('cambio')
     #           lista_db[i] = item
     #      else:
     #           print('ok')

     notepad[str(request.json['id_lista'])] = request.json['listado']
     with open(DATABASE_PATH, 'w') as DB:
          json.dump(notepad, DB)
     return 'listado actualizado'

@route('/new_list', method=['POST'])
def new_list():
     umin = 1000
     umax = 1003
     while ...:
          list_id = str(random.randint(umin, umax))
          if list_id not in notepad.keys():
               notepad[list_id] = []
               print(notepad)
               return list_id
          elif len(notepad) == umax - umin + 1:
               return 'fuku'

@route('/check_list', method=['GET'])
def check_list():
     if request.query.id in notepad.keys():
          return 'encontrada'
     else:
          return 'inexistente'

@route('/last_edit', 'GET')
def last_edit():
     return str(last_edit)


### # ###
if __name__ == '__main__':
     config('')
     if len(sys.argv) != 3: raise Exception('EXPLODE')
     print(f'Running in {sys.argv[1]} mode on port {sys.argv[2]}...')
     if sys.argv[1] == 'dev':
          run(host='0.0.0.0', port=int(sys.argv[2]), debug=True, reloader=True)
     if sys.argv[1] == 'FTW':
          run(host='0.0.0.0', port=int(sys.argv[2]))
else:
     config('/kart')

#ned
