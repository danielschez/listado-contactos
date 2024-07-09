$(document).ready(function() {
  let emailCount = 1; // Inicializar un contador para los IDs de campo
  let telCount = 1; // Inicializar un contador para los IDs de campo
  let dirCount = 1; // Inicializar un contador para los IDs de campo

  // Añadir campos de correo electrónico extra
  $('#add_email').click(function() {
      // Crear un nuevo elemento de campo de formulario para correo electrónico
      let newEmail = `
          <div class="form-group">
              <label for="extra_email_${emailCount}">Email Extra ${emailCount}:</label>
              <input type="email" id="extra_email_${emailCount}" name="extra_email_${emailCount}" class="form-control">
          </div>`;

        //let totalEmail = `<input type="hidden" value="${emailCount}" id="total_email" name="total_email">`;

      // Añadir el nuevo campo de correo electrónico al contenedor
      $('#fields_email').append(newEmail);

      // Incrementar el contador de campos
      emailCount++;
      $('#total_email').val(emailCount-1);
  });


  // Añadir campos de teléfono extra
  $('#add_telefono').click(function() {
      // Crear un nuevo elemento de campo de formulario para teléfono
      let newTel = `
          <div class="form-group">
              <label for="extra_tel_${telCount}">Teléfono Extra ${telCount}:</label>
              <input type="text" id="extra_tel_${telCount}" name="extra_tel_${telCount}" class="form-control">
          </div>`;

      // Añadir el nuevo campo de teléfono al contenedor
      $('#fields_telefono').append(newTel);

      // Incrementar el contador de campos
      telCount++;
      $('#total_tel').val(telCount-1);
  });

  // Añadir campos de dirección extra
  $('#add_dir').click(function() {
      // Crear un nuevo elemento de campo de formulario para dirección
      let newDir = `
          <div class="form-group">
              <label for="extra_dir_${dirCount}">Dirección Extra ${dirCount}:</label>
              <input type="text" id="extra_dir_${dirCount}" name="extra_dir_${dirCount}" class="form-control">
          </div>`;

      // Añadir el nuevo campo de dirección al contenedor
      $('#fields_direccion').append(newDir);

      // Incrementar el contador de campos
      dirCount++;
      $('#total_dir').val(dirCount-1);
  });
});