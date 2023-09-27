
// document.addEventListener("DOMContentLoaded", function(event) {
  // - Code to execute when all DOM content is loaded. 


// });
window.addEventListener( 'scroll', function() {
    // if scroll down after 45px (position Y)
    if (window.scrollY > 45) {
      document.querySelector('nav').style.position = 'fixed'
      document.querySelector('nav').style.top = '0'
      document.querySelector('nav').style.left = '0'
      document.querySelector('nav').style.right = '0'

    } else {
      document.querySelector('nav').style.position='fixed'
      document.querySelector('nav').style.top = '4%'
      document.querySelector('nav').style.left = '1%'
      document.querySelector('nav').style.right = '1%'
 
    }
  });
  
// counter 
  $('.count').each(function () {
    $(this).prop('Counter',0).animate({
        Counter: $(this).text()
    }, {
      
      //chnage count up speed here
        duration: 4000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });
});

// certificate image model
$('.pop').on('click', function() {
  $('.imagepreview').attr('src', $(this).find('img').attr('src'));

  $('#imagemodal').modal('show');   
});	

// testimonial slider
//  var myCarousel = document.querySelector('#carouselExampleIndicators')
// var carousel = new bootstrap.Carousel(myCarousel, {
//   interval: 5000
// })

// interval is in milliseconds. 1000 = 1 second -> so 1000 * 10 = 10 seconds
 

 	$(window).scroll(function () {
    if ($(this).scrollTop() > 45) {
      $('#back-to-top').fadeIn();
    } else {
      $('#back-to-top').fadeOut();
    }
  });
  // scroll body to 0px on click
  $('#back-to-top').click(function () {
    $('body,html').animate({
      scrollTop: 0
    }, 100);
    return false;
  });
 

  //Show tooltip on page load
   
  // $("#test").addClass("load");
  window.onload = () => {
    $('#onload').modal('show');
}
function reveal() {
  var reveals = document.querySelectorAll(".reveal");

  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 5;

    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add("active");
    } else {
      reveals[i].classList.remove("active");
    }
  }
}

window.addEventListener("scroll", reveal);
 
// gallery image Carousel
// var myCarousel1 = document.querySelector('#galleryControls')
// var myModalEl = document.getElementById('galleryModal')

// myModalEl.addEventListener('show.bs.modal', function (event) {
//     const trigger = event.relatedTarget
//     var bsCarousel = bootstrap.Carousel.getInstance(myCarousel1)
//     bsCarousel.to(trigger.dataset.bsSlideTo)
// })
  

var $btns = $('.btn-gallery').click(function() {
  if (this.id == 'all') {
    $('#parent > div').fadeIn(450);
  } else {
    var $el = $('.' + this.id).fadeIn(450);
    $('#parent > div').not($el).hide();
  }
  $btns.removeClass('active');
  $(this).addClass('active');
})

// contact
 
  // $('#QuestionOptions').change(function () {
  //     $('#myAnswers > div').hide();
  //      $('#myAnswers').find('#' + $(this).val()).fadeIn('slow');

  // });
 

  
$('#QuestionOptions').change(function () {
  dropdown = $('#QuestionOptions').val();
 //first hide all tabs again when a new option is selected
 $('#myAnswers > div').hide();

 //then show the tab content of whatever option value was selected
  $('#'  + dropdown).show();                                       
});


// 
// var current = 0;
// var tabs = $(".tab");
// var tabs_pill = $(".tab-pills");

// loadFormData(current);

// function loadFormData(n) {
//   $(tabs_pill[n]).addClass("active");
//   $(tabs[n]).removeClass("d-none");
//   $("#back_button").attr("disabled", n == 0 ? true : false);
//   n == tabs.length - 1
//     ? $("#next_button").text("Submit").removeAttr("onclick")
//     : $("#next_button")
//         .attr("type", "button")
//         .text("Next")
//         .attr("onclick", "next()");
// }

// function next() {
//   $(tabs[current]).addClass("d-none");
//   $(tabs_pill[current]).removeClass("active");

//   current++;
//   loadFormData(current);
// }

// function back() {
//   $(tabs[current]).addClass("d-none");
//   $(tabs_pill[current]).removeClass("active");

//   current--;
//   loadFormData(current);
// }

// booking casrsoel
 
  // var myCarousel = document.querySelector('#myCarousel')
// var carousel = new bootstrap.Carousel(myCarousel, {
//   interval: 100000
// })

