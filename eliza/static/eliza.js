$(document).ready(function() {
	$("#inputForm").submit(function (event) {
		event.preventDefault();	
		var input = $("#input").val();
		$("#input").val("");
		$.ajax({
			type: "POST",
			headers: {"Content-Type": "application/json"},
			data: {'human': input},
			dataType: "json",
			url: "/eliza/DOCTOR"
		}).done(function(data) {
			$("#dialogue").append("<div class='human'> Human: " + input + "</div>");
			$("#dialogue").append("<div class='eliza'>Eliza: " + data.eliza + "</div>")
		}).fail(function() {
			dial_elem = document.getElementById('dialogue');
                        dial_elem.innerHTML += "FAIL" + "<br>";
		});		
	});	
});

