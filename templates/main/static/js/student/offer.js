$(document).ready(function() {
    $('.input-reset').on('input', function() {
        var searchText = $(this).val().toLowerCase();
        $('.info-user__block').each(function() {
            var title = $(this).find('.info_name').text().toLowerCase();
            var tags = $(this).find('.info__skills p').map(function() {
                return $(this).text().toLowerCase();
            }).get();
            var found = title.includes(searchText);
            tags.forEach(function(tag) {
                if (tag.includes(searchText)) {
                    found = true;
                }
            });
            if (found) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
});