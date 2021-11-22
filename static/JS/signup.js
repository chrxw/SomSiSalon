signup();
function signup() {
  $("#btnSIGNUP").on("click", function () {
    if ($("#username").val() != "") {
      var token = $("[name=csrfmiddlewaretoken]").val();
      $.ajax({
        url: "/signup",
        type: "post",
        data: $("#UserForm").serialize(),
        headers: { "X-CSRFToken": token },
        dataType: "json",
        success: function (data) {
          if (data.error) {
            alert(data.error);
          } else {
            alert("Register success");
          }
        },
      });
    }
  });
}