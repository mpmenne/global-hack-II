
$(document).ready(function() {

	// Initialize Masonry
	var msnry = $('#content');
	msnry.masonry({
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
		console.log(event.type + ' just happened to #' + event.target.id );
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

	/*
	 * Add
	 **/

	(function (){
	
	var button = document.querySelector('#prepend-button');
	var container = document.querySelector('#content');

	// prepare div box
	function getItemElement() {
		var elem = document.createElement('div');
		var rand = Math.random();
		var size= 'medium';
		elem.className = "item " + size;
		return elem;
	}

	eventie.bind(button, 'click', function() {
		// create new item elements
		var elems = [];
		var fragment = document.createDocumentFragment();

		var elem = getItemElement();
		fragment.appendChild( elem );
		elems.push( elem );
		
		// prepend elements to container
		container.insertBefore( fragment, container.firstChild );
		// add and lay out newly prepended elements

		$('#content').masonry('prepended', elems );

		
	});
	
	})();
	
	/*
	 * Remove
	 **/

	(function (){
	
	var container = document.querySelector('#content');

	eventie.bind( container, 'click', function( event ) {
		// don't proceed if item was not clicked on
		if ( !classie.has( event.target, 'item' ) ) {
			return;
		}
		// remove clicked element
		$('#content').masonry('remove', event.target );
		
		// layout remaining item elements
		$('#content').masonry('layout');
	});
	
	})();

	/*
	 * Stamp & Unstamp
	 **/

});

function fetchNodes() {
	$.get('http://54.200.98.221:5000/api/v1', function(data) {
		return data;
	});
}

function updateNodesOnPage() {
	var jsonNodes = fetchNodes();
	// update data binding to bricks/nodes
}
