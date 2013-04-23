$(function() {
	
	$('#btn-login').tooltip({
		'animation': true,
		'placement': 'bottom',
		'title': '只有授权成功后才会登录成功',
		'trigger': 'hover focus',
		'delay': 0,
		'container': false
	});
	

	Morris.Line({
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
	
	$('[href="#turnover"]').click(function() { 
		$('#turnovercount').append('<p>请稍候</p>');
		$.get('/ajax?type=turnover', function(data, status) {
			if (status == 'success') {
			$('#turnovercount').find('p').remove();
				alert(data);
			} else {
				alert('error');
			}
		});
	});
});
