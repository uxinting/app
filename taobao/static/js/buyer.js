$(function() {
	
	$('[href="/buyer"]').parent().addClass('active');
	
	var buyercount;
	$.get('/buyer/ajax?type=buyer', function(jsondata, status) {
		if (typeof(buyercount) != 'undefined') return;
		$('#base-info').text('请稍候，正在请求数据..').show();

		if (status == 'success') {
			$('#base-info').hide();
			
			if (jsondata.indexOf('error') != -1) {
				$('#base-error').text(jsondata);
				return;
			}
			
			buyercount = Morris.Bar({
				element: 'buyercount',
				data: JSON.parse(jsondata),
				xkey: 'buyer_nick',
				ykeys: [ 'sell', 'total_fee' ],
				labels: [ '购买量', '消费金额' ],
				barColors: [ 'blue', 'green' ]
			});
		} else {
			$('#base-error').text('请求数据数据失败！');
		}
	}); //ajax sell get
});