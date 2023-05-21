function eliminarProducto(id) {
    Swal.fire({
      title: 'Confirmar',
      text: '¿Desea Eliminar?',
      icon: 'question',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'success'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire('Eliminado!','Producto Eliminado Correctamente','success').then(function() {
            window.location.href = "/delete/"+id+"/";
        })
      }
    })
  }
