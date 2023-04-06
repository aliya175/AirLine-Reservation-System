{% extends 'base.html' %} {% load static %} {% block pageContent %}
<section class="py-4">
    <div class="container">
        <h3 class="fw-bolder text-center">List of Flights</h3>
        <center>
            <hr class="bg-primary opacity-100" style="height:3px" width="5%">
        </center>
        <div class="card rounded-0 shadow">
            <div class="card-body">
                <div class="container-fluid">
                    <div class="text-end mb-3">
                        <button class="btn btn-sm btn-primary rounded-0 bg-gradient-primary" type="button" id="create_new"><i class="fa fa-plus"></i> Add New</button>
                    </div>
                    <table class="table table-bordered table-striped" id="flight-tbl">
                        <colgroup>
                            <col width="5%">
                            <col width="20%">
                            <col width="20%">
                            <col width="40%">
                            <col width="15%">
                        </colgroup>
                        <thead>
                            <tr>
                                <th class="text-center">#</th>
                                <th class="text-center">Flight</th>
                                <th class="text-center">Airline</th>
                                <th class="text-center">Details</th>
                                <th class="text-center">Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for flight in flights %}
                            <tr>
                                <td class="text-center">{{ forloop.counter }}</td>
                                <td>{{ flight.code }}</td>
                                <td>{{ flight.airline.name}}</td>
                                <td>
                                    <div class="lh-1">
                                        <small><b>Departure:</b> {{ flight.departure|date:"Y-m-d h:i A" }}, {{ flight.from_airport.name }}</small><br>
                                        <small><b>Arrival:</b> {{ flight.estimated_arrival|date:"Y-m-d h:i A" }}, {{ flight.to_airport.name }}</small>
                                    </div>
                                </td>
                                <td class="text-center">
                                    <div class="dropdown">
                                        <button class="btn btn-light btn-sm rounded-0 border dropdown-toggle" type="button" id="abtn{{flight.pk}}" data-bs-toggle="dropdown" aria-expanded="false">
                                          Action
                                        </button>
                                        <ul class="dropdown-menu" aria-labelledby="abtn{{flight.pk}}">
                                            <li><a class="dropdown-item view-data" href="javascript:void(0)" data-url="{% url 'view-flight-pk' flight.pk %}"><i class="fa fa-eye text-dark"></i> View</a></li>
                                            <li><a class="dropdown-item edit-data" href="javascript:void(0)" data-url="{% url 'manage-flight-pk' flight.pk %}"><i class="fa fa-edit text-primary"></i> Edit</a></li>
                                            <li><a class="dropdown-item delete-data" href="javascript:void(0)" data-url="{% url 'delete-flight-pk' flight.pk %}"><i class="fa fa-trash text-danger"></i> Delete</a></li>
                                        </ul>
                                    </div>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</section>
{% endblock pageContent %} {% block ScriptBlock %}
<script>
    $(function() {
        $('#create_new').click(function() {
            uni_modal("<i class='fa fa-plus'></i> Add New Flight", "{% url 'manage-flight' %}", 'modal-lg')
        })
        $('.edit-data').click(function() {
            uni_modal("<i class='fa fa-edit'></i> Edit Flight Details", $(this).attr('data-url'), 'modal-lg')
        })
        $('.view-data').click(function() {
            uni_modal("<i class='fa fa-th-list'></i> Flight Details", $(this).attr('data-url'), 'modal-lg')
        })
        $('.view_image').click(function() {
            var img = $(this).attr('data-img-url')
            $('#viewer_modal #img-viewer-field').attr('src', img)
            $('#viewer_modal').modal('show')
        })
        $('.delete-data').click(function() {
            _conf("Are you sure to delete this flight?", 'delete_flight', ["'" + $(this).attr('data-url') + "'"])
        })
        $('#flight-tbl').find('td, th').addClass('px-2 py-1 align-middle')
        $('#flight-tbl').DataTable({
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

    function delete_flight(url) {

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

