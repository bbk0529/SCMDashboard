(function ($) {

    var data4 = new Array();    
    $.ajax({
        url : "boxplot",
        type : "get",
        async: false,
        success : function(data) {
            // console.log("JSON load");
            // console.log(data)                       

            
            
            for(var item in data) {               
                
                data4.push({label:item , y: data[item]});
                
            
            }                                
            
        }
    })

    console.table(data4)
    var chart = new CanvasJS.Chart("boxPlotChartContainer", {
        animationEnabled: true,
        title:{
            text: "Lead time in F-KR from HQ per Category"
        },
        axisX: {            
            //valueFormatString: "DDD"
        },
        axisY: {
            title: "Leadtime (In Days)"
        },
        data: [{
           type: "boxAndWhisker",            
            color: "black",
            yValueFormatString: "####",
            dataPoints: data4
        }]
    });
    chart.render();
    console.log(data4)
} )( jQuery );