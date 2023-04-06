{% endblock pageContent %} {% block ScriptBlock %}
<script>
    $(function() {
        $('#create_new').click(function() {
            uni_modal("<i class='fa fa-plus'></i> Add New Airport", "{% url 'manage-airport' %}")
        })
        $('.edit-data').click(function() {
            uni_modal("<i class='fa fa-edit'></i> Edit Airport Details", $(this).attr('data-url'))
        })
        $('.view_image').click(function() {
            var img = $(this).attr('data-img-url')
            $('#viewer_modal #img-viewer-field').attr('src', img)
            $('#viewer_modal').modal('show')
        })
        $('.delete-data').click(function() {
            _conf("Are you sure to delete this airport?", 'delete_airport', ["'" + $(this).attr('data-url') + "'"])
        })
        $('#airport-tbl').find('td, th').addClass('px-2 py-1 align-middle')
        $('#airport-tbl').DataTable({
            columnDefs: [{
                orderable: false,
                targets: [4]
            }],
            lengthMenu: [
                [25, 50, 100, -1],
                [25, 50, 100, "All"]
            ]
        })
    })

    function delete_airport(url) {

        var _this = $('#confirm_modal .modal-body')
        $('.err-msg').remove();
        var el = $('<div>')
        el.addClass("alert alert-danger err-msg")
        el.hide()
        start_loader()
        $.ajax({
            headers: {
                "X-CSRFToken": "{{csrf_token}}"
            },
            url: url,
            dataType: 'JSON',
            error: err => {
                console.log(err)
                alert("an error occurred.")
                end_loader()
            },
            success: function(resp) {
                if (resp.status == 'success') {
                    location.reload()
                } else if (!!resp.msg) {
                    el.html(resp.msg)
                    _this.prepend(el)
                    el.show()
                } else {
                    el.html("An error occurred")
                    _this.prepend(el)
                    el.show()
                }
                end_loader()
            }

        })
    }
</script>

