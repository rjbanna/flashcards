$(document).ready(function(){
  $("[name='location'] option[value='']").remove();
  $('[name="location"]').prepend(new Option("--- Select Study location ---", "0"));
  $('[name="location"] option[value="0"]').attr("selected",true);

  $("[name='course'] option[value='']").remove();
  $('[name="course"]').prepend(new Option("--- Select Course Type ---", "0"));
  $('[name="course"] option[value="0"]').attr("selected",true);
});

function formatNumber(num) {
  return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
}

$("[name=loan_amount]").on("keypress keyup blur",function (event) {
  $(this).val($(this).val().replace(/[^0-9\.]/g,''));
  if ((event.which != 46 || $(this).val().indexOf('.') != -1) && (event.which < 48 || event.which > 57)) {
    event.preventDefault();
  }

  if ($(this).val() > 6000000) {
       event.preventDefault();
       $(this).val(6000000);
    }
});




$('[name="search_loan"]').click(function () {
  var location = $("[name='location']").val();
  var course = $("[name='course']").val();
  var amount = $("[name=loan_amount]").val();

  if(location == 0){
    e.preventdefault();
  }
  if(course == 0){
    e.preventdefault();
  }
});
