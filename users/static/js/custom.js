// $('[name="adddeck"]').click(function () {
//   var url = $('.deckname').attr("deck-add-url");
//   var deck_name = $("[name='name']").val();
//   if(deck_name != ''){
//     $.ajax({
//       url: url,
//       data: {
//         'deck_name': deck_name,
//       },
//       success: function(data){
//         alert(data);
//       }
//     });

//   }
// });


// ADD CSS CLASS TO DROPDOWN ON ADD CARD PAGE
$(document).ready(function(){
	// var d = document.getElementById("id_decks");
	// d.className += 'form-control';
	$('#id_decks').addClass("form-control");
	$("#id_decks option[value='']").remove();	
});