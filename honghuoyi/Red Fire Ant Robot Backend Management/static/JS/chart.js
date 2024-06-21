;
// 温度湿度折线图
var chartDom1 = document.getElementById('1');
var myChart1 = echarts.init(chartDom1);
var option1;

option1 = {
    title: {
        text: '温度&湿度'
    },
    dataZoom: [{
        type: 'slider',
        show: true, //flase直接隐藏图形
        xAxisIndex: [0],
        left: '10%', //滚动条靠左侧的百分比
        bottom: -1,
        start: 0,//滚动条的起始位置
        end: 100 //滚动条的截止位置（按比例分割你的柱状图x轴长度）
    }],
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            crossStyle: {
                color: '#999'
            }
        }
    },
    toolbox: {
        feature: {
            dataView: { show: true, readOnly: false },
            magicType: { show: true, type: ['line', 'bar'] },
            restore: { show: true },
            saveAsImage: { show: true }
        }
    },
    legend: {
        data: ['湿度', '温度']
    },
    xAxis: [
        {
            type: 'category',
            data: ['10-01', '10-02', '10-03', '10-04', '10-05', '10-06', '10-07'],
            axisPointer: {
                type: 'shadow'
            }
        }
    ],
    yAxis: [
        {
            type: 'value',
            name: '湿度',
            min: 0,
            max: 100,
            interval: 20,
            axisLabel: {
                formatter: '{value} %'
            }
        },
        {
            type: 'value',
            name: '温度',
            min: -10,
            max: 40,
            interval: 10,
            axisLabel: {
                formatter: '{value} °C'
            }
        }
    ],
    series: [
        {
            name: '湿度',
            type: 'bar',
            tooltip: {
                valueFormatter: function (value) {
                    return value + ' %';
                }
            },
            data: [
                20.6, 5.9, 9.0, 26.4, 28.7, 70.7, 75.6, 82.2, 48.7, 18.8, 6.0, 20.3
            ]
        },
        {
            name: '温度',
            type: 'line',
            yAxisIndex: 1,
            tooltip: {
                valueFormatter: function (value) {
                    return value + ' °C';
                }
            },
            data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
        }
    ]
};

myChart1.setOption(option1);

//光照强度and光谱频段
var chartDom2 = document.getElementById('2');
var myChart2 = echarts.init(chartDom2);
var option2 = {
    title: {
        text: '光强&光谱频段'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['光照强度', '光谱频段', ]
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['10-01', '10-02', '10-03', '10-04', '10-05', '10-06', '10-07']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: '光照强度',
            type: 'line',
           
            data: [120, 132, 101, 134, 90, 230, 210]
        },
        {
            name: '光谱频段',
            type: 'line',
            
            data: [220, 182, 191, 234, 290, 330, 310]
        },
        
    ]
};

myChart2.setOption(option2);

//含水量与PH值
var chartDom3 = document.getElementById('3');
var myChart3 = echarts.init(chartDom3);
var option3;

option3 = {
    dataZoom: [{
        type: 'slider',
        show: true, //flase直接隐藏图形
        xAxisIndex: [0],
        left: '10%', //滚动条靠左侧的百分比
        bottom: -1,
        start: 0,//滚动条的起始位置
        end: 100 //滚动条的截止位置（按比例分割你的柱状图x轴长度）
    }],
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            crossStyle: {
                color: '#999'
            }
        }
    },
    toolbox: {
        feature: {
            dataView: { show: true, readOnly: false },
            magicType: { show: true, type: ['line', 'bar'] },
            restore: { show: true },
            saveAsImage: { show: true }
        }
    },
    legend: {
        data: ['含水量', 'PH值']
    },
    xAxis: [
        {
            type: 'category',
            data: ['10-01', '10-02', '10-03', '10-04', '10-05', '10-06', '10-07'],
            axisPointer: {
                type: 'shadow'
            }
        }
    ],
    yAxis: [
        {
            type: 'value',
            name: '含水量',
            min: 0,
            max: 100,
            interval: 20,
            axisLabel: {
                formatter: '{value} %'
            }
        },
        {
            type: 'value',
            name: 'PH值',
            min: 0,
            max: 14,
            interval: 2,
            axisLabel: {
                formatter: '{value} °C'
            }
        }
    ],
    series: [
        {
            name: '含水量',
            type: 'bar',
            tooltip: {
                valueFormatter: function (value) {
                    return value + ' %';
                }
            },
            data: [
                20.6, 50.9, 39.0, 26.4, 28.7, 70.7, 75.6, 82.2, 48.7, 18.8, 60.0, 20.3
            ]
        },
        {
            name: 'PH值',
            type: 'line',
            yAxisIndex: 1,
            tooltip: {
                valueFormatter: function (value) {
                    return value + ' °C';
                }
            },
            data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 10.3, 13.4, 13.0, 11.5, 12.0, 6.2]
        }
    ]
};

myChart3.setOption(option3);

//各种土壤元素含量折线图
var chartDom4 = document.getElementById('4');
var myChart4 = echarts.init(chartDom4);
var option4 = {
    title: {
        text: '元素含量图'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['N', 'P', 'S', 'K', 'Ca']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['10-01', '10-02', '10-03', '10-04', '10-05', '10-06', '10-07']
    },
    yAxis: {
        type: 'value',
        name: '含量',
        min: 0,
        max: 400,
        interval: 50,
    },
    series: [
        {
            name: 'N',
            type: 'line',

            data: [120, 132, 101, 134, 90, 230, 210]
        },
        {
            name: 'P',
            type: 'line',

            data: [220, 182, 191, 234, 290, 330, 310]
        },
        {
            name: 'S',
            type: 'line',

            data: [200, 142, 196, 234, 296, 260, 310]
        },
        {
            name: 'K',
            type: 'line',

            data: [210, 189, 156, 252, 268, 300, 284]
        },
        {
            name: 'Ca',
            type: 'line',

            data: [160, 189, 220, 259, 258, 150, 320]
        }
    ]
};

myChart4.setOption(option4);


$(".wrap>.head").click(
    // $(".wrap>.item").toggle()
    $(".wrap")
)