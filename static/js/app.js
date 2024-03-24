const consultarBtn = document.getElementById("btn-consultar");
const editarBtn = document.getElementById("btn-editar");
const nombreInput = document.getElementById("nombre");
const precioInput = document.getElementById("precio");
const resultadoDiv = document.getElementById("resultado");

consultarBtn.addEventListener("click", consultarProducto);
editarBtn.addEventListener("click", editarProducto);

function consultarProducto() {
    const nombre = nombreInput.value;

    // Realizar la petición para obtener los productos del archivo productos.json
    fetch('/static/data/productos.json')
        .then(response => response.json())
        .then(data => {
            // Buscar el producto por nombre en los datos obtenidos
            const producto = data.find(item => item.nombre === nombre);

            // Verificar si se encontró el producto
            if (producto) {
                resultadoDiv.innerHTML = `
                    <h3>Producto encontrado</h3>
                    <p>Nombre: ${producto.nombre}</p>
                    <p>Precio: ${producto.precio}</p>
                `;
            } else {
                resultadoDiv.innerHTML = `
                    <p>Producto no encontrado</p>
                `;
            }
        })
        .catch(error => {
            console.error('Error al obtener los datos:', error);
            resultadoDiv.innerHTML = `
                <p>Ocurrió un error al obtener los datos del servidor.</p>
            `;
        });
}




function obtenerProductoPorNombre(nombre) {
  // Aquí se debe realizar la llamada a la API o a la base de datos para obtener el producto por nombre.
  // Ejemplo:
  const url = `/api/productos/${nombre}`;
  return fetch(url).then(response => response.json());
}

function editarProducto(nombre, precio) {
  // Aquí se debe realizar la llamada a la API o a la base de datos para editar el producto.
  // Ejemplo:
  const url = `/api/productos/${nombre}`;
  const data = {
    precio: precio,
  };
  return fetch(url, {
    method: 'PUT',
    body: JSON.stringify(data),
  }).then(response => response.json());
}