console.log('heaw');

function register_players(players) {
     const api = `.${module_path}/registre_players`;
     const options = {
          method: `POST`,
          headers: {'Content-Type': 'application/json'},
          body: `${JSON.stringify(players)}`
     };
     fetch(`/${api}`, options)
          .then(response => response.text())
          .then(response => {
               console.log(response);
          })
          .catch(err => console.error(err));
}

function save_points(player, points) {
     const api = `.${module_path}/save_points/${player}`;
     const options = {
          method: `PUT`,
          headers: {'Content-Type': 'application/json'},
          body: `{"${player}": ${JSON.stringify(points)}}`
     };
     console.log(options.body);
     fetch(`/${api}`, options)
          .then(response => response.text())
          .then(response => {
               console.log(response);
          })
          .catch(err => console.error(err));
}
