$(function(){

//Mouse Cursor on Supplier Detail
    $(".detail").css({"cursor":"pointer"})



//Detail table rows added deleted
$('.tableRowAddSupplier').click(function(){
    var num=$(this).prop('id').slice(-1,)
    console.log(num);
    $("#detailTableSupplier" + num +" tbody tr:hidden").first().prop('hidden',false)
    $("#summaryTableSupplier" + num).prop('hidden',false)
    $("#Number_of_suppliers").val(
           $('#summaryTable tbody tr:visible').length
    )
 })

 $('.tableRowDeleteSupplier').click(function(){
     var num=$(this).prop('id').slice(-1,)
     console.log(num);
     $("#detailTableSupplier"+num +" tbody tr:visible").last().prop('hidden',true)
     if ($("#detailTableSupplier"+num+" tbody tr:visible").length==0){
         $("#summaryTableSupplier"+num).prop('hidden',true)
     }
 })


////////////////////////////////////////////////////////////////////////////////
// Supplier1
////////////////////////////////////////////////////////////////////////////////
// in approvalPlanDetailSupplierx.html   -        Single, Muliple
    $('#singleSupplier1').click(function(){
        $('#singleReasonSupplier1').prop("hidden",false)
    })
    $('#multipleSupplier1').click(function(){
        $('#singleReasonSupplier1').prop("hidden",true)
    })
//  Hidden Detail Pop Up or Not
    $('#btnDetailSupplier1').click(function(){
      $('#detailSupplier1').prop('hidden', !$('#detailSupplier1').prop('hidden'))
    })



//Detail Math, automatically calculation
    $('.Supplier1_1').on('input', function () {
      console.log('Supplier1_1 input')
      supplierDetailMath(1,1);
      copyFromDetail(1,1)
    });
    $('.Supplier1_2').on('input', function () {
      supplierDetailMath(1,2);
    });
    $('.Supplier1_3').on('input', function () {
      supplierDetailMath(1,3);
    });


////////////////////////////////////////////////////////////////////////////////
// Supplier2
////////////////////////////////////////////////////////////////////////////////
// in approvalPlanDetailSupplierx.html   -        Single, Muliple
    $('#singleSupplier2').click(function(){
        $('#singleReasonSupplier2').prop("hidden",false)
    })
    $('#multipleSupplier2').click(function(){
        $('#singleReasonSupplier2').prop("hidden",true)
    })
//  Hidden Detail Pop Up or Not
    $('#btnDetailSupplier2').click(function(){
      $('#detailSupplier2').prop('hidden', !$('#detailSupplier2').prop('hidden'))
    })

//Detail Math, automatically calculation
    $('.Supplier2_1').on('input', function () {
      console.log('Supplier2_1 input')
      supplierDetailMath(2,1);
      copyFromDetail(2,1)
    });
    $('.Supplier2_2').on('input', function () {
      supplierDetailMath(2,2);
    });
    $('.Supplier2_3').on('input', function () {
      supplierDetailMath(2,3);
    });


////////////////////////////////////////////////////////////////////////////////
// Supplier3
////////////////////////////////////////////////////////////////////////////////
// in approvalPlanDetailSupplierx.html   -        Single, Muliple
    $('#singleSupplier3').click(function(){
        $('#singleReasonSupplier3').prop("hidden",false)
    })
    $('#multipleSupplier3').click(function(){
        $('#singleReasonSupplier3').prop("hidden",true)
    })
//  Hidden Detail Pop Up or Not
    $('#btnDetailSupplier3').click(function(){
      $('#detailSupplier3').prop('hidden', !$('#detailSupplier3').prop('hidden'))
    })

//Detail Math, automatically calculation
    $('.Supplier3_1').on('input', function () {
      console.log('Supplier3_1 input')
      supplierDetailMath(3,1);
      copyFromDetail(3,1)
    });
    $('.Supplier3_2').on('input', function () {
      supplierDetailMath(3,2);
    });
    $('.Supplier3_3').on('input', function () {
      supplierDetailMath(3,3);
    });


////////////////////////////////////////////////////////////////////////////////
// Supplier4
////////////////////////////////////////////////////////////////////////////////
// in approvalPlanDetailSupplierx.html   -        Single, Muliple
    $('#singleSupplier4').click(function(){
        $('#singleReasonSupplier4').prop("hidden",false)
    })
    $('#multipleSupplier4').click(function(){
        $('#singleReasonSupplier4').prop("hidden",true)
    })
//  Hidden Detail Pop Up or Not
    $('#btnDetailSupplier4').click(function(){
      $('#detailSupplier4').prop('hidden', !$('#detailSupplier4').prop('hidden'))
    })

//Detail Math, automatically calculation
    $('.Supplier4_1').on('input', function () {
      console.log('Supplier4_1 input')
      supplierDetailMath(4,1);
      copyFromDetail(4,1)
    });
    $('.Supplier4_2').on('input', function () {
      supplierDetailMath(4,2);
    });
    $('.Supplier4_3').on('input', function () {
      supplierDetailMath(4,3);
    });


////////////////////////////////////////////////////////////////////////////////
// Supplier5
////////////////////////////////////////////////////////////////////////////////
// in approvalPlanDetailSupplierx.html   -        Single, Muliple
    $('#singleSupplier5').click(function(){
        $('#singleReasonSupplier5').prop("hidden",false)
    })
    $('#multipleSupplier5').click(function(){
        $('#singleReasonSupplier5').prop("hidden",true)
    })
//  Hidden Detail Pop Up or Not
    $('#btnDetailSupplier5').click(function(){
      $('#detailSupplier5').prop('hidden', !$('#detailSupplier5').prop('hidden'))
    })

//Detail Math, automatically calculation
    $('.Supplier5_1').on('input', function () {
      console.log('Supplier5_1 input')
      supplierDetailMath(5,1);
      copyFromDetail(5,1)
    });
    $('.Supplier5_2').on('input', function () {
      supplierDetailMath(5,2);
    });
    $('.Supplier5_3').on('input', function () {
      supplierDetailMath(5,3);
    });

////////////////////////////////////////////////////////////////////////////////
// Supplier6
////////////////////////////////////////////////////////////////////////////////
// in approvalPlanDetailSupplierx.html   -        Single, Muliple
    $('#singleSupplier6').click(function(){
        $('#singleReasonSupplier6').prop("hidden",false)
    })
    $('#multipleSupplier6').click(function(){
        $('#singleReasonSupplier6').prop("hidden",true)
    })
//  Hidden Detail Pop Up or Not
    $('#btnDetailSupplier6').click(function(){
      $('#detailSupplier6').prop('hidden', !$('#detailSupplier6').prop('hidden'))
    })

//Detail Math, automatically calculation
    $('.Supplier6_1').on('input', function () {
      console.log('Supplier6_1 input')
      supplierDetailMath(6,1);
      copyFromDetail(6,1)
    });
    $('.Supplier6_2').on('input', function () {
      supplierDetailMath(6,2);
    });
    $('.Supplier6_3').on('input', function () {
      supplierDetailMath(6,3);
    });

////////////////////////////////////////////////////////////////////////////////
// Supplier7
////////////////////////////////////////////////////////////////////////////////
// in approvalPlanDetailSupplierx.html   -        Single, Muliple
    $('#singleSupplier7').click(function(){
        $('#singleReasonSupplier7').prop("hidden",false)
    })
    $('#multipleSupplier7').click(function(){
        $('#singleReasonSupplier7').prop("hidden",true)
    })
//  Hidden Detail Pop Up or Not
    $('#btnDetailSupplier7').click(function(){
      $('#detailSupplier7').prop('hidden', !$('#detailSupplier7').prop('hidden'))
    })

//Detail Math, automatically calculation
    $('.Supplier7_1').on('input', function () {
      console.log('Supplier7_1 input')
      supplierDetailMath(7,1);
      copyFromDetail(7,1)
    });
    $('.Supplier7_2').on('input', function () {
      supplierDetailMath(7,2);
    });
    $('.Supplier7_3').on('input', function () {
      supplierDetailMath(7,3);
    });

////////////////////////////////////////////////////////////////////////////////
// Supplier8
////////////////////////////////////////////////////////////////////////////////
// in approvalPlanDetailSupplierx.html   -        Single, Muliple
    $('#singleSupplier8').click(function(){
        $('#singleReasonSupplier8').prop("hidden",false)
    })
    $('#multipleSupplier8').click(function(){
        $('#singleReasonSupplier8').prop("hidden",true)
    })
//  Hidden Detail Pop Up or Not
    $('#btnDetailSupplier8').click(function(){
      $('#detailSupplier8').prop('hidden', !$('#detailSupplier8').prop('hidden'))
    })

//Detail Math, automatically calculation
    $('.Supplier8_1').on('input', function () {
      console.log('Supplier8_1 input')
      supplierDetailMath(8,1);
      copyFromDetail(8,1)
    });
    $('.Supplier8_2').on('input', function () {
      supplierDetailMath(8,2);
    });
    $('.Supplier8_3').on('input', function () {
      supplierDetailMath(8,3);
    });










function supplierDetailMath(supplierNo, detailNo){
    console.log('supplierDetailMath')
    $('#negoSupplier' + supplierNo + '_' + detailNo).text(
        Math.round((
            (parseInt($('#quotValueSupplier' + supplierNo +'_' + detailNo).val())
            - parseInt($('#finalValueSupplier'  + supplierNo + '_'+ detailNo).val())
            )
            / (parseInt($('#quotValueSupplier' + supplierNo + '_' + detailNo).val())) * 100
        ), 2
    )
  );

  $('#quotTotalValueSupplier'+ supplierNo + '_'+detailNo).text(
    (parseInt($('#quotValueSupplier' + supplierNo +'_' + detailNo).val()) *  (parseInt($('#qtySupplier'+ supplierNo +'_'+detailNo).val())))
  );
  $('#finalTotalValueSupplier'+supplierNo+'_'+detailNo).text(
    (parseInt($('#finalValueSupplier' + supplierNo +'_' + detailNo).val()) *  (parseInt($('#qtySupplier'+ supplierNo +'_'+detailNo).val())))
  );

}


function copyFromDetail(supplierNo, detailNo){
    $('#Supplier'+ supplierNo).text($('#nameSupplier'+ supplierNo).val());
    $('#Supplier'+ supplierNo +'_Qty').text($('#qtySupplier'+ supplierNo +'_' + detailNo).val());
    $('#supplier'+ supplierNo +'QuotValue').text($('#quotValueSupplier'+ supplierNo +'_' + detailNo).val());
    $('#supplierQuotTotalValue'+ supplierNo).text($('#quotTotalValueSupplier'+ supplierNo +'_' + detailNo).text())
    $('#Supplier'+ supplierNo +'_Final_Unit_Price').text($('#finalValueSupplier'+ supplierNo +'_' + detailNo).val())
    $('#supplierFinalTotalValue'+ supplierNo).text($('#finalTotalValueSupplier'+ supplierNo +'_' + detailNo).text())
    $('#supplier'+ supplierNo +'Nego').text($('#negoSupplier'+ supplierNo +'_' + detailNo).text())

}

$('textarea').each(function () {

    if ($(this).parent().parent().parent().prop('hidden')==true){
        height=50
        console.log("hidden",height)
    }
    else{
        height=this.scrollHeight
        console.log("Not hidden",height)
    }
   this.setAttribute('style', 'height:' + (height) + 'px;overflow-y:hidden;');
   // this.setAttribute('style', 'overflow-y:hidden;');
}).on('input', function () {
  this.style.height = 'auto';
  this.style.height = (this.scrollHeight) + 'px';
});



}) //end of function
