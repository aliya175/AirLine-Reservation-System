{% load qr_code %} {% load static %} {% load humanize %}
<style>
    #uni_modal .modal-footer {
        display: none
    }
    
    #uni_modal .modal-sub-footer {
        display: flex
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
        <div class="row">
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <dl>
                    <dt>Flight Code</dt>
                    <dd class="ps-4">{{flight.code}}</dd>
                    <dt>Airline</dt>
                    <dd class="ps-4"><img src="{% if flight.airline.image_path %}{{ flight.airline.image_path.url}}{% else %}{% static 'assets/default/img/no-image-available.png' %}{% endif %}" alt="" class="img-thumbnail rounded-circle" id="airline-logo"> {{flight.airline.name}}</dd>
                    <dt>Air Craft/Plane Code</dt>
                    <dd class="ps-4">{{flight.air_craft_code}}</dd>
                    <dt>From</dt>
                    <dd class="ps-4">{{flight.from_airport.name}}</dd>
                    <dt>To</dt>
                    <dd class="ps-4">{{flight.to_airport.name}}</dd>
                </dl>
            </div>
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <dl>
                    <dt>Departure Date and Time</dt>
                    <dd class="ps-4">{{flight.departure|date:"F d, Y h:i A"}}</dd>
                    <dt>Estimated Time of Arrival</dt>
                    <dd class="ps-4">{{flight.estimated_arrival|date:"F d, Y h:i A"}}</dd>
                    <dt>Business Class Available Slots</dt>
                    <dd class="ps-4">{{flight.business_class_slots|intcomma}}</dd>
                    <dt>Economy Available Slots</dt>
                    <dd class="ps-4">{{flight.economy_slots|intcomma}}</dd>
                    <dt>Business Class Available Price</dt>
                    <dd class="ps-4">{{flight.business_class_price|intcomma}}</dd>
                    <dt>Economy Available Price</dt>
                    <dd class="ps-4">{{flight.economy_price|intcomma}}</dd>
                </dl>
            </div>
        </div>
    </div>
</div>
