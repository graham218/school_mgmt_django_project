$(document).ready(function () {
    $('#id_stage').select2({
        ajax: {
            url: "{% url 'school:add-students' %}",
            dataType: 'json',
            processResults: function (data) {
                return {
                    results: $.map(data, function (item) {
                        return {id: item.id, text: item.year};
                    })
                };
            }
        },
        minimumInputLength: 1
    });
});
