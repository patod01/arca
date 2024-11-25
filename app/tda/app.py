import sys
from bottle import (
     error,
     request,
     response,
     route,
     run,
     static_file,
     template,
)


### settings ###
def config(module_path):
     global MODULE_PATH, The_House, jugadores
     The_House = {"stakes": 0, "The Hole": 0}
     jugadores = {}
     MODULE_PATH = module_path


### Real sh1t ###
@error(404)
def go_default(error):
     return 'notmyproblem .!.'

@route('/')
def landing():
     return template('.' + MODULE_PATH + '/index.html', module_path=MODULE_PATH)

@route('/a.js')
def staticjs():
     return static_file('/a.js', root='.'+MODULE_PATH+'/')

@route('/registre')
def registar():
     return template('.' + MODULE_PATH + '/registre.html', module_path=MODULE_PATH)

@route('/tablon')
def tablon():
     return template(
          '.' + MODULE_PATH + '/tablon.html',
          module_path=MODULE_PATH,
          jugadores=jugadores,
          stakes=The_House['stakes'],
          hole=The_House['The Hole']
     )

@route('/tabla/<jugador>')
def tabla(jugador):
     return template(
          '.' + MODULE_PATH + '/tabla.html',
          module_path=MODULE_PATH,
          jugadores=list(filter(lambda x: x != jugador, jugadores.keys())),
          jugador=jugador,
          gold=jugadores[jugador]['gold'],
          debt=jugadores[jugador]['debt'],
          stakes=The_House['stakes'],
          hole=The_House['The Hole']
     )


### APIs ###
@route('/registre_players', method=['POST'])
def registre_players():
     print((request.json))
     global The_House, jugadores
     The_House = {"stakes": 0, "The Hole": 0}
     jugadores = {}
     for player in request.json['players']:
          jugadores[player] = {
               "gold": int(request.json['gold']/len(request.json['players'])),
               "debt": 0
          }
     for player in jugadores: print(f'{player}: {jugadores[player]}')
     return 'jugadores actualizados'

@route('/send_coins', method=['POST'])
def send_coins():
     global The_House, jugadores
     mode = request.json['mode']
     amount_of_gold = request.json['amount_of_gold']
     abuse = request.json['abuse']
     from_player = request.json['from_player']
     to_player = request.json['to_player']

     if mode == 'give to a player':
          if to_player not in jugadores.keys(): return 'wtf u sckr'
          jugadores[from_player]['gold']-=amount_of_gold+abuse
          jugadores[from_player]['debt']-=abuse
          jugadores[to_player]['gold']+=amount_of_gold+abuse
     elif mode == 'pay to stakes':
          jugadores[from_player]['gold']-=amount_of_gold+abuse
          jugadores[from_player]['debt']-=abuse
          The_House['stakes']+=amount_of_gold+abuse
     elif mode == 'steal from stakes':
          The_House['stakes']-=amount_of_gold
          jugadores[from_player]['gold']+=amount_of_gold

     return 'cartera actualizada!'

@route('/claim_staked', method=['POST'])
def claim_staked():
     global The_House, jugadores
     game_finished = False
     player = request.json['player']
     jugadores[player]['gold']+=The_House['stakes']
     The_House['stakes'] = 0
     for player in jugadores.keys():
          balance = jugadores[player]['gold'] - jugadores[player]['debt']
          if balance < 0:
               The_House['The Hole']+=jugadores[player]['gold']
               game_finished = True
          else:
               The_House['The Hole']+=jugadores[player]['debt']
          jugadores[player]['gold']-=jugadores[player]['debt']
          jugadores[player]['debt'] = 0
     return ' '.join(f'gambit {"and game" if game_finished else ""} finished!'.split())


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
     config('/tda')

#ned
