$(function() {
	
	$('#btn-login').tooltip({
		'animation': true,
		'placement': 'bottom',
		'title': '只有授权成功后才会登录成功',
		'trigger': 'hover focus',
		'delay': 0,
		'container': false
	}); //tooltip
	
	$('#base-info').hide();
	$('#base-warn').hide();
	$('#base-error').hide();
});
