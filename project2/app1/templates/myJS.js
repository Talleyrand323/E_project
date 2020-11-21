$(document).ready(function(){

	$('#front').mousedown(function(){
	  $.ajax({
		  url: "{% url 'front' %}",		  dataType: 'json',
		  success: function(data) {  },	  error: function(data) {  },
	  	})	})
	$('#front').mouseup(function(){
	  $.ajax({
		  url: "{% url 'stop' %}",			  dataType: 'json',
		  success: function(data) {  },  error: function(data) {  },
		})	})


	$('#front').touchstart(function(){
	  $.ajax({
		  url: "{% url 'front' %}",		  dataType: 'json',
		  success: function(data) {  },	  error: function(data) {  },
	  	})	})
	$('#front').touchend(function(){
	  $.ajax({
		  url: "{% url 'stop' %}",			  dataType: 'json',
		  success: function(data) {  },  error: function(data) {  },
		})	})


	$('#back').mousedown(function(){
	  $.ajax({
		  url: "{% url 'back' %}",		  dataType: 'json',
		  success: function(data) {  },	  error: function(data) {  },
	  	})	})
	$('#back').mouseup(function(){
	  $.ajax({
		  url: "{% url 'stop' %}",			  dataType: 'json',
		  success: function(data) {  },  error: function(data) {  },
		})	})
		
	$('#cl_wise').mousedown(function(){
	  $.ajax({
		  url: "{% url 'cl_wise' %}",		  dataType: 'json',
		  success: function(data) {  },	  error: function(data) {  },
	  	})	})
	$('#cl_wise').mouseup(function(){
	  $.ajax({
		  url: "{% url 'stop' %}",			  dataType: 'json',
		  success: function(data) {  },  error: function(data) {  },
		})	})
		
	$('#counter_cl').mousedown(function(){
	  $.ajax({
		  url: "{% url 'counter_cl' %}",		  dataType: 'json',
		  success: function(data) {  },	  error: function(data) {  },
	  	})	})
	$('#counter_cl').mouseup(function(){
	  $.ajax({
		  url: "{% url 'stop' %}",			  dataType: 'json',
		  success: function(data) {  },  error: function(data) {  },
		})	})


	$('#speed_up').mousedown(function(){
	  $.ajax({
		  url: "{% url 'speed_up' %}",		  dataType: 'json',
		  success: function(data) {  },	  error: function(data) {  },
	  	})	})
	$('#speed_down').mouseup(function(){
	  $.ajax({
		  url: "{% url 'speed_down' %}",		  dataType: 'json',
		  success: function(data) {  },  error: function(data) {  },
		})	})
})
