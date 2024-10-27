async function get_new_list() {
     const api = `.${module_path}/new_list`;
     const method = 'POST';
     const options = {
          method: `${method}`,
          headers: {'Content-Type': 'application/json'},
     };
     let id_list = await fetch(`/${api}`, options)
          .then(response => response.text())
          .catch(err => console.error(err));
     return id_list;
}

async function check_list(id_list) {
     const query = `.${module_path}/check_list?id=${id_list}`;
     const method = 'GET';
     const options = {
          method: `${method}`,
          headers: {'Content-Type': 'application/json'},
     };
     let status = await fetch(`/${query}`, options)
          .then(response => response.text())
          .catch(err => console.error(err));
     return status;
}
