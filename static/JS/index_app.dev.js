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
mail_register();

function mail_register() {
  $("#submitEmail").on("click", function () {
    if ($("#email").val() != "") {
      var token = $("[name=csrfmiddlewaretoken]").val();
      $.ajax({
        url: "/mail_register_for_infomation",
        type: "post",
        data: $("#infoForm").serialize(),
        headers: {
          "X-CSRFToken": token
        },
        dataType: "json",
        success: function success(data) {
          if (data.error) {
            alert(data.error);
          } else {
            alert("Register success");
          }
        }
      });
    }
  });
} // Chat Bot


$(function () {
  var INDEX = 0;
  $("#chat-submit").click(function (e) {
    e.preventDefault();
    var msg = $("#chat-input").val();

    if (msg.trim() == "") {
      return false;
    }

    generate_message(msg, "self");
    var buttons = [{
      name: "Existing User",
      value: "existing"
    }, {
      name: "New User",
      value: "new"
    }];
    setTimeout(function () {
      generate_message(msg, "user");
    }, 1000);
  });

  function generate_message(msg, type) {
    INDEX++;
    var str = "";
    str += "<div id='cm-msg-" + INDEX + "' class=\"chat-msg " + type + '">';
    str += '          <span class="msg-avatar">';
    str += '            <img src="https://image.crisp.im/avatar/operator/196af8cc-f6ad-4ef7-afd1-c45d5231387c/240/?1483361727745">';
    str += "          </span>";
    str += '          <div class="cm-msg-text">';
    str += msg;
    str += "          </div>";
    str += "        </div>";
    $(".chat-logs").append(str);
    $("#cm-msg-" + INDEX).hide().fadeIn(300);

    if (type == "self") {
      $("#chat-input").val("");
    }

    $(".chat-logs").stop().animate({
      scrollTop: $(".chat-logs")[0].scrollHeight
    }, 1000);
  }

  function generate_button_message(msg, buttons) {
    /* Buttons should be object array 
      [
        {
          name: 'Existing User',
          value: 'existing'
        },
        {
          name: 'New User',
          value: 'new'
        }
      ]
    */
    INDEX++;
    var btn_obj = buttons.map(function (button) {
      return '              <li class="button"><a href="javascript:;" class="btn btn-primary chat-btn" chat-value="' + button.value + '">' + button.name + "</a></li>";
    }).join("");
    var str = "";
    str += "<div id='cm-msg-" + INDEX + '\' class="chat-msg user">';
    str += '          <span class="msg-avatar">';
    str += '            <img src="https://image.crisp.im/avatar/operator/196af8cc-f6ad-4ef7-afd1-c45d5231387c/240/?1483361727745">';
    str += "          </span>";
    str += '          <div class="cm-msg-text">';
    str += msg;
    str += "          </div>";
    str += '          <div class="cm-msg-button">';
    str += "            <ul>";
    str += btn_obj;
    str += "            </ul>";
    str += "          </div>";
    str += "        </div>";
    $(".chat-logs").append(str);
    $("#cm-msg-" + INDEX).hide().fadeIn(300);
    $(".chat-logs").stop().animate({
      scrollTop: $(".chat-logs")[0].scrollHeight
    }, 1000);
    $("#chat-input").attr("disabled", true);
  }

  $(document).delegate(".chat-btn", "click", function () {
    var value = $(this).attr("chat-value");
    var name = $(this).html();
    $("#chat-input").attr("disabled", false);
    generate_message(name, "self");
  });
  $("#chat-circle").click(function () {
    $("#chat-circle").toggle("scale");
    $(".chat-box").toggle("scale");
  });
  $(".chat-box-toggle").click(function () {
    $("#chat-circle").toggle("scale");
    $(".chat-box").toggle("scale");
  });
});
get_best_service_sell(); // Best Service Seller

function get_best_service_sell() {
  $.ajax({
    url: "/best_service_seller",
    type: "get",
    dataType: "json",
    success: function success(data) {
      data.forEach(function (e) {
        var _html = "\n          <div class=\"col-4 text-center best-service-box\">\n          <a href = \"#\" style=\"color:#000000; text-decoration: none;\">\n              <div class=\"mb-2\" style=\"height: 250px; background-color: rgb(244 244 244); padding: 1em;\">\n                  <img class=\"service_img\" src=\"".concat(e.service_img, "\"\n                      style=\"max-width: 100%; max-height: 100%;\">\n              </div>\n              <h5 class=\"service-name\" style=\"font-weight: bold;\">").concat(e.service_name, "</h5>\n              <p class=\"service-price\">\u0E40\u0E23\u0E34\u0E48\u0E21\u0E15\u0E49\u0E19\u0E17\u0E35\u0E48 ").concat(e.service_cost, " Bath</p>\n          </a>\n          </div>\n        ");

        $("#bestServices").append(_html);
      });
    }
  });
}

get_best_product_sell(); // Best Product Seller

function get_best_product_sell() {
  $.ajax({
    url: "/best_product_seller",
    type: "get",
    dataType: "json",
    success: function success(data) {
      data.forEach(function (e) {
        var _html = "\n          <div class=\"col-4 text-center best-product-box\">\n          <a href = \"#\" style=\"color:#000000; text-decoration: none;\">\n            <div class=\"mb-2\" style=\"height: 250px; background-color: rgb(244 244 244); padding: 1em;\">\n              <img class=\"product-img\" src=\"".concat(e.prod_img, "\"\n                style=\"max-width: 100%; max-height: 100%;\">\n            </div>\n            <h5 class=\"product-name\" style=\"font-weight: bold;\">").concat(e.prod_name, "</h5>\n            <h5 class=\"product-detail\">").concat(e.prod_detail, "</h5>\n            <p class=\"product-review\">").concat(e.prod_review, "</p>\n            <p class=\"product-price\">").concat(e.prod_price, " Bath</p>\n            </a>\n          </div>\n        ");

        $("#bestProduct").append(_html);
      });
    }
  });
}