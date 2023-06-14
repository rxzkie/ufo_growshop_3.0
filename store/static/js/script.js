

function enviar() {
    var nombre, email, mensaje;

    nombre = document.getElementById("nombre").value;
    email = document.getElementById("email").value;
    mensaje = document.getElementById("mensaje").value;

    var error = false;
    var mensaje_error = "";

    if (nombre == "") {
        error = true;
        mensaje_error += "Por favor ingrese un nombre. ";
        document.getElementById("error-nombre").innerHTML = "Por favor ingrese un nombre.";
    } else {
        document.getElementById("error-nombre").innerHTML = "";
    }

    if (!/^\S+@\S+\.\S+$/.test(email)) {
        error = true;
        mensaje_error += "Por favor ingrese un correo electrónico válido. ";
        document.getElementById("error-email").innerHTML = "Por favor ingrese un correo electrónico válido.";
    } else {
        document.getElementById("error-email").innerHTML = "";
    }


    if (mensaje == "") {
        error = true;
        mensaje_error += "Por favor ingrese un mensaje. ";
        document.getElementById("error-mensaje").innerHTML = "Por favor ingrese un mensaje.";
    } else {
        document.getElementById("error-mensaje").innerHTML = "";
    }

    if (error) {
        return false;
    } else {
        document.getElementById("enviado").innerHTML = "¡Mensaje enviado correctamente!";
        document.getElementById("enviado").style.display = "block";
        return true;
    }
}



$(document).ready(function() {
  $('#enviar').click(function(event) {
    var username = $('#username').val();
    var password = $('#password').val();
    var errorMensaje = document.getElementById("error-mensaje");

    // Validación de campos
    if (username == '') {
      $('.error-username').html('Debe ingresar un nombre de usuario.').show();
      event.preventDefault(); // Evita el envío del formulario
      return false;
    } else {
      $('.error-username').hide();
    }

    if (password == '') {
      $('.error-password').html('Debe ingresar una contraseña.').show();
      event.preventDefault(); // Evita el envío del formulario
      return false;
    } else {
      $('.error-password').hide();
    }

    // Envío de formulario
    if (username == 'admin' && password == 'admin') {
      // Si las credenciales son correctas, se enviará el formulario y se cargará la página panel.html
    } else {
      errorMensaje.innerHTML = "Credenciales incorrectas";
      event.preventDefault(); // Evita el envío del formulario
    }
  });
});


  $(document).ready(function() {
    $.getJSON('https://ufo-growshop-default-rtdb.firebaseio.com/semillas.json', function(data) {
      $.each(data, function(key, value) {
        var card = $('<div>').addClass('card');
        var cardBody = $('<div>').addClass('card-body');
        var cardTitle = $('<h5>').addClass('card-title').text(value.nombre);
        var cardPrice = $('<p>').addClass('card-text').text('Precio: $' + value.precio);
        var cardType = $('<p>').addClass('card-text').text('Tipo: ' + value.tipo);
        var cardImage = $('<img>').addClass('card-img-top').attr('src', value.imagen).attr('alt', value.nombre);
        var cardButton = $('<button>').addClass('btn btn-primary').text('Comprar');
        cardBody.append(cardTitle).append(cardPrice).append(cardType).append(cardButton);
        card.append(cardImage).append(cardBody);
        $('#card-container').append(card);
      });
    });
  });
  





  
  function filterByType() {
    $('#card-container').empty();
    var selectedTypes = [];
  
    // Obtener todos los tipos seleccionados
    $('input[type=checkbox]:checked').each(function() {
      selectedTypes.push($(this).val());
    });
  
    if (selectedTypes.length === 0) {
      // Si no hay tipos seleccionados, mostrar todas las semillas
      $.getJSON('https://ufo-growshop-default-rtdb.firebaseio.com/semillas.json', function(data) {
        $.each(data, function(key, value) {
          var card = $('<div>').addClass('card');
          var cardBody = $('<div>').addClass('card-body');
          var cardTitle = $('<h5>').addClass('card-title').text(value.nombre);
          var cardPrice = $('<p>').addClass('card-text').text('Precio: $' + value.precio);
          var cardType = $('<p>').addClass('card-text').text('Tipo: ' + value.tipo);
          var cardImage = $('<img>').addClass('card-img-top').attr('src', value.imagen).attr('alt', value.nombre);
          var cardButton = $('<button>').addClass('btn btn-primary').text('Comprar');
          cardBody.append(cardTitle).append(cardPrice).append(cardType).append(cardButton);
          card.append(cardImage).append(cardBody);
          $('#card-container').append(card);
        });
      });
  
    } else {
      // Filtrar semillas por tipo
      $.getJSON('https://ufo-growshop-default-rtdb.firebaseio.com/semillas.json', function(data) {
        $.each(data, function(key, value) {
          if (selectedTypes.includes(value.tipo)) {
            var card = $('<div>').addClass('card');
            var cardBody = $('<div>').addClass('card-body');
            var cardTitle = $('<h5>').addClass('card-title').text(value.nombre);
            var cardPrice = $('<p>').addClass('card-text').text('Precio: $' + value.precio);
            var cardType = $('<p>').addClass('card-text').text('Tipo: ' + value.tipo);
            var cardImage = $('<img>').addClass('card-img-top').attr('src', value.imagen).attr('alt', value.nombre);
            var cardButton = $('<button>').addClass('btn btn-primary').text('Comprar');
            cardBody.append(cardTitle).append(cardPrice).append(cardType).append(cardButton);
            card.append(cardImage).append(cardBody);
            $('#card-container').append(card);
          }
        });
      });
    }
  }
  
  

