(function ($) {
    let id=$("td:first-child").attr('id');

    console.log(id);
    graph(id);

    var ctx = document.getElementById( "barChartContainer2" );



    $('td').click(function() { //the event happening, table <td> clicked
        let id=$(this).attr('id');
        graph(id)
        console.log(id);
    }) // end of 'td' click


    function graph(id){
        console.log("barchart 2 ajax called");
        data =consumptionRead(id);
        console.log(data);
        chartDraw(id, data[0],data[1]);
    }

    function consumptionRead(id) {
        var data1 = new Array();
        var data2 = new Array();
        $.ajax({
            url : "barchart2",
            type : "get",
            data: {
                'id' : id
            },
            async: false,
            success : function(data) {
                BarPlot2=JSON.parse(data['BarPlot2'])
                BarPlot2Mean=JSON.parse(data['BarPlot2Mean'])
                for(var item in BarPlot2) {
                    data1.push({label:item , y: BarPlot2[item]});
                }
                for(var item2 in BarPlot2Mean) {
                    data2.push({label:item2 , y: BarPlot2Mean[item2]});
                }

            }
        }) //end of $.ajax
        return [data1,data2];
    }

    function chartDraw(id, data1, data2) {
        console.log(id,data1,data2);
        title=id.toString().concat(" Consumption");
        console.log(title);
        var chart = new CanvasJS.Chart("barChartContainer2", {
            animationEnabled: true,
            title:{
                text: title
            },
            axisY: {
                title: "Consumption",
                titleFontColor: "#4F81BC",
                lineColor: "#4F81BC",
                labelFontColor: "#4F81BC",
                tickColor: "#4F81BC"
            },
            axisY2: {
                title: "120D Avg",
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
                name: "Consumption",
                legendText: "Consumption",
                showInLegend: true,
                dataPoints:
                    data1

            },
            {
                type: "line",
                name: "120D avg",
                legendText: "120D Avg",
                axisYType: "secondary",
                showInLegend: true,
                dataPoints: data2
            }]
        });
        chart.render();
    } // end of function



    function toggleDataSeries(e) {
        if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
            e.dataSeries.visible = false;
        }
        else {
            e.dataSeries.visible = true;
        }
        chart.render();
    }

})( jQuery);
