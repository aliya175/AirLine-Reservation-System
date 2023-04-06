{% load qr_code %} {% load static %} {% load humanize %}
<style>
    #uni_modal .modal-footer {
        display: none
    }
    
    #airline-logo {
        max-width: 3em;
        max-height: 3em;
        object-fit: scale-down;
        object-position: center center;
    }
</style>
<div class="container-fluid" id="e-details">
    <div class="lh-1">
        <fieldset>
            <legend>Flight Information</legend>
            <hr>
            <div class="row">
                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <dl>
                        <dt>Flight Code</dt>
                        <dd class="ps-4">{{reservation.flight.code}}</dd>
                        <dt>Air Craft/Plane Code</dt>
                        <dd class="ps-4">{{reservation.flight.air_craft_code}}</dd>
                        <dt>From</dt>
                        <dd class="ps-4">{{reservation.flight.from_airport.name}}</dd>
                        <dt>To</dt>
                        <dd class="ps-4">{{reservation.flight.to_airport.name}}</dd>
                    </dl>
                </div>
                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <dl>
                        <dt>Airline</dt>
                        <dd class="ps-4"><img src="{% if reservation.flight.airline.image_path %}{{ reservation.flight.airline.image_path.url}}{% else %}{% static 'assets/default/img/no-image-available.png' %}{% endif %}" alt="" class="img-thumbnail rounded-circle" id="airline-logo">                            {{reservation.flight.airline.name}}</dd>
                        <dt>Departure Date and Time</dt>
                        <dd class="ps-4">{{reservation.flight.departure|date:"F d, Y h:i A"}}</dd>
                        <dt>Estimated Time of Arrival</dt>
                        <dd class="ps-4">{{reservation.flight.estimated_arrival|date:"F d, Y h:i A"}}</dd>
                    </dl>
                </div>
            </div>
        </fieldset>
        <fieldset>
            <legend>Pasenger Information</legend>
            <hr>
            <div class="row">
                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <dl>
                        <dt>Fullname</dt>
                        <dd class="ps-4">{{reservation.name}}</dd>
                        <dt>Gender</dt>
                        <dd class="ps-4">{{reservation.gender}}</dd>
                        <dt>Contact #</dt>
                        <dd class="ps-4">{{reservation.contact}}</dd>
                    </dl>
                </div>
                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <dl>
                        <dt>Email</dt>
                        <dd class="ps-4">{{reservation.email}}</dd>
                        <dt>Address</dt>
                        <dd class="ps-4">{{reservation.address}}</dd>
                    </dl>
                </div>
            </div>
        </fieldset>
        <hr>
        <div class="row">
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <dl>
                    <dt>Select Seat Type</dt>
                    <dd class="ps-4">
                        {% if reservation.type == '1' %} Business Class {% else %} Economy {% endif %}
                    </dd>
                </dl>
            </div>
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <dl>
                    <dt>Status</dt>
                    <dd class="ps-4">
                        {% if reservation.status == '0' %}
                        <span class="badge badge-secondary bg-gradient bg-secondary text-sm px-3 rounded-pill">Pending</span> {% elif reservation.status == '1' %}
                        <span class="badge badge-primary bg-gradient bg-primary text-sm px-3 rounded-pill">Confirmed</span> {% else %}
                        <span class="badge badge-danger bg-gradient bg-danger text-sm px-3 rounded-pill">Cancelled</span> {% endif %}
                    </dd>
                </dl>
            </div>
        </div>
    </div>
</div>
<hr>
<div class="text-end">
    {% if reservation.status == '0' %}
    <button class="btn btn-primary border bg-gradient bg-primary rounded-0 update_reservation" data-status="1" type="button">Mark as Confirmed</button> {% endif %}
    <button class="btn btn-danger border bg-gradient bg-danger rounded-0 update_reservation" data-status="2" type="button">Cancel</button>
    <button class="btn btn-light border bg-gradient bg-light rounded-0" data-bs-dismiss="modal" type="button">Close</button>
</div>
<script>
    $(function() {
        $('.update_reservation').click(function() {
            var status = $(this).attr('data-status')
            var message;
            if (status == 1)
                message = "Are you sure to mark this reservation as confirmed?";
            else
                message = "Are you sure to cancel this reservation?";

            _conf(message, "update_reservation", [status])
        })
    })

    function update_reservation($status) {
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
            url: "{% url 'update-reservation' %}",
            method: "POST",
            data: {
                id: '{{reservation.id}}',
                status: $status
            },
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
