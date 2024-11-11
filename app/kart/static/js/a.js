function add_item_to(listado, new_item) {
     if (new_item != '')
          listado.push({nombre: new_item, is_ready: false, hora: 0});
}

function formattedNow() {
     return [
          new Date().getFullYear(),
          new Date().getMonth(),
          new Date().getDate(),
          new Date().getHours(),
          new Date().getMinutes(),
          new Date().getSeconds(),
     ];
}

function now() {return Math.floor(new Date().getTime()/1000);}

async function get_last_edit() {
     const api = `${module_path}/last_edit`;
     const method = 'GET';
     const options = {
          method: `${method}`,
     };
     return await fetch(`${api}`, options)
          .then(response => response.json())
          .then(secondsFromEpoch => secondsFromEpoch)
          .catch(err => console.error(err));
}

function backup(id_lista, listado) {
     const api = `.${module_path}/backup`;
     const method = 'POST';
     const options = {
          method: `${method}`,
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({id_lista, listado})
     };
     fetch(`/${api}`, options)
          .then(response => response.text())
          .then(response => {
               console.log(response);
          })
          .catch(err => console.error(err));
}
