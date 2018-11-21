$(function(){

    $('#import').click(function(){
        $('.lds-ring').prop('hidden', false)
        console.log("{{uploaded_file_url}}")
        $.ajax({
            url : "import_data_xls",
            type : "GET",
            data: {
                'uploaded_file_url' : "{{uploaded_file_url}}"
            },

            success : function(data) {
                console.log("successfully communicated with Server");
                $('.lds-ring').prop('hidden', true)

              $('#header').html(''+
              '<div class="sufee-alert alert with-close alert-secondary alert-dismissible fade show" id="alert_message">'+
                  '<span class="badge badge-pill badge-primary">Success</span>'+
                  'Assay No : ' +
                   "{{uploaded_file_url}}" +
                      ' Import has been successfully saved.'+
                    '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'+
                      '<span aria-hidden="true">&times;</span>'+
                  '</button>'+
              '</div>'
                )
              window.setTimeout(function() {
                  $("#alert_message").fadeTo(300, 0).slideUp(300, function(){
                    $(this).remove();
                  });
              }, 2000);

          },
          error :function(){
              $('#header').html(''+
              '<div class="sufee-alert alert with-close alert-danger alert-dismissible fade show" id="alert_message">'+
                  '<span class="badge badge-pill badge-danger">Failure</span>'+
                      'Import has NOT been successfully saved. Please contat administrator.'+
                    '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'+
                      '<span aria-hidden="true">&times;</span>'+
                  '</button>'+
              '</div>'
              )
              window.setTimeout(function() {
                  $("#alert_message").fadeTo(300, 0).slideUp(300, function(){
                    $(this).remove();
                  });
              }, 2000);
              $('.lds-ring').prop('hidden', true)
          }
        }) //end of $.ajax
})
})
