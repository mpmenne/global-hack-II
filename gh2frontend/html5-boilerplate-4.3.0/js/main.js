
$(document).ready(function() {

	// Initialize Masonry
	$('#content').masonry({
		// Masonry options
		columnWidth: 30,
		itemSelector: '.item',
		isFitWidth: true,
		isAnimated: !Modernizr.csstransitions
	});

	/*
	 * Bind actions to events for an action if desired
	 **/
	var elem = document.querySelector('#test');
	
	function onElemClick(event){
		console.log(event.type + ' just happned to #' + event.target.id );
	}

	eventie.bind(elem, 'click', onElemClick);
	
	/*
	 * Filter by binding event on any changes from select box
	 **/
	$('#grid-filter').on("change", function(){
		group = $(this).val();
		groupClass = "." + group;

		if (group != "") {
			$('.item').hide();
			$(groupClass).show();
			$('#content').masonry('layout');
		}
		else {
			$('.item').show();
			$('#content').masonry('layout');
		}
	});

});