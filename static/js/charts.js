$(function () {
    
        var colors = Highcharts.getOptions().colors,
            categories = [{{test}}, 'Firefox', 'Chrome', 'Safari', 'Opera'],
            name = 'Browser brands',
            data = [{
                    y: 55.11,
                    color: colors[0]
                }, {
                    y: 21.63,
                    color: colors[1]
                }, {
                    y: 11.94,
                    color: colors[2]
                }, {
                    y: 7.15,
                    color: colors[3]
                }, {
                    y: 2.14,
                    color: colors[4]
                }];
    
        function setChart(name, categories, data, color) {
			chart.xAxis[0].setCategories(categories, false);
			chart.series[0].remove(false);
			chart.addSeries({
				name: name,
				data: data,
				color: color || 'white'
			}, false);
			chart.redraw();
        }
    
        var chart = $('#container').highcharts({
            chart: {
                type: 'column'
            },
            title: {
                text: 'Browser market share, April, 2011'
            },
            subtitle: {
                text: 'Click the columns to view versions. Click again to view brands.'
            },
            xAxis: {
                categories: categories
            },
            yAxis: {
                title: {
                    text: 'Total percent market share'
                }
            },
            plotOptions: {
                column: {
                    cursor: 'pointer',
                    point: {
                        events: {
                            click: function() {
                                var drilldown = this.drilldown;
                                if (drilldown) { // drill down
                                    setChart(drilldown.name, drilldown.categories, drilldown.data, drilldown.color);
                                } else { // restore
                                    setChart(name, categories, data);
                                }
                            }
                        }
                    },
                    dataLabels: {
                        enabled: true,
                        color: colors[0],
                        style: {
                            fontWeight: 'bold'
                        },
                        formatter: function() {
                            return this.y +'%';
                        }
                    }
                }
            },
            tooltip: {
                formatter: function() {
                    var point = this.point,
                        s = this.x +':<b>'+ this.y +'% market share</b><br/>';
                    if (point.drilldown) {
                        s += 'Click to view '+ point.category +' versions';
                    } else {
                        s += 'Click to return to browser brands';
                    }
                    return s;
                }
            },
            series: [{
                name: name,
                data: data,
                color: 'white'
            }],
            exporting: {
                enabled: false
            }
        })
        .highcharts(); // return chart
    });
    

