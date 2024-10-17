const timout = 2000;

console.log(Date());
let a;

function add_item_to(listado, new_item) {
     if (new_item != '')
          listado.push({nombre: new_item, is_ready: false, hora: 0});
}

setTimeout(() => window.location.reload(), timout);
