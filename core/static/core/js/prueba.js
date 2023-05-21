$(document).ready(function() {
    $.ajax({
      url: '/cantidad_items_carrito/',
      success: function(response) {
        var cantidadItems = response.cantidad_items;
        $('#cantidad-items').text(cantidadItems);
      }
    });
  });

$(document).ready(function() {
  $.ajax({
    url: '/obtener_total_carrito/',
    success: function(response) {
      var totalCarrito =response.total_carrito
      $('#total-carrito').text(totalCarrito);
    },
    error: function(xhr, status, error) {
      console.error('Error en la solicitud AJAX:', status, error);
    }
  });
});

document.addEventListener('DOMContentLoaded', function() {
  const botonesIncremento = document.querySelectorAll('.btn-incremento');
  const botonesDecremento = document.querySelectorAll('.btn-decremento');

  botonesIncremento.forEach(boton => {
    boton.addEventListener('click', function() {
      const productoId = this.getAttribute('data-producto-id');
      const inputCantidad = document.getElementById(`cantidad-${productoId}`);
      const nuevaCantidad = parseInt(inputCantidad.value) + 1;
      inputCantidad.value = nuevaCantidad;
    });
  });

  botonesDecremento.forEach(boton => {
    boton.addEventListener('click', function() {
      const productoId = this.getAttribute('data-producto-id');
      const inputCantidad = document.getElementById(`cantidad-${productoId}`);
      const nuevaCantidad = parseInt(inputCantidad.value) - 1;
      if (nuevaCantidad >= 0) {
        inputCantidad.value = nuevaCantidad;
      }
    });
  });
});
