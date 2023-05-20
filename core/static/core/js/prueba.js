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