console.log('heaw');

function registre_players(players, gold) {
     const api = `.${module_path}/registre_players`;
     const options = {
          method: `POST`,
          headers: {'Content-Type': 'application/json'},
          body: `${JSON.stringify({players, gold})}`
     };
     fetch(`/${api}`, options)
          .then(response => response.text())
          .then(response => {
               console.log(response);
          })
}

async function send_coins(mode, amount_of_gold, from_player, to_player=null) {
     const api = `.${module_path}/send_coins`;
     const options = {
          method: `POST`,
          headers: {'Content-Type': 'application/json'},
          body: `${JSON.stringify({mode, amount_of_gold, from_player, to_player})}`
     };
     return await fetch(`/${api}`, options)
          .then(response => response.text())
}

async function claim_staked(player) {
     const api = `.${module_path}/claim_staked`;
     const options = {
          method: `POST`,
          headers: {'Content-Type': 'application/json'},
          body: `${JSON.stringify({player})}`
     };
     return await fetch(`/${api}`, options)
          .then(response => response.text())
}
