$(document).ready(function() {
    $('.dashboard__list-block').click(function(e) {
        e.preventDefault();
        var target = $(this).attr('href');
        $('.section-right-container').hide();
        $(target).show();
    });
});