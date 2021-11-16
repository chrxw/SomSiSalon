"use strict";

// Promocode
$("#VoucherCode").on("input", function () {
  if ($(this).val() == "") {
    $("#submitVoucherCode").prop("disabled", true);
  } else {
    $("#submitVoucherCode").prop("disabled", false);
  }
});
var form = document.getElementById("infoForm");
form.addEventListener("submit", function (event) {
  if (!form.checkValidity()) {
    event.preventDefault();
    event.stopPropagation();
  }

  form.classList.add("was-validated");
}, false);