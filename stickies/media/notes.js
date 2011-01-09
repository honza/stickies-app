// Notes

var _id;
var _c;
var _mode;
var _r;

$(function() {

    $('#new-sticky').button();
    $('#new-sticky').click(function(){
        $('#edit-sticky').html(' ');
        _mode = 'new';
        $('#dialog').dialog('open');
        return false;
    });


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
                    a: _mode,
                    project: _project
                }, function(r){
                    _r = r;
                    _r = $.parseJSON(r);
                    if (_r.status == 200){
                        if (_mode == 'edit'){
                            $('#' + _id + ' .portlet-content').children().remove();
                            $('#' + _id + ' .portlet-content').html(_c);
                        } else {
                            // create a new sticky
                            $('#todo').append(_r.content);
                        }
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
                    _r = $.parseJSON(r);
                    if (_r.status != 200){
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
            _mode = 'edit';
            $('#dialog').dialog('open');

		});

        $('.ui-icon-close').click(function(){
            _id = $(this).parent().parent().attr('id');
            $.post('/ajax/', {
                a: 'delete',
                note: _id
                }, function(r){
                    _r = $.parseJSON(r);
                    if (_r.status != 200){
                        alert('Error deleting'); 
                        return;
                    }
                    $('#' + _id).remove();
                });
        });
		
        $( ".column" ).disableSelection();
});
