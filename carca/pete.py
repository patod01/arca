import sys
from bottle import error, route, run, static_file, template, request, response


### Default settings ###
@error(404)
def go_default(error):
     return 'notmyproblem .!.'


### Real sh1t ###
@route('/a.js')
def staticjs():
     return static_file('/a.js', root='.')

@route('/')
def landing():
     return static_file('index.html', root='.')

@route('/registre')
def registar():
     return static_file('registre.html', root='.')

@route('/tablon')
def tablon():
     return template('tablon.html', jugadores=jugadores)


### API ###
@route('/registre_players', method=['POST'])
def registre_players():
     print((request.json))
     global jugadores
     jugadores = {}
     for player in request.json:
          jugadores[player] = [0]*9
     for jugador in jugadores: print(f'{jugador}: {jugadores[jugador]}')
     return 'jugadores actualizados'

@route('/save_points/<player>', method=['PUT'])
def save_points(player):
     print(request.json)
     global jugadores
     if player not in request.json.keys():
          return 'fial con los puntos'
     jugadores[player] = request.json[player]
     for jugador in jugadores: print(f'{jugador}: {jugadores[jugador]}')
     return 'jugadores actualizados'


### # ###
jugadores = {
     "patox1": [1,2,3,4,5,3,7],
     "patox2": [1,2,1,4,5,6,7],
     "patox3": [1,2,3,4,5,6,7],
     "patox4": [1,2,3,4,15,6,7],
     "patox5": [1,2,3,0,5,6,7],
}


if __name__ == '__main__':
     if len(sys.argv) != 3: raise Exception('EXPLODE')
     print(f'Running in {sys.argv[1]} mode on port {sys.argv[2]}...')
     if sys.argv[1] == 'dev':
          run(host='0.0.0.0', port=int(sys.argv[2]), debug=True, reloader=True)
     if sys.argv[1] == 'FTW':
          run(host='0.0.0.0', port=int(sys.argv[2]))

#ned
