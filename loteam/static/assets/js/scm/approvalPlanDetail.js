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



  $('#Supplier1TableRowAdd').click(function(){
        $("#detailTable1 tbody tr:hidden").first().prop('hidden',false)
  })
  $('#Supplier1TableRowDelete').click(function(){
        $("#detailTable1 tbody tr:visible").last().prop('hidden',true)
  })
  $('#Supplier2TableRowAdd').click(function(){
        $("#detailTable2 tbody tr:hidden").first().prop('hidden',false)
  })
  $('#Supplier2TableRowDelete').click(function(){
        $("#detailTable2 tbody tr:visible").last().prop('hidden',true)
  })
  $('#Supplier3TableRowAdd').click(function(){
        $("#detailTable3 tbody tr:hidden").first().prop('hidden',false)
  })
  $('#Supplier3TableRowDelete').click(function(){
        $("#detailTable3 tbody tr:visible").last().prop('hidden',true)
  })
  $('#Supplier4TableRowAdd').click(function(){
        $("#detailTable4 tbody tr:hidden").first().prop('hidden',false)
  })
  $('#Supplier4TableRowDelete').click(function(){
        $("#detailTable4 tbody tr:visible").last().prop('hidden',true)
  })
  $('#Supplier5TableRowAdd').click(function(){
        $("#detailTable5 tbody tr:hidden").first().prop('hidden',false)
  })
  $('#Supplier5TableRowDelete').click(function(){
        $("#detailTable5 tbody tr:visible").last().prop('hidden',true)
  })
  $('#Supplier6TableRowAdd').click(function(){
        $("#detailTable6 tbody tr:hidden").first().prop('hidden',false)
  })
  $('#Supplier6TableRowDelete').click(function(){
        $("#detailTable6 tbody tr:visible").last().prop('hidden',true)
  })



  $('.supplier1_1').on('input', function () {
    supplierDetailMath(1,1);
  });
  $('.supplier1_2').on('input', function () {
    supplierDetailMath(1,2);
  });
  $('.supplier1_3').on('input', function () {
    supplierDetailMath(1,3);
  });

  $('.supplier2_1').on('input', function () {
    supplierDetailMath(2,1);
  });
  $('.supplier2_2').on('input', function () {
    supplierDetailMath(2,2);
  });
  $('.supplier2_3').on('input', function () {
    supplierDetailMath(2,3);
  });

  $('.supplier3_1').on('input', function () {
    supplierDetailMath(3,1);
  });
  $('.supplier3_2').on('input', function () {
    supplierDetailMath(3,2);
  });
  $('.supplier3_3').on('input', function () {
    supplierDetailMath(3,3);
  });

  $('.supplier4_1').on('input', function () {
    supplierDetailMath(4,1);
  });
  $('.supplier4_2').on('input', function () {
    supplierDetailMath(4,2);
  });
  $('.supplier4_3').on('input', function () {
    supplierDetailMath(4,3);
  });

  $('.supplier5_1').on('input', function () {
    supplierDetailMath(5,1);
  });
  $('.supplier5_2').on('input', function () {
    supplierDetailMath(5,2);
  });
  $('.supplier5_3').on('input', function () {
    supplierDetailMath(5,3);
  });
  $('.supplier6_1').on('input', function () {
    supplierDetailMath(6,1);
  });
  $('.supplier6_2').on('input', function () {
    supplierDetailMath(6,2);
  });
  $('.supplier6_3').on('input', function () {
    supplierDetailMath(6,3);
  });








function supplierDetailMath(supplierNo, detailNo){
    $('#supplier' + supplierNo + 'Nego' + detailNo).text(
        Math.round((
            (parseInt($('#supplier' + supplierNo + 'QuotValue' + detailNo).text())
            - parseInt($('#supplier' + supplierNo + 'FinalValue' +detailNo).text())
            )
            / (parseInt($('#supplier' + supplierNo + 'QuotValue' + detailNo).text())) * 100
        ), 2
    )
  );

  $('#supplier'+supplierNo+'QuotTotalValue'+detailNo).text(
    (parseInt($('#supplier'+supplierNo+'QuotValue'+ detailNo).text()) *  (parseInt($('#supplier'+ supplierNo +'Qty'+detailNo).text())))
  );
  $('#supplier'+supplierNo+'FinalTotalValue'+detailNo).text(
    (parseInt($('#supplier'+supplierNo+'FinalValue'+detailNo).text()) *  (parseInt($('#supplier'+ supplierNo +'Qty' + detailNo).text())))
  );
}




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


















}) //end of function
