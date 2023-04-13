(function ($) {
    $(document).ready(function () {

        function toggleTicketInline(selected) {
            $.getJSON('/ajax/event-type/', {id: selected}, function (data, jqXHR) {
                if (data[0].fields.type == 'B')
                    $('#tickets-group').show();
                else
                    $('#tickets-group').hide();
            });
        }

        var $category = $('#id_event');
        toggleTicketInline($category.val());
        $category.change(function () {
            toggleTicketInline($(this).val());
        });
    });
})(django.jQuery);
