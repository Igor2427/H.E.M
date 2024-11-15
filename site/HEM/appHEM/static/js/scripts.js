//Informa que o CPF deve ter 11 dígitos
document.querySelector('input[name="cpf"]').addEventListener('input', function() {
    if (!this.validity.valid) {
      this.setCustomValidity('O CPF deve ter exatamente 11 dígitos numéricos.');
    } else {
      this.setCustomValidity('');
    }
  });

//Restringe a inserção de letras no campo de CPF
document.querySelector('input[name="cpf"]').addEventListener('keypress', function(event) {
    if (!/d/.test(event.key)) {
      event.preventDefault(); // Impede a digitação de qualquer caractere que não seja um número
    }
  });
  