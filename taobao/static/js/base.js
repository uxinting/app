$(function() {
	
	$('#btn-login').tooltip({
		'animation': true,
		'placement': 'bottom',
		'title': '只有授权成功后才会登录成功',
		'trigger': 'hover focus',
		'delay': 0,
		'container': false
	});
	

	var sellcount = Morris.Line({
	  // ID of the element in which to draw the chart.
	  element: 'sellcount',
	  // Chart data records -- each entry in this array corresponds to a point on
	  // the chart.
	  data: sell_data,
	  goals: [
	  	40
	  ],
	  // The name of the data record attribute that contains x-clothess.
	  xkey: 'time',
	  // A list of names of data record attributes that contain y-clothess.
	  ykeys: ['sum' ],
	  // Labels for the ykeys -- will be displayed when you hover over the
	  // chart.
	  labels: ['日销售量']
	});
	
	var turnovercount;
	$('[href="#turnover"]').click(function() {
		if (typeof(turnovercount) != 'undefined') return;
		$('#turnovercount').append('<p class="alert alert-warn text-center">请稍候,正在处理..</p>');
		
		setTimeout(function() {
			$('#turnovercount').find('p').remove();
			turnovercount = Morris.Line({
				element: 'turnovercount',
				data: turnover_data,
				postUnits: '￥',
				xkey: 'time',
				ykeys: [ 'total_fee' ],
				labels: [ '销售额' ]
			});
		}, 500
		);
	});
});
