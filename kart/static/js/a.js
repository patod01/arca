const timout = 20000;

console.log(Date());
let a;

function add_item_to(listado, new_item) {
     if (new_item != '')
          listado.push({nombre: new_item, is_ready: false, hora: 0});
}

// setTimeout(() => window.location.reload(), timout);

function now() {
     return [
          new Date().getFullYear(),
          new Date().getMonth(),
          new Date().getDate(),
          new Date().getHours(),
          new Date().getMinutes(),
          new Date().getSeconds(),
     ];
}

function get_last_edit() {
     const api = 'last-edit';
     const method = 'GET';
     const options = {
          method: `${method}`,
          headers: {'Content-Type': 'application/json'},
          // body: ``
     };
     fetch(`/${api}`, options)
          .then(response => response.json())
          .then(response => {
               console.log(response);
          })
          .catch(err => console.error(err));
}

function backup(listado) {
     const api = 'backup';
     const method = 'POST';
     const options = {
          method: `${method}`,
          headers: {'Content-Type': 'application/json'},
          body: `${JSON.stringify(listado)}`
     };
     fetch(`/${api}`, options)
          .then(response => response.text())
          .then(response => {
               console.log(response);
          })
          .catch(err => console.error(err));
}

// setTimeout(get_last_edit, 5000);
