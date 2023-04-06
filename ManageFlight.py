{% load qr_code %}{% load static %}
<div class="container-fluid">
    <form action="" id="flight-form">
        <input type="hidden" name="id" value="{{flight.id}}">
        <div class="row">
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div class="mb-3">
                    <label for="code" class="control-label">Flight Code</label>
                    <input type="text" id="code" name="code" class="form-control form-control-sm rounded-0" value="{{flight.code}}" required>
                </div>
                <div class="mb-3">
                    <label for="airline" class="control-label">Airline</label>
                    <select type="text" id="airline" name="airline" class="form-select form-select-sm rounded-0 select2" required>
                        {% if not flight.airline %}
                        <option value=""  disabled selected></option>
                        {% else %}
                        <option value="" disabled ></option>
                        {% endif %}
                        {% for airline in airlines %}
                            {% if airline.id == flight.airline.id %}
                            <option value="{{airline.id}}" selected>{{airline.name}}</option>
                            {% else %}
                            <option value="{{airline.id}}">{{airline.name}}</option>
                            {% endif %}
                        {% endfor %}
                    </select>
                </div>
                <div class="mb-3">
                    <label for="air_craft_code" class="control-label">Plane/Air Craft Code</label>
                    <input type="text" id="air_craft_code" name="air_craft_code" class="form-control form-control-sm rounded-0" value="{{flight.air_craft_code}}" required>
                </div>
                <div class="mb-3">
                    <label for="from_airport" class="control-label">From</label>
                    <select type="text" id="from_airport" name="from_airport" class="form-select form-select-sm rounded-0 select2" required>
                        {% if not flight.from_airport %}
                        <option value=""  disabled selected></option>
                        {% else %}
                        <option value="" disabled ></option>
                        {% endif %}
                        {% for airport in airports %}
                            {% if airport.id == flight.from_airport.id %}
                            <option value="{{airport.id}}" selected>{{airport.name}}</option>
                            {% else %}
                            <option value="{{airport.id}}">{{airport.name}}</option>
                            {% endif %}
                        {% endfor %}
                    </select>
                </div>
                <div class="mb-3">
                    <label for="to_airport" class="control-label">To</label>
                    <select type="text" id="to_airport" name="to_airport" class="form-select form-select-sm rounded-0 select2" required>
                        {% if not flight.to_airport %}
                        <option value=""  disabled selected></option>
                        {% else %}
                        <option value="" disabled ></option>
                        {% endif %}
                        {% for airport in airports %}
                            {% if airport.id == flight.to_airport.id %}
                            <option value="{{airport.id}}" selected>{{airport.name}}</option>
                            {% else %}
                            <option value="{{airport.id}}">{{airport.name}}</option>
                            {% endif %}
                        {% endfor %}
                    </select>
                </div>
            </div>
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div class="mb-3">
                    <label for="departure" class="control-label">Departure Date and Time</label>
                    <input type="datetime-local" id="departure" name="departure" class="form-control form-control-sm rounded-0" value="{{flight.departure|date:'Y-m-d\TH:i'}}" required>
                </div>
                <div class="mb-3">
                    <label for="estimated_arrival" class="control-label">Estimated Time of Arrival</label>
                    <input type="datetime-local" id="estimated_arrival" name="estimated_arrival" class="form-control form-control-sm rounded-0" value="{{flight.estimated_arrival|date:'Y-m-d\TH:i'}}" required>
                </div>
                <div class="mb-3">
                    <label for="business_class_slots" class="control-label">No. of Business Class Available Seats</label>
                    <input type="number" id="business_class_slots" name="business_class_slots" class="form-control form-control-sm rounded-0 text-end" value="{{flight.business_class_slots}}" required>
                </div>
                <div class="mb-3">
                    <label for="economy_slots" class="control-label">No. of Economy Available Seats</label>
                    <input type="number" id="economy_slots" name="economy_slots" class="form-control form-control-sm rounded-0 text-end" value="{{flight.economy_slots}}" required>
                </div>
                <div class="mb-3">
                    <label for="business_class_price" class="control-label">No. of Business Class Available Seats</label>
                    <input type="text" pattern="^[0-9/.]$+" id="business_class_price" name="business_class_price" class="form-control form-control-sm rounded-0 text-end" value="{{flight.business_class_price}}" required>
                </div>
                <div class="mb-3">
                    <label for="economy_price" class="control-label">No. of Economy Available Seats</label>
                    <input type="text" pattern="^[0-9/.]$+" id="economy_price" name="economy_price" class="form-control form-control-sm rounded-0 text-end" value="{{flight.economy_price}}" required>
                </div>
            </div>
        </div>
    </form>
</div>
<script>
    $(function() {
        $('#uni_modal').on('shown.bs.modal', function() {
            $('.select2').select2({
                placeholder: "Please Select Here",
                width: "100%",
                dropdownParent: $('#uni_modal'),
                containerCssClass: 'form-control form-control-sm rounded-0'
            })
        })
        $('#flight-form').submit(function(e) {
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
            if ($('#from_airport').val() == $('#to_airport').val()) {
                el.text("Invalide From and To Airports.")
                _this.append(el)
                el.show('slow')
                $('html, body, .modal').scrollTop(0)
                return false
            }
            start_loader();
            $.ajax({
                headers: {
                    "X-CSRFToken": '{{csrf_token}}'
                },
                url: "{% url 'save-flight' %}",
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
                        el.html(resp.msg)
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
