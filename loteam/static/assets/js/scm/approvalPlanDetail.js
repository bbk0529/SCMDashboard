$(function(){

  $('table td').on('input', function () {
    // console.log($(this).text());
    var nego1=parseInt($('#quot1Value').text()) / parseInt($('#final1Value').text())
    $('#nego1').text(nego1);

  });
} ) //end of function
