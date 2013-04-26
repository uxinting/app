$(function() {
	$('[href="/"]').parent().addClass('active');
	$('#base-info').hide();
	$('#base-warn').hide();
	$('#base-error').hide();
	
	var sellcount;
	$.get('/sell/ajax?type=sell', function(jsondata, status) {
		if (typeof(sellcount) != 'undefined') return;
		$('#base-warn').text('请稍候，正在请求数据..').show();

		if (status == 'success') {
			$('#base-warn').hide();
			if (jsondata.indexOf('error') != -1) {
				$('#base-error').text(josndata).show();
			}
			
			sellcount = Morris.Line({
				element: 'sellcount',
				data: JSON.parse(jsondata),
				xkey: 'pay_time',
				ykeys: [ 'sell' ],
				labels: [ '销量' ]
			});
		} else {
			$('#base-error').text('服务器错误').show();
		}
	}); //ajax sell get
	
	var turnovercount;
	$('[href="#turnover"]').click(function() {
		$.get('/sell/ajax?type=turnover', function(jsondata, status) {
			if (typeof(turnovercount) != 'undefined') return;
			$('#base-warn').text('请稍候，正在请求数据..').show();
		
			if (status == 'success') {
				$('#base-warn').hide();
				if (jsondata.indexOf('error') != -1) {
					$('#base-error').text(jsondata).show();
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
				$('#base-error').text('服务器出错').show();
			}
		});
	}); //turnover click

});