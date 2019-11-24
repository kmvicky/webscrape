/* Project specific Javascript goes here. */


var readyAllFunctions = function() {

	var UpdateData = function() {
			
		$.ajax({
			method: 'get',
			url: 'niftygainers',
			data: {}
		}).done(function(response) {

			$("div.lists").html(response);
			
		}).fail(function(xhr, responseJSON) {

			$("body")
			.toast({
				class: "error",
				position: "top right",
				message:xhr.responseJSON.message
			});
		});

	}

	window.setInterval(function(){
		UpdateData();
	}, 300000);

}



$(document).ready(function() {
	readyAllFunctions();
});
