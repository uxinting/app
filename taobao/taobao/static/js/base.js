$(function() {
	new Morris.Line({
	  // ID of the element in which to draw the chart.
	  element: 'all',
	  // Chart data records -- each entry in this array corresponds to a point on
	  // the chart.
	  data: [
		{ time: '2013-1', clothes: 20, shoes: 25 },
		{ time: '2013-2', clothes: 10, shoes: 12 },
		{ time: '2013-2-15', clothes: 50, shoes: 20},
		{ time: '2013-3', clothes: 5, shoes: 1 },
		{ time: '2013-4', clothes: 23, shoes: 9},
		{ time: '2013-5', clothes: 5, shoes: 4 },
		{ time: '2013-6', clothes: 20, shoes: 34 }
	  ],
	  goals: [
	  	40
	  ],
	  events: [
	  	'2013-2-14', '2013-5-1'
	  ],
	  // The name of the data record attribute that contains x-clothess.
	  xkey: 'time',
	  // A list of names of data record attributes that contain y-clothess.
	  ykeys: ['clothes', 'shoes'],
	  // Labels for the ykeys -- will be displayed when you hover over the
	  // chart.
	  labels: ['clothes', 'shoes'],
	  smooth: false
	});
});