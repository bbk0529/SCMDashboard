(function ($) {

    var data4 = new Array();    
    var data2 = new Array();
    console.log("ajax called");
    $.ajax({
        url : "barchart",
        type : "get",
        async: false,
        success : function(data) {
            console.log("JSON load successfully");
            console.log(data)                       
            
            for(var item in data) {               
                
                data4.push({label:item , y: data[item]});
                data2.push({label:item , y: data[item]-Math.floor(Math.random() * data[item])});
                
            
            }                                
            
        }
    })

    console.log(data4)
    var chart = new CanvasJS.Chart("barChartContainer", {
        animationEnabled: true,
        title:{
            text: "Leadtime per Category"
        },	
        axisY: {
            title: "Planned Leadtime",
            titleFontColor: "#4F81BC",
            lineColor: "#4F81BC",
            labelFontColor: "#4F81BC",
            tickColor: "#4F81BC"
        },
        axisY2: {
            title: "Actual Leadtime",
            titleFontColor: "#C0504E",
            lineColor: "#C0504E",
            labelFontColor: "#C0504E",
            tickColor: "#C0504E"
        },	
        toolTip: {
            shared: true
        },
        legend: {
            cursor:"pointer",
            itemclick: toggleDataSeries
        },
        data: [{
            type: "column",
            name: "Planned Leadtime",
            legendText: "Planned",
            showInLegend: true, 
            dataPoints:
                data4
            
        },
        {
            type: "column",	
            name: "Actual Leadtime",
            legendText: "Actual",
            axisYType: "secondary",
            showInLegend: true,
            dataPoints: data2                
        }]
    });
    chart.render();

    function toggleDataSeries(e) {
        if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
            e.dataSeries.visible = false;
        }
        else {
            e.dataSeries.visible = true;
        }
        chart.render();
    }

})( jQuery );