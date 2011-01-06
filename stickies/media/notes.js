// Notes
$(function() {
		$( ".column" ).sortable({
			connectWith: ".column"
		});
 
		$( ".portlet" ).addClass( "ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" );
        $( ".column" ).disableSelection();
});
