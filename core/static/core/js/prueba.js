$(document).ready(function() {
    $.ajax({
      url: '/cantidad_items_carrito/',
      success: function(response) {
        var cantidadItems = response.cantidad_items;
        $('#cantidad-items').text(cantidadItems);
      }
    });
  });