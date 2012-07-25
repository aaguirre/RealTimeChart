var chart;

$(document).ready(function() {
	Highcharts.setOptions({
		global: {
			useUTC: false
		}
	});

	chart = new Highcharts.Chart({
		chart: {
			renderTo: 'container',
			type: 'spline',
			marginRight: 10,
		},
		title: {
			text: 'CPU Usage'
		},
		xAxis: {
			type: 'datetime',
                        tickPixelInterval: 150,
                        gridLineWidth: 1,
		},
		yAxis: {
			title: {
				text: 'Value'
			},
                        min: 0,
                        max:100,
			plotLines: [{
				value: 0,
				width: 1,
				color: '#808080'
			}]
		},
		tooltip: {
			formatter: function() {
					return '<b>'+ this.series.name +'</b><br/>'+
					Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) +'<br/>'+
					Highcharts.numberFormat(this.y, 2);
			}
		},
		legend: {
			enabled: false
		},
		exporting: {
			enabled: false
		},
 		plotOptions: {
			spline: {
				lineWidth: 2,
				states: {
					hover: {
						lineWidth: 3
					}
				},
				marker: {
					enabled: false,
				},
                        },
                        line: {
                            marker: { enabled: false }
                        }
		},
		series: [{
			name: 'Random data',
			data: (function() {
				var data = [],
					time = (new Date()).getTime(),
					i;

				for (i = -19; i <= 0; i++) {
					data.push({
						x: time + i * 1000,
						y: 0
					});
				}
				return data;
			})()
		}]
	});


        var socket = io.connect('/message');

        socket.on("showdata",function(e){
           console.log(e);
           var x = (new Date()).getTime(); 
           var y = e.point
           chart.series[0].addPoint([x, y], true, true);
        });

        socket.emit("message", 'start');

});
