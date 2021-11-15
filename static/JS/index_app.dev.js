"use strict";

// Information
$("#email").on("input", function () {
  if ($(this).val() == "") {
    $("#submitEmail").prop("disabled", true);
  } else {
    $("#submitEmail").prop("disabled", false);
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