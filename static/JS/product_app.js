//Service slideshow
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}

//Add to cart ()
function clickOn_Gluten() {
  if(typeof(Storage) !== "undefined") {
    if (localStorage.clickcount1) {
      localStorage.clickcount1 = Number(localStorage.clickcount1)+1;
    } else {
      localStorage.clickcount1 = 1;
    }
    // document.getElementById("tothecart1").innerHTML = "You have clicked the button " + localStorage.clickcount1 + " time(s).";
  } else {
    document.getElementById("tothecart1").innerHTML = "Sorry, your browser does not support web storage...";
  }
}
function clickOn_Loma() {
  if(typeof(Storage) !== "undefined") {
    if (localStorage.clickcount2) {
      localStorage.clickcount2 = Number(localStorage.clickcount2)+1;
    } else {
      localStorage.clickcount2 = 1;
    }
    // document.getElementById("tothecart2").innerHTML = "You have clicked the button " + localStorage.clickcount2 + " time(s).";
  } else {
    document.getElementById("tothecart2").innerHTML = "Sorry, your browser does not support web storage...";
  }
}
function clickOn_Hempz() {
  if(typeof(Storage) !== "undefined") {
    if (localStorage.clickcount3) {
      localStorage.clickcount3 = Number(localStorage.clickcount3)+1;
    } else {
      localStorage.clickcount3 = 1;
    }
    // document.getElementById("tothecart3").innerHTML = "You have clicked the button " + localStorage.clickcount3 + " time(s).";
  } else {
    document.getElementById("tothecart3").innerHTML = "Sorry, your browser does not support web storage...";
  }
}

count_product();
function count_product(){
  var x = Number(localStorage.clickcount1);
  var y = Number(localStorage.clickcount2);
  var z = Number(localStorage.clickcount3);
  countnoti = x + y + z;
  $("#countprod").append(countnoti);
}

// function clickOn(){
//   if(typeof(Storage) !== "undefined") {
//     if (localStorage.clickcount1) {
//       localStorage.clickcount1 = Number(localStorage.clickcount1)+1;
//       countnoti++;
//     if (localStorage.clickcount2) {
//       localStorage.clickcount2 = Number(localStorage.clickcount2)+1;
//       countnoti++;
//     if (localStorage.clickcount3) {
//       localStorage.clickcount3 = Number(localStorage.clickcount3)+1;
//       countnoti++;

//   }
// }

//clear local storge
// clear_count();
// function clear_count(){
//   localStorage.clear();
//   countnoti = 0;
//   $("#countprod").append(countnoti);
// }

get_product_list();
// Product List
function get_product_list() {
  console.log("*********************")
  $.ajax({
    url: "/product_list",
    type: "get",
    dataType: "json",
    success: function (data) {
      data.forEach((e) => {
        const _html = `
          <div class="card">
            <br>
            <img class="product-img" src="${e.prod_img}" style="margin-left: 5em; width:120px; height: 120px;">
            <h5 class="product-name"><u>${e.prod_name}</u></h5>
            <p class="product-price">${e.prod_price} Baht</p>
            <p>✓ Hypoallergenic<br>✓ Biodegradable<br>✓ Made in America</p>
            <p><button><i class="fa fa-cart-plus"></i>&nbsp;&nbsp;Add to cart</button>
          </div>
        `;
        $("#ProductListt").append(_html);
      });
    },
  });
}

