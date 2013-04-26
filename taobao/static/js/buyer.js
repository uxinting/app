$(function() {
	
	var buyercount;
	$.get('/buyer/ajax?type=sell', function(jsondata, status) {
		if (typeof(buyercount) != 'undefined') return;
		$('#buyercount').append('<p class="alert alert-warn text-center">请稍候,正在请求数据..</p>');

		if (status == 'success') {
			if (jsondata == 'error') {
					$('#buyercount').find('p').text('请求数据失败！');
			}
			
			$('#buyercount').find('p').remove();
			
			buyercount = Morris.Bar({
				element: 'buyercount',
				data: JSON.parse(jsondata),
				xkey: 'buyer_nick',
				ykeys: [ 'sell', 'total_fee' ],
				labels: [ '购买量', '消费金额' ]
			});
		} else {
			$('#buyercount').find('p').text('请求数据数据失败！');
		}
	}); //ajax sell get
});