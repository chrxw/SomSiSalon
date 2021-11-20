// Information
$("#email").on("input", function () {
  if ($(this).val() == "") {
    $("#submitEmail").prop("disabled", true);
  } else {
    $("#submitEmail").prop("disabled", false);
  }
});

const form = document.getElementById("infoForm");

form.addEventListener(
  "submit",
  function (event) {
    if (!form.checkValidity()) {
      event.preventDefault();
      event.stopPropagation();
    }

    form.classList.add("was-validated");
  },
  false
);

mail_register();
function mail_register() {
  $("#submitEmail").on("click", function () {
    if ($("#email").val() != "") {
      var token = $("[name=csrfmiddlewaretoken]").val();
      $.ajax({
        url: "/mail_register_for_infomation",
        type: "post",
        data: $("#infoForm").serialize(),
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

// Chat Bot
$(function () {
  var INDEX = 0;
  $("#chat-submit").click(function (e) {
    e.preventDefault();
    var msg = $("#chat-input").val();
    if (msg.trim() == "") {
      return false;
    }
    generate_message(msg, "self");
    var buttons = [
      {
        name: "Existing User",
        value: "existing",
      },
      {
        name: "New User",
        value: "new",
      },
    ];
    setTimeout(function () {
      generate_message(msg, "user");
    }, 1000);
  });

  function generate_message(msg, type) {
    INDEX++;
    var str = "";
    str += "<div id='cm-msg-" + INDEX + "' class=\"chat-msg " + type + '">';
    str += '          <span class="msg-avatar">';
    str +=
      '            <img src="https://image.crisp.im/avatar/operator/196af8cc-f6ad-4ef7-afd1-c45d5231387c/240/?1483361727745">';
    str += "          </span>";
    str += '          <div class="cm-msg-text">';
    str += msg;
    str += "          </div>";
    str += "        </div>";
    $(".chat-logs").append(str);
    $("#cm-msg-" + INDEX)
      .hide()
      .fadeIn(300);
    if (type == "self") {
      $("#chat-input").val("");
    }
    $(".chat-logs")
      .stop()
      .animate({ scrollTop: $(".chat-logs")[0].scrollHeight }, 1000);
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
    var btn_obj = buttons
      .map(function (button) {
        return (
          '              <li class="button"><a href="javascript:;" class="btn btn-primary chat-btn" chat-value="' +
          button.value +
          '">' +
          button.name +
          "</a></li>"
        );
      })
      .join("");
    var str = "";
    str += "<div id='cm-msg-" + INDEX + '\' class="chat-msg user">';
    str += '          <span class="msg-avatar">';
    str +=
      '            <img src="https://image.crisp.im/avatar/operator/196af8cc-f6ad-4ef7-afd1-c45d5231387c/240/?1483361727745">';
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
    $("#cm-msg-" + INDEX)
      .hide()
      .fadeIn(300);
    $(".chat-logs")
      .stop()
      .animate({ scrollTop: $(".chat-logs")[0].scrollHeight }, 1000);
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

get_best_service_sell();
// Best Service Seller
function get_best_service_sell() {
  $.ajax({
    url: "/best_service_seller",
    type: "get",
    dataType: "json",
    success: function (data) {
      data.forEach((e) => {
        const _html = `
          <div class="col-4 text-center best-service-box">
          <a href = "#" style="color:#000000; text-decoration: none;">
              <div class="mb-2" style="height: 250px; background-color: rgb(244 244 244); padding: 1em;">
                  <img class="service_img" src="${e.service_img}"
                      style="max-width: 100%; max-height: 100%;">
              </div>
              <h5 class="service-name" style="font-weight: bold;">${e.service_name}</h5>
              <p class="service-price">เริ่มต้นที่ ${e.service_cost} Bath</p>
          </a>
          </div>
        `;
        $("#bestServices").append(_html);
      });
    },
  });
}

get_best_product_sell();
// Best Product Seller
function get_best_product_sell() {
  $.ajax({
    url: "/best_product_seller",
    type: "get",
    dataType: "json",
    success: function (data) {
      data.forEach((e) => {
        const _html = `
          <div class="col-4 text-center best-product-box">
          <a href = "#" style="color:#000000; text-decoration: none;">
            <div class="mb-2" style="height: 250px; background-color: rgb(244 244 244); padding: 1em;">
              <img class="product-img" src="${e.prod_img}"
                style="max-width: 100%; max-height: 100%;">
            </div>
            <h5 class="product-name" style="font-weight: bold;">${e.prod_name}</h5>
            <h5 class="product-detail">${e.prod_detail}</h5>
            <p class="product-review">${e.prod_review}</p>
            <p class="product-price">${e.prod_price} Bath</p>
            </a>
          </div>
        `;
        $("#bestProduct").append(_html);
      });
    },
  });
}
