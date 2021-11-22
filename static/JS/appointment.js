
var ROW_NUMBER = 5;

Date.prototype.addDays = function (days) {
  var date = new Date(this.valueOf());
  date.setDate(date.getDate() + days);
  return date;
};

$(document).ready(function () {
  /* create datepicker */
  $("#txt_Date").datepicker({
    dateFormat: "dd/mm/yy",
  });

  $("#btn_Date").click(function () {
    $("#txt_Date").datepicker("show");
    $.ajax({
      url: "getemp" ,
      type: "get",
      dataType: "json",
      success: function (data) {
        if (data.error) {
          alert(data.error);
        } else {
          alert("Register success");
        }
      },
    });
  });
});


  
