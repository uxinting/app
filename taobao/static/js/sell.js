$(function() {

	var sellcount;
	$.get('/sell/ajax?type=sell', function(jsondata, status) {
		if (typeof(sellcount) != 'undefined') return;
		$('#sellcount').append('<p class="alert alert-warn text-center">请稍候,正在请求数据..</p>');

		if (status == 'success') {
			if (jsondata == 'error') {
					$('#turnovercount').find('p').text('请求数据失败！');
			}
			
			$('#sellcount').find('p').remove();
			
			sellcount = Morris.Line({
				element: 'sellcount',
				data: JSON.parse(jsondata),
				xkey: 'pay_time',
				ykeys: [ 'sell' ],
				labels: [ '销量' ]
			});
		} else {
			$('#sellcount').find('p').text('请求数据数据失败！');
		}
	}); //ajax sell get
	
	var turnovercount;
	$('[href="#turnover"]').click(function() {
		$.get('/ajax?type=turnover', function(jsondata, status) {
			if (typeof(turnovercount) != 'undefined') return;
			$('#turnovercount').append('<p class="alert alert-warn text-center">请稍候,正在请求数据..</p>');
		
			if (status == 'success') {
				if (jsondata == 'error') {
					$('#turnovercount').find('p').text('请求数据失败！');
				}
				
				$('#turnovercount').find('p').remove();
				
				turnovercount = Morris.Line({
					element: 'turnovercount',
					data: JSON.parse(jsondata),
					postUnits: '￥',
					xkey: 'pay_time',
					ykeys: [ 'turnover' ],
					labels: [ '销售额' ]
				});
			} else {
				$('#turnovercount').find('p').text('请求数据数据失败！');
			}
		});
	}); //turnover click

});