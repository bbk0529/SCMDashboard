$(function(){
      $('#check').click(function(){
          var assayNo=$("#assayNo").val()
          query(assayNo)
      }); //end of #check click

      $("#assayNo").keypress(function(event) {
          if (event.keyCode === 13) {
              console.log('enter key in')
              var assayNo=$("#assayNo").val()
              query(assayNo)
          }
      });

      function query(assayNo){
      $.ajax({
              url : "assayQuery",
              type : "get",
              data: {
                'SA_No' : assayNo
                },
            // async: false,
            success : function(data) {
                console.log("successfully communicated with Server");
                // console.log(data);
                $("#result").html(
                  ""
                );
                $("#result").html(
                  data
                );
            }
        }) //end of $.ajax
    }

  });
