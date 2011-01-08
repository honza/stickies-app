// Notes

var _id;
var _c;

$(function() {


    $('#dialog').dialog({
        autoOpen: false,
        height: 300,
        width: 600,
        modal: true,
        buttons: {
            "Save": function(){
                _c = $('#edit-sticky').val();
                $.post('/ajax/', {
                    note: _id,
                    content: _c,
                    a: 'edit'
                }, function(r){
                    if (r == 'OK'){
                        $('#' + _id + ' .portlet-content').children().remove();
                        $('#' + _id + ' .portlet-content').html(_c);
                        $('#dialog').dialog('close');
                    }
            } // response fn
            ); // post
        }
        } // buttons
        }); // dialog



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
                    section: w,
                    a: 'move'
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
		// connect icon buttons
		$('.ui-icon-pencil').click(function(){
            _id = $(this).parent().parent().attr('id');
            var cont = $(this).parent().next().html();
            $('#edit-sticky').html('').html(cont);
            $('#dialog').dialog('open');

		});
        $( ".column" ).disableSelection();
});
