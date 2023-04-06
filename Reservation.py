{% extends 'base.html' %} {% load static %} {% load humanize %} {% block pageContent %}
<style>
    .al-logo {
        height: 5em;
        width: 5em;
        object-fit: scale-down;
        object-position: center center;
    }
</style>
<section class="py-4">
    <div class="container">
        <h3 class="fw-bolder text-center">Reservation Form</h3>
        <center>
            <hr class="bg-primary opacity-100" style="height:3px" width="5%">
        </center>
        <div class="row justify-content-center">
            <div class="col-lg-8 col-md-10 col-sm-12 col-xs-12">
                <div class="list-group mb-3">
                    <div class="list-group-item">
                        <div class="d-flex w-100 align-items-center">
                            <div class="col-auto text-center px-3">
                                <img src="{% if flight.airline.image_path %}{{ flight.airline.image_path.url}}{% else %}{% static 'assets/default/img/no-image-available.png' %}{% endif %}" alt="{{ flight.airline.name}}" class="img-thumbnail rounded-circle al-logo">
                            </div>
                            <div class="col-auto flex-shrink-1 flex-grow-1">
                                <h4 class="m-0"><b>Flight - {{flight.code}}</b></h4>
                                <hr>
                                <div class="row">
                                    <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                                        <dl class="d-flex m-0">
                                            <dt class="m-0 fw-bold col-auto px-1">Plane:</dt>
                                            <dd class="m-0 col-auto flex-shrink-1 flex-grow-1">{{flight.air_craft_code}}</dd>
                                        </dl>
                                        <dl class="d-flex m-0">
                                            <dt class="m-0 fw-bold col-auto px-1">From:</dt>
                                            <dd class="m-0 col-auto flex-shrink-1 flex-grow-1">{{flight.from_airport.name}}</dd>
                                        </dl>
                                        <dl class="d-flex m-0">
                                            <dt class="m-0 fw-bold col-auto px-1">To:</dt>
                                            <dd class="m-0 col-auto flex-shrink-1 flex-grow-1">{{flight.to_airport.name}}</dd>
                                        </dl>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                                        <dl class="d-flex m-0">
                                            <dt class="m-0 fw-bold col-auto px-1">Airline:</dt>
                                            <dd class="m-0 col-auto flex-shrink-1 flex-grow-1">{{flight.airline.name}}</dd>
                                        </dl>
                                        <dl class="d-flex m-0">
                                            <dt class="m-0 fw-bold col-auto px-1">Departure:</dt>
                                            <dd class="m-0 col-auto flex-shrink-1 flex-grow-1">{{flight.departure|date:"F d, Y h:i A"}}</dd>
                                        </dl>
                                        <dl class="d-flex m-0">
                                            <dt class="m-0 fw-bold col-auto px-1">ETA:</dt>
                                            <dd class="m-0 col-auto flex-shrink-1 flex-grow-1">{{flight.estimated_arrival|date:"F d, Y h:i A"}}</dd>
                                        </dl>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                                        <dl class="d-flex m-0">
                                            <dt class="m-0 fw-bold col-auto px-1">Business Class Slot:</dt>
                                            <dd class="m-0 col-auto flex-shrink-1 flex-grow-1">{{flight.b_slot|intcomma}}</dd>
                                        </dl>
                                        <dl class="d-flex m-0">
                                            <dt class="m-0 fw-bold col-auto px-1">Business Class Price:</dt>
                                            <dd class="m-0 col-auto flex-shrink-1 flex-grow-1">{{flight.business_class_price|intcomma}}</dd>
                                        </dl>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                                        <dl class="d-flex m-0">
                                            <dt class="m-0 fw-bold col-auto px-1">Economy Slot:</dt>
                                            <dd class="m-0 col-auto flex-shrink-1 flex-grow-1">{{flight.e_slot|intcomma}}</dd>
                                        </dl>
                                        <dl class="d-flex m-0">
                                            <dt class="m-0 fw-bold col-auto px-1">Economy Price:</dt>
                                            <dd class="m-0 col-auto flex-shrink-1 flex-grow-1">{{flight.economy_price|intcomma}}</dd>
                                        </dl>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card rounded-0 shadow">
                    <div class="card-body">
                        <div class="container-fluid">
                            <form action="" id="reserve-form">
                                <input type="hidden" name="flight" value="{{flight.id}}">
                                <div class="row">
                                    <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                                        <div class="mb-3">
                                            <label for="first_name" class="control-label">First Name</label>
                                            <input type="text" id="first_name" name="first_name" class="form-control form-control-sm rounded-0" value="" required>
                                        </div>
                                    </div>
                                    <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                                        <div class="mb-3">
                                            <label for="middle_name" class="control-label">Middle Name</label>
                                            <input type="text" id="middle_name" name="middle_name" class="form-control form-control-sm rounded-0" value="">
                                        </div>
                                    </div>
                                    <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                                        <div class="mb-3">
                                            <label for="last_name" class="control-label">Last Name</label>
                                            <input type="text" id="last_name" name="last_name" class="form-control form-control-sm rounded-0" value="" required>
                                        </div>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                                        <div class="mb-3">
                                            <label for="gender" class="control-label">Gender</label>
                                            <select id="gender" name="gender" class="form-select form-select-sm rounded-0" required>
                                                <option>Male</option>
                                                <option>Female</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                                        <div class="mb-3">
                                            <label for="contact" class="control-label">Contact #</label>
                                            <input type="text" id="contact" name="contact" class="form-control form-control-sm rounded-0" value="">
                                        </div>
                                    </div>
                                    <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                                        <div class="mb-3">
                                            <label for="email" class="control-label">Email</label>
                                            <input type="email" id="email" name="email" class="form-control form-control-sm rounded-0" value="" required>
                                        </div>
                                    </div>
                                    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                                        <div class="mb-3">
                                            <label for="address" class="control-label">Address</label>
                                            <textarea type="address" id="address" name="address" class="form-control form-control-sm rounded-0" required></textarea>
                                        </div>
                                    </div>
                                    <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                                        <div class="mb-3">
                                            <label for="type" class="control-label">Seat Type</label>
                                        </div>
                                    </div>
                                    <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                                        <div class="mb-3">
                                            <select id="type" name="type" class="form-select form-select-sm rounded-0" required>
                                                <option value="1">Business Class</option>
                                                <option value="2">Economy</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                <div class="text-center mb-3">
                                    <button class="btn btn-primary bg-gradient-dark btn-lg rounded-pill w-100">Submit Reservation</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
{% endblock pageContent %} {% block ScriptBlock %}
<script>
    $(function() {
        $('.select2').select2({
            placeholder: "Please Select Here",
            width: "100%",
            containerCssClass: 'form-control form-control-sm rounded-0'
        })
        $('#reserve-form').submit(function(e) {
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
                url: "{% url 'save-reservation' %}",
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
{% endblock ScriptBlock %}
