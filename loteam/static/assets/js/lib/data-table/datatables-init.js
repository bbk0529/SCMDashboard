(function ($) {
    //    "use strict";



    $('#bootstrap-data-table').DataTable({
        lengthMenu: [[5,10, 20, 50, -1], [5,10, 20, 50, "All"]],
    });



    $('#bootstrap-data-table-export').DataTable({
        dom: 'lBfrtip',
        lengthMenu: [[5, 10, 25, 50], [5, 10, 25, 50]],
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ]
    });

	$('#row-select').DataTable( {
			initComplete: function () {
				this.api().columns().every( function () {
					var column = this;
					var select = $('<select class="form-control"><option value=""></option></select>')
						.appendTo( $(column.footer()).empty() )
						.on( 'change', function () {
							var val = $.fn.dataTable.util.escapeRegex(
								$(this).val()
							);

							column
								.search( val ? '^'+val+'$' : '', true, false )
								.draw();
						} );

					column.data().unique().sort().each( function ( d, j ) {
						select.append( '<option value="'+d+'">'+d+'</option>' )
					} );
				} );
			}
		} );





    $('#bootstrap-data-table-export tfoot th').each( function () {
        var title = $(this).text();
        $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
    } );

    // DataTable
    var table = $('#bootstrap-data-table-export').DataTable();

    // Apply the search
    table.columns().every( function () {
        var that = this;

        $( 'input', this.footer() ).on( 'keyup change', function () {
            if ( that.search() !== this.value ) {
                that
                    .search( this.value )
                    .draw();
            }
        } );
    } );


})(jQuery);
