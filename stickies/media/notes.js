// Notes
var mle;

$(function() {
		$( ".column" ).sortable({
			connectWith: ".column",
		    stop: function(event, ui){
		        // When done sorting, fire off an ajax call
		        //$.post('/ajax', 
		        mle = ui;
		        var id = ui.item[0].id;
		    }
		});
 
		$( ".portlet" ).addClass( "ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" );
        $( ".column" ).disableSelection();
});
