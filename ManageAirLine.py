       {% load qr_code %}{% load static %}
<style>
    img.img-thumbnail.avatar {
        max-width: 7em;
        max-height: 7em;
        object-fit: scale-down;
        object-position: center center;
    }
</style>
<div class="container-fluid">
    <form action="" id="airline-form">
        <input type="hidden" name="id" value="{{airline.id}}">
        <div class="mb-3">
            <label for="name" class="control-label">Name</label>
            <input type="text" id="name" name="name" class="form-control form-control-sm rounded-0" value="{{airline.name}}" required>
        </div>
        <div class="mb-3">
            <label for="status" class="control-label">Status</label>
            <select type="text" id="status" name="status" class="form-select form-select-sm rounded-0" required>
                {% if airline.status == '1' %}
                <option value="1" selected>Active</option>
                {% else %}
                <option value="1">Active</option>
                {% endif %}
                {% if airline.status == '2' %}
                <option value="2" selected>Inactive</option>
                {% else %}
                <option value="2">Inactive</option>
                {% endif %}
            </select>
        </div>
        <div class="mb-3">
            <label for="image" class="form-label">Logo File</label>
            <input class="form-control" type="file" name="image_path" accept="images/*" id="image" onchange="display_image(this)">
        </div>
        <div class="mb-3">
            <img src="{% if airline.image_path %}{{ airline.image_path.url}}{% else %}{% static 'assets/default/img/no-image-available.png' %}{% endif %}" alt="{{ airline.name}}" alt="" class="img-thumbnail rounded-circle avatar" id="cimg">
        </div>
    </form>
</div>
<script>
    function display_image(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                $('#cimg').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        } else {
            $('#cimg').attr('src', "{% static 'assets/default/img/no-image-available.png' %}");
        }
    }
    $(function() {
        $('#airline-form').submit(function(e) {
            e.preventDefault();
            var _this = $(this)
            $('.err-msg').remove();
            var el = $('<div>')
            el.addClass("alert alert-danger err-msg")
            el.hide()
            if (_this[0].checkValidity() == false) {
                _this[0].reportValidity();
                return false;
            }
            start_loader();
            $.ajax({
                headers: {
                    "X-CSRFToken": '{{csrf_token}}'
                },
                url: "{% url 'save-airline' %}",
                data: new FormData($(this)[0]),
                cache: false,
                contentType: false,
                processData: false,
                method: 'POST',
                type: 'POST',
                dataType: 'json',
                error: err => {
                    console.log(err)
                    alert("An error occured", 'error');
                    end_loader();
                },
                success: function(resp) {
                    if (typeof resp == 'object' && resp.status == 'success') {
                        location.reload()
                    } else if (resp.status == 'failed' && !!resp.msg) {
                        el.text(resp.msg)
                    } else {
                        el.text("An error occured", 'error');
                        end_loader();
                        console.err(resp)
                    }
                    _this.prepend(el)
                    el.show('slow')
                    $("html, body, .modal").scrollTop(0);
                    end_loader()
                }
            })
        })
    })
</script>
