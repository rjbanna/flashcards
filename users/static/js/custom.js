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

function buttonAction(type, cardNumber){
	if(type == 1){
		// REVEAL BUTTON
		$('.back'+cardNumber).show()
		$('.card'+cardNumber).addClass('learnt')
		$('.card_buttons').show()
		$('.show-btn').hide()
	}else if(type == 2){
		// AGAIN BUTTON
		$('.back'+cardNumber).hide()
		$('.card'+cardNumber).removeClass('learnt')
		$('.card_buttons').hide()
		$('.show-btn').show()
	}else{
		// EASY BUTTON
		// DISPLAYING NEXT CARDS FROM REMAINING CARDS WHERE LEARNT CLASS IS NOT AVAILABLE
		let unvisited = $('.cards').not('.learnt');
		let next_card = unvisited.eq(Math.floor(Math.random(unvisited.length)));
		next_card.show();

		// TO CHECK IF IT WAS LAST CARD
		// alert(next_card.length)

		$('.learnt').hide()
		$('.card_buttons').hide()
		$('.show-btn').show()
	}	
}