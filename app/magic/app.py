import sys, json, os, random
from bottle import (
     abort,
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
def get_db(*, at='', default='explode'):
     if not at:
          raise Exception('EXPLODED. It cant be empty')
     if os.path.isfile(at):
          with open(at) as DB:
               DB = json.load(DB)
          return DB
     else:
          if default:
               raise Exception('EXPLODED. `default` must be `[]` or `{}`')
          with open(at, 'w') as DB:
               json.dump(default, DB, indent=2)
          return default


def config(module_path):
     global MODULE_PATH, MAGIC_DB_PATH, USER_DB_PATH, magicarp, pokedex, SECRET
     MODULE_PATH = module_path
     conf_file = '.' + MODULE_PATH + '/conf.json'

     if os.path.isfile(conf_file):
          with open(conf_file) as settings:
               settings = json.load(settings)
     else:
          settings = {
               "links_db": '',
               "users_db": '',
               "secret": ''
          }
          with open(conf_file, 'w') as temp:
               json.dump(settings, temp, indent=5)

     for key in settings:
          print('config:', settings[key])
          if not os.path.isfile('.' + MODULE_PATH + '/' + settings[key]):
               raise Exception(f'Config file not filled correctly at `{key}`')

     MAGIC_DB_PATH = '.' + MODULE_PATH + '/magicarp.json'
     USER_DB_PATH = '.' + MODULE_PATH + '/pokedex.json'

     with open('.' + MODULE_PATH + '/secret.txt') as file:
          SECRET = file.read().strip()

     magicarp = get_db(at=MAGIC_DB_PATH, default={})
     pokedex = get_db(at=USER_DB_PATH, default=[])


### Real sh1t ###
@error(404)
def go_default(error):
     return 'wholesome pete'

@route('/')
def index():
     magic_link = request.query.link
     pokemon = request.get_cookie(
          'magicpass',
          # secret=SECRET
     )

     global magicarp, pokedex
     magicarp = get_db(at=MAGIC_DB_PATH)
     pokedex = get_db(at=USER_DB_PATH)

     if magic_link not in magicarp.keys():
          return 'wholesome pete'

     match (
          magicarp[magic_link]['vigente'],
          magicarp[magic_link]['usos'] < magicarp[magic_link]['limite'],
          magicarp[magic_link]['limite'] == 0
     ):
          case (1,1,0) | (1,0,1):
               if pokemon and pokemon in pokedex:
                    contenido = 'estas OK!'
               else:
                    contenido = 'no tenias cookie pero ahora si jaja salu3'

                    while ...: # Registro de usuario
                         pokemon = '0' if not pokemon else str(int(pokemon) + 1) # get this randomly
                         if pokemon not in pokedex:
                              pokedex.append(pokemon)
                              break

                    magicarp[magic_link]['usos']+=1

                    with open(MAGIC_DB_PATH, 'w') as DB:
                         json.dump(magicarp, DB, indent=2)

                    with open(USER_DB_PATH, 'w') as DB:
                         json.dump(pokedex, DB, indent=2)

                    response.set_cookie(
                         'magicpass',
                         pokemon,
                         # secret=SECRET,
                         max_age=5270400,
                         httponly=True,
                         samesite='strict'
                    )
               return template(
                    '.' + MODULE_PATH + '/index.html',
                    module_path=MODULE_PATH,
                    contenido=contenido
               )
     return 'wholesome pete'


### API ###
@route('/gyaradont', method=['PUT'])
def gyaradont():
     magic_link = request.query.link
     if magic_link in magicarp.keys():
          magicarp[magic_link]['vigente'] = False
          with open(MAGIC_DB_PATH, 'w') as DB:
               json.dump(magicarp, DB, indent=2)
          return 'eliminadous'
     else:
          return 'pete'


### export Utility ###
def verify_user():
     if request.path == MODULE_PATH:
          print('ulala')
     elif not request.get_cookie('magicpass') in get_db(at=USER_DB_PATH):
          print('chino cochino')
          abort(404)


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
     config('/magic')

#ned
