import sys, json, os
from bottle import Bottle, static_file

app = Bottle()

tapp = Bottle()
with tapp: from magic import app as module
app.mount('/magic', tapp)
app.add_hook('before_request', module.verify_user)

tapp = Bottle()
with tapp: from kart import app as module
app.mount('/kart', tapp)

### Real sh1t ###
@app.error(404)
def go_default(error):
     return 'notmyproblem .!.'

@app.route('/')
def index():
     return static_file('arca.html', root='.')

@app.route('/cogs.mjs')
def cogs():
     return static_file('cogs.mjs', root='.')


### # ###
if __name__ == '__main__':
     if len(sys.argv) != 3: raise Exception('EXPLODE')
     print(f'Running in {sys.argv[1]} mode on port {sys.argv[2]}...')
     if sys.argv[1] == 'dev':
          app.run(host='0.0.0.0', port=int(sys.argv[2]), debug=True, reloader=True)
     if sys.argv[1] == 'FTW':
          app.run(host='0.0.0.0', port=int(sys.argv[2]))

#ned
