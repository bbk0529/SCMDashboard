$(function(){
    $(".detail").css({"cursor":"pointer"})


    $('#supplierSingle'+ 1).click(function(){
      console.log('single1 click')
        $('#supplierSingleReason1').prop("hidden",false)

    })
    $('#supplierMultiple'+1).click(function(){
      console.log('multi1 click')
        $('#supplierSingleReason1').prop("hidden",true)

    })

    $('#supplierSingle2').click(function(){
      console.log('single2 click')
        $('#supplierSingleReason2').prop("hidden",false)

    })
    $('#supplierMultiple2').click(function(){
      console.log('multi1 click')
        $('#supplierSingleReason2').prop("hidden",true)

    })
    $('#supplierSingle3').click(function(){
      console.log('single3 click')
        $('#supplierSingleReason3').prop("hidden",false)

    })
    $('#supplierMultiple3').click(function(){
      console.log('multi1 click')
        $('#supplierSingleReason3').prop("hidden",true)

    })







    $('#btnSupplierDetail1').click(function(){
      console.log("java script called");
      if($('#suppierDetail1').prop('hidden')==false){
        $('#suppierDetail1').prop('hidden', true)

      }
      else{
        $('#suppierDetail1').prop('hidden', false)
      }

    })

    $('#btnSupplierDetail2').click(function(){
      console.log("java script called");
      if($('#suppierDetail2').prop('hidden')==false){
        $('#suppierDetail2').prop('hidden', true)

      }
      else{
        $('#suppierDetail2').prop('hidden', false)
      }

    })

    $('#btnSupplierDetail3').click(function(){
      console.log("java script called");
      if($('#suppierDetail3').prop('hidden')==false){
        $('#suppierDetail3').prop('hidden', true)
      }
      else{
        $('#suppierDetail3').prop('hidden', false)
      }

    })



    $('#copyFromDetail').click(function(){
      console.log("copyfromdetail clicked");
      $('#summaryTable tbody').html("")
      newtr=$('#detailTable1 tbody tr:nth-child(1)').clone();
      newtr.appendTo($('#summaryTable tbody'))
      newtr=$('#detailTable2 tbody tr:nth-child(1)').clone();
      newtr.appendTo($('#summaryTable tbody'))
      newtr=$('#detailTable3 tbody tr:nth-child(1)').clone();
      newtr.appendTo($('#summaryTable tbody'))



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
          'Supplier1'                                  :   $("input[name='Supplier1']").val(),
          'Supplier1_Qty'                              :   $("input[name='Supplier1_Qty']").val(),
          'Supplier1_Final_Unit_Price'                 :   $("input[name='Supplier1_Final_Unit_Price']").val(),
          'Supplier1_Fabricating_Goods'                :   $("input[name='Supplier1_Fabricating_Goods']").val(),
          'Supplier1_Modification_of_free_offerd_item' :   $("input[name='Supplier1_Modification_of_free_offerd_item']").val(),

          'Supplier2'                                  :   $("input[name='Supplier2']").val(),
          'Supplier2_Qty'                              :   $("input[name='Supplier2_Qty']").val(),
          'Supplier2_Final_Unit_Price'                 :   $("input[name='Supplier2_Final_Unit_Price']").val(),
          'Supplier2_Fabricating_Goods'                :   $("input[name='Supplier2_Fabricating_Goods']").val(),
          'Supplier2_Modification_of_free_offerd_item' :   $("input[name='Supplier2_Modification_of_free_offerd_item']").val(),

          'Supplier3'                                  :   $("input[name='Supplier3']").val(),
          'Supplier3_Qty'                              :   $("input[name='Supplier3_Qty']").val(),
          'Supplier3_Final_Unit_Price'                 :   $("input[name='Supplier3_Final_Unit_Price']").val(),
          'Supplier3_Fabricating_Goods'                :   $("input[name='Supplier3_Fabricating_Goods']").val(),
          'Supplier3_Modification_of_free_offerd_item' :   $("input[name='Supplier3_Modification_of_free_offerd_item']").val(),

          'Supplier4'                                  :   $("input[name='Supplier4']").val(),
          'Supplier4_Qty'                              :   $("input[name='Supplier4_Qty']").val(),
          'Supplier4_Final_Unit_Price'                 :   $("input[name='Supplier4_Final_Unit_Price']").val(),
          'Supplier4_Fabricating_Goods'                :   $("input[name='Supplier4_Fabricating_Goods']").val(),
          'Supplier4_Modification_of_free_offerd_item' :   $("input[name='Supplier4_Modification_of_free_offerd_item']").val(),

          'Supplier5'                                  :   $("input[name='Supplier5']").val(),
          'Supplier5_Qty'                              :   $("input[name='Supplier5_Qty']").val(),
          'Supplier5_Final_Unit_Price'                 :   $("input[name='Supplier5_Final_Unit_Price']").val(),
          'Supplier5_Fabricating_Goods'                :   $("input[name='Supplier5_Fabricating_Goods']").val(),
          'Supplier5_Modification_of_free_offerd_item' :   $("input[name='Supplier5_Modification_of_free_offerd_item']").val(),

          'Supplier6'                                  :   $("input[name='Supplier6']").val(),
          'Supplier6_Qty'                              :   $("input[name='Supplier6_Qty']").val(),
          'Supplier6_Final_Unit_Price'                 :   $("input[name='Supplier6_Final_Unit_Price']").val(),
          'Supplier6_Fabricating_Goods'                :   $("input[name='Supplier6_Fabricating_Goods']").val(),
          'Supplier6_Modification_of_free_offerd_item' :   $("input[name='Supplier6_Modification_of_free_offerd_item']").val(),


        }
      })
      console.log( $("input[name='Supplier6_Modification_of_free_offerd_item']").val());
      $('.form-control.query').prop("disabled", true)
      $('#submit').prop("hidden", true)
      $('#header').html(''+
      '<div class="sufee-alert alert with-close alert-secondary alert-dismissible fade show">'+
          '<span class="badge badge-pill badge-primary">Success</span>'+
              'Change has been successfully saved.'+
            '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'+
              '<span aria-hidden="true">&times;</span>'+
          '</button>'+
      '</div>'
      )
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
    });



} ) //end of function
