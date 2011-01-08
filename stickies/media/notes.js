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
		        alert(id);
		        alert(w);
		    }
		});
 
		$( ".portlet" ).addClass( "ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" );
        $( ".column" ).disableSelection();
});
