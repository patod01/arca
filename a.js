console.log('heaw');


function api_shortcut(api, method, players) {
     const options = {
          method: `${method}`,
          headers: {'Content-Type': 'application/json'},
          body: `${players}`
     };
     console.log(players)
     console.log(typeof players)
     fetch(`/${api}`, options)
          .then(response => response.text())
          .then(response => {
               console.log(response);
          })
          .catch(err => console.error(err));
}


function save_points(player, points) {
     const api = `save_points/${player}`;
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
