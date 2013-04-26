$(function() {

	$('[href="/"]').parent().addClass('active');

	var sellcount;
	$.get('/sell/ajax?type=sell', function(jsondata, status) {
		if (typeof(sellcount) != 'undefined') return;
		$('#base-info').text('请稍候,正在请求数据..').show();

		if (status == 'success') {
			$('#base-info').hide();
			if (jsondata.indexOf('error') != -1) {
				$('#base-error').text('请求数据失败！').show();
			}
			
			sellcount = Morris.Line({
				element: 'sellcount',
				data: JSON.parse(jsondata),
				xkey: 'pay_time',
				ykeys: [ 'sell' ],
				labels: [ '销量' ]
			});
		} else {
			$('#base-error').text('请求数据数据失败！').show();
		}
	}); //ajax sell get
	
	var turnovercount;
	$('[href="#turnover"]').click(function() {
		$.get('/sell/ajax?type=turnover', function(jsondata, status) {
			if (typeof(turnovercount) != 'undefined') return;
			$('#base-info').text('请稍候,正在请求数据..').show();
		
			if (status == 'success') {
				$('#base-info').hide();
				if (jsondata.indexOf('error') != -1) {
					$('#base-error').text('请求数据失败！').show();
				}
				
				turnovercount = Morris.Line({
					element: 'turnovercount',
					data: JSON.parse(jsondata),
					postUnits: '￥',
					xkey: 'pay_time',
					ykeys: [ 'turnover' ],
					labels: [ '销售额' ]
				});
			} else {
				$('#base-error').text('请求数据数据失败！').show();
			}
		});
	}); //turnover click

});