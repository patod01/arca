import sys
from bottle import error, route, run, static_file, template, request, response


### Real sh1t ###
@route('/a.js')
def staticjs():
     return static_file('/a.js', root='.')

@route('/')
def index():
     return template('index.html', listado=listado_to_json(listado))


listado = [
     {
          "nombre": 'a cosa1',
          "is_ready": False,
          "hora": 0,
     },
     {
          "nombre": '1313 y como la mia',
          "is_ready": False,
          "hora": 0,
     },
     {
          "nombre": 'cosa3',
          "is_ready": False,
          "hora": 0,
     },
     {
          "nombre": 'cosa4',
          "is_ready": False,
          "hora": 0,
     }
]

def listado_to_json(cosa):
     for i, item in enumerate(cosa):
          cosa[i] = {
               "nombre": cosa[i]['nombre'],
               "is_ready": str(cosa[i]['is_ready']).lower(),
               "hora": str(cosa[i]['hora']),
          }
     return str(cosa)


### API ###

### # ###

if __name__ == '__main__':
     if len(sys.argv) != 3: raise Exception('EXPLODE')
     print(f'Running in {sys.argv[1]} mode on port {sys.argv[2]}...')
     if sys.argv[1] == 'dev':
          run(host='0.0.0.0', port=int(sys.argv[2]), debug=True, reloader=True)
     if sys.argv[1] == 'FTW':
          run(host='0.0.0.0', port=int(sys.argv[2]))

#ned
