$(function() {
	$('[href="/product"]').parent().addClass('active');
	
	var setting = {
		data: {
			simpleData: {
				enable: true
			}
		},
		callback: {
			onClick: onclick
		},
		async: {
			enable: true,
			url: "/product/ajax",
			autoParam: [ 'id' ],
			otherParam: { 'type': 'product' }
		}
	};
	
	function onclick(event, treeId, treeNode) {
		alert(treeNode.tId + " " + treeNode.id + " " + treeNode.name);
	};
	
	var products_tree;
	$.getJSON(
		"/product/ajax?type=product",
		function(jsondata) {
			if (jsondata.indexOf('error') != -1) {
				$('#base-error').text(jsondata).show();
				return;
			}
			products_tree = $.fn.zTree.init($('#products-tree'), setting, jsondata);
		}
	);
});