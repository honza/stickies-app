// Notes
var mle;
var ev;

$(function() {
		$( ".column" ).sortable({
			connectWith: ".column",
		    stop: function(event, ui){
		        // When done sorting, fire off an ajax call
		        var id = ui.item[0].id;
		        var w = event.toElement.parentElement;
		        w = $(w).parent();
		        w = w.attr('id');
		        $.post('/ajax/', {
                    note: id,
                    section: w
                }, function(r){
                    if (r != 'OK'){
                        alert('There was an error while saving.');
                    }
                });
		    }
		});
 
		$( ".portlet" ).addClass( "ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" )
		    .prepend('<div class="portlet-header"></div>')
		    .find(".portlet-header")
		        .prepend('<span class="ui-icon ui-icon-pencil"></span>')
		        .prepend('<span class="ui-icon ui-icon-close"></span>')
		        .addClass('ui-widget-header ui-corner-all');
        $( ".column" ).disableSelection();
});
