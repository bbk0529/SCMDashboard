$(function(){
    $(".detail").css({"cursor":"pointer"})

    $('#supplierSingle'+ 1).click(function(){
        $('#supplierSingleReason1').prop("hidden",false)
    })
    $('#supplierMultiple'+1).click(function(){
        $('#supplierSingleReason1').prop("hidden",true)
    })
    $('#supplierSingle2').click(function(){
        $('#supplierSingleReason2').prop("hidden",false)
    })
    $('#supplierMultiple2').click(function(){
        $('#supplierSingleReason2').prop("hidden",true)
    })
    $('#supplierSingle3').click(function(){
        $('#supplierSingleReason3').prop("hidden",false)
    })
    $('#supplierMultiple3').click(function(){
        $('#supplierSingleReason3').prop("hidden",true)
    })
    $('#supplierSingle4').click(function(){
        $('#supplierSingleReason4').prop("hidden",false)
    })
    $('#supplierMultiple4').click(function(){
        $('#supplierSingleReason4').prop("hidden",true)
    })
    $('#supplierSingle5').click(function(){
        $('#supplierSingleReason5').prop("hidden",false)
    })
    $('#supplierMultiple5').click(function(){
        $('#supplierSingleReason5').prop("hidden",true)
    })
    $('#supplierSingle6').click(function(){
        $('#supplierSingleReason6').prop("hidden",false)
    })
    $('#supplierMultiple6').click(function(){
        $('#supplierSingleReason6').prop("hidden",true)
    })



// Hidden Detail Pop Up or Not
    $('#btnSupplierDetail1').click(function(){
      $('#suppierDetail1').prop('hidden', !$('#suppierDetail1').prop('hidden'))
    })
    $('#btnSupplierDetail2').click(function(){
      $('#suppierDetail2').prop('hidden', !$('#suppierDetail2').prop('hidden'))
    })
    $('#btnSupplierDetail3').click(function(){
      $('#suppierDetail3').prop('hidden', !$('#suppierDetail3').prop('hidden'))
    })
    $('#btnSupplierDetail4').click(function(){
      $('#suppierDetail4').prop('hidden', !$('#suppierDetail4').prop('hidden'))
    })
    $('#btnSupplierDetail5').click(function(){
      $('#suppierDetail5').prop('hidden', !$('#suppierDetail5').prop('hidden'))
    })
    $('#btnSupplierDetail6').click(function(){
      $('#suppierDetail6').prop('hidden', !$('#suppierDetail6').prop('hidden'))
    })



    // $('#copyFromDetail').click(function(){
    //   console.log("copyfromdetail clicked");
    //   $('#summaryTable tbody').html("")
    //   newtr=$('#detailTable1 tbody tr:nth-child(1)').clone();
    //   newtr.appendTo($('#summaryTable tbody'))
    //   newtr=$('#detailTable2 tbody tr:nth-child(1)').clone();
    //   newtr.appendTo($('#summaryTable tbody'))
    //   newtr=$('#detailTable3 tbody tr:nth-child(1)').clone();
    //   newtr.appendTo($('#summaryTable tbody'))
    //   newtr=$('#detailTable4 tbody tr:nth-child(1)').clone();
    //   newtr.appendTo($('#summaryTable tbody'))
    //   newtr=$('#detailTable5 tbody tr:nth-child(1)').clone();
    //   newtr.appendTo($('#summaryTable tbody'))
    //   newtr=$('#detailTable6 tbody tr:nth-child(1)').clone();
    //   newtr.appendTo($('#summaryTable tbody'))
    // })//end of copyFromDetail

    $('#copyFromDetail').click(function(){
      console.log("copyfromdetail clicked");

      var count=0
      for(var i=1;i<=6;i++){
          if ($('#supplier' + i +'Name').text()!=''){
              copyFromDetail(i)
              $('#summaryTable tr:nth-child('+ i +')').prop('hidden',false)
              count+=1
              console.log(i);
          }
         $('input[name="Number_of_suppliers"]').val(count);
      }


      function copyFromDetail(supplierNo){
          $('#Supplier' + supplierNo).text($('#supplier'+ supplierNo+'Name').text())
          $('#Supplier' + supplierNo + '_Qty').text($('#supplier' + supplierNo +'Qty1').text())
          $('#supplier'+ supplierNo +'QuotValue').text($('#supplier'+ supplierNo +'QuotValue1').text())
          $('#supplierQuotTotalValue' + supplierNo).text($('#supplier'+supplierNo+'QuotTotalValue1').text())
          $('#Supplier'+supplierNo+'_Final_Unit_Price').text($('#supplier'+supplierNo+'FinalValue1').text())
          $('#supplierFinalTotalValue'+supplierNo).text($('#supplier'+supplierNo+'FinalTotalValue1').text())
          $('#supplier'+supplierNo+'Nego').text($('#supplier'+supplierNo+'Nego1').text())
      }

    })//end of copyFromDetail

















    $('#save').click(function(){
      console.log("save clicked");
      $.ajax({
          url:"updateQuery",
          type:"POST",
          data:{
              'csrfmiddlewaretoken': '{{csrf_token}}',
              'SA_No' : $("input[name='SA_No']").val(),
              'Type' : $("input[name='Type']").val(),
              'Date' : $("input[name='Date']").val(),
              'Number_of_suppliers' : $("input[name='Number_of_suppliers']").val(),
              'Details_1' : $("input[name='Details_1']").val(),
              'Details_2' : $("input[name='Details_2']").val(),
              'Supplier1'                                  :   $("#Supplier1").text(),
              'Supplier1_Qty'                              :   $("#Supplier1_Qty").text(),
              'Supplier1_Final_Unit_Price'                 :   $("#Supplier1_Final_Unit_Price").text(),
              'Supplier1_Fabricating_Goods'                :   $("#Supplier1_Fabricating_Goods").val(),
              'Supplier1_Modification_of_free_offerd_item' :   $("#Supplier1_Modification_of_free_offerd_item").val(),

              'Supplier2'                                  :   $("#Supplier2").text(),
              'Supplier2_Qty'                              :   $("#Supplier2_Qty").text(),
              'Supplier2_Final_Unit_Price'                 :   $("#Supplier2_Final_Unit_Price").text(),
              'Supplier2_Fabricating_Goods'                :   $("#Supplier2_Fabricating_Goods").val(),
              'Supplier2_Modification_of_free_offerd_item' :   $("#Supplier2_Modification_of_free_offerd_item").val(),

              'Supplier3'                                  :   $("#Supplier3").text(),
              'Supplier3_Qty'                              :   $("#Supplier3_Qty").text(),
              'Supplier3_Final_Unit_Price'                 :   $("#Supplier3_Final_Unit_Price").text(),
              'Supplier3_Fabricating_Goods'                :   $("#Supplier3_Fabricating_Goods").val(),
              'Supplier3_Modification_of_free_offerd_item' :   $("#Supplier3_Modification_of_free_offerd_item").val(),

              'Supplier4'                                  :   $("#Supplier4").text(),
              'Supplier4_Qty'                              :   $("#Supplier4_Qty").text(),
              'Supplier4_Final_Unit_Price'                 :   $("#Supplier4_Final_Unit_Price").text(),
              'Supplier4_Fabricating_Goods'                :   $("#Supplier4_Fabricating_Goods").val(),
              'Supplier4_Modification_of_free_offerd_item' :   $("#Supplier4_Modification_of_free_offerd_item").val(),

              'Supplier5'                                  :   $("#Supplier5").text(),
              'Supplier5_Qty'                              :   $("#Supplier5_Qty").text(),
              'Supplier5_Final_Unit_Price'                 :   $("#Supplier5_Final_Unit_Price").text(),
              'Supplier5_Fabricating_Goods'                :   $("#Supplier5_Fabricating_Goods").val(),
              'Supplier5_Modification_of_free_offerd_item' :   $("#Supplier5_Modification_of_free_offerd_item").val(),

              'Supplier6'                                  :   $("#Supplier6").text(),
              'Supplier6_Qty'                              :   $("#Supplier6_Qty").text(),
              'Supplier6_Final_Unit_Price'                 :   $("#Supplier6_Final_Unit_Price").text(),
              'Supplier6_Fabricating_Goods'                :   $("#Supplier6_Fabricating_Goods").val(),
              'Supplier6_Modification_of_free_offerd_item' :   $("#Supplier6_Modification_of_free_offerd_item").val(),
          },
          success:function(data){
               // location.reload();


              $('#header').html(''+
              '<div class="sufee-alert alert with-close alert-secondary alert-dismissible fade show" id="alert_message">'+
                  '<span class="badge badge-pill badge-primary">Success</span>'+
                  'Assay No : ' +
                   $("input[name='SA_No']").val() +
                      ' Change has been successfully saved.'+
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
              // $("#approvalPlanHeader").html(data)
          },
          error :function(){
              $('#header').html(''+
              '<div class="sufee-alert alert with-close alert-danger alert-dismissible fade show" id="alert_message">'+
                  '<span class="badge badge-pill badge-danger">Failure</span>'+
                      'Change has NOT been successfully saved. SA Number is not given or server is not working properly'+
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
          }

      })
    }) // end of save




    $('#radio_create').click(function(){
      console.log('clicked radio_create')
      $('#newDocOptions').prop('hidden',false)
      $('#changeDocOptions').prop('hidden',true)
      $.ajax({
        url : "approvalPlanCreate",
        type : "GET",
        success : function(data) {
            console.log("successfully communicated with Server");
            $("#approvalPlanQuery").html(
              data
            );
        }
      })
    })

    toggle=true
    $('#disableToggle').click(function(){
      console.log("clicked query/Change")

      $('#header').html("");
      if(toggle==true){
        $('.form-control.query').prop("disabled", false)
        $('td').prop("contenteditable", true)
        $('#submit').prop("hidden", false)
        toggle=false
        console.log(toggle)
      }
      else {
        $('.form-control.query').prop("disabled", true)
        $('#submit').prop("hidden", true)
        $('td').prop("contenteditable",false)
        toggle=true
        console.log(toggle)
      }


    })

    $('#check').click(function(){
      console.log("clicked//")
      var assayNo=$("#assayNo").val()
      if (assayNo!='') {
          $('#radio_change').prop('checked', true)
          $('#changeDocOptions').prop('hidden', false);
          $('#newDocOptions').prop('hidden', true);
          console.log(assayNo);
          $.ajax({
              url : "approvalPlanQuery",
              type : "GET",
              data: {
                  'SA_No' : assayNo
              },
              success : function(data) {
                  console.log("successfully communicated with Server");
                  $("#approvalPlanQuery").html(
                    data
                  );
              }
          }) //end of $.ajax
      }

    });



} ) //end of function
