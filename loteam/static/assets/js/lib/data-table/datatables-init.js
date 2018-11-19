(function ($) {
    //    "use strict";

// <style>
//     .dataTables_filter {
//        float: left !important;
//     }
// </style>

    $('#bootstrap-data-table').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });






    $('#bootstrap-data-table-export').DataTable({
        dom: '  frtipB',
         "paging": false,
        "orderClasses": false,
         "deferRender": true,
        lengthMenu: [[10, 25, 50], [10, 25, 50]],
        buttons: [
            'copy', 'excel',
        ],
        // initComplete: function ()
        // {
        //   var r = $('#bootstrap-data-table-export tfoot tr');
        //   r.find('th').each(function(){
        //     $(this).css('padding', 8);
        //   });
        //   $('#bootstrap-data-table-export thead').append(r);
        //   $('#search_0').css('text-align', 'center');
        // },
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






        // Setup - add a text input to each footer cell
      $('#item tfoot th').each( function () {
          var title = $(this).text();
          $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
      } );

     // DataTable
      var otable = $('#item').DataTable();

      // Apply the search
      otable.columns().every( function () {

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
