$(document).ready(function(){
    $(".multiselect").multiselect();
    $("#adv_search").click(function(){
	$("#adv").slideToggle();
    });
});
jQuery.fn.multiselect = function() {
    $(this).each(function() {
	var checkboxes = $(this).find("input:checkbox");
	checkboxes.each(function() {
	    var checkbox = $(this);
	    // Highlight pre-selected checkboxes
	    if (checkbox.attr("checked"))
		checkbox.parent().addClass("multiselect-on");

	    // Highlight checkboxes that the user selects
	    checkbox.click(function() {
		if (checkbox.attr("checked"))
		    checkbox.parent().addClass("multiselect-on");
		else
		    checkbox.parent().removeClass("multiselect-on");
	    });
	});
    });
};
jQuery.fn.multiselect2 = function() {
    $(this).each(function() {
	var checkboxes = $(this).find("input:checkbox");
	checkboxes.each(function() {
	    var checkbox = $(this);
	    // Highlight pre-selected checkboxes
	    if (checkbox.attr("checked"))
		checkbox.parent().addClass("multiselect-on");

	    // Highlight checkboxes that the user selects
	    checkbox.click(function() {
		if (checkbox.attr("checked"))
		    checkbox.parent().addClass("multiselect-on");
		else
		    checkbox.parent().removeClass("multiselect-on");
	    });
	});
    });
};