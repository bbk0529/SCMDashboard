$(function(){

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

}) //end of function
