
{% extends 'base.html' %}{% load static %}{% block pageContent %}
<div class="container-fluid">
    <div class="row justify-content-center">
        <div class="col-lg-6 col-md-8 col-sm-12 col-xs-12">
            <div class="card card-default rounded-0 shadow">
                <div class="card-header">
                    <h4 class="card-title"><b>Update Account Details</b></h4>
                </div>
                <div class="card-body">
                    <div class="container-fluid">
                        <form id="update-user" method="POST" action="{% url 'update-profile' %}" enctype="multipart/form-data">
                            {% csrf_token %}
                            <div class="mdc-layout-grid">
                                <div class="mdc-layout-grid__inner">
                                    <div class="form-group mb-3">
                                        <label for="first_name" class="control-label">First Name</label>
                                        <input type="text" class="form-control rounded-0" name="first_name" id="first_name" value="{% if form.data.first_name %}{{ form.data.first_name }}{% else %}{{ user.first_name }}{% endif %}" required="required">
                                    </div>
                                    <div class="form-group mb-3">
                                        <label for="last_name" class="control-label">Last Name</label>
                                        <input type="text" class="form-control rounded-0" name="last_name" id="last_name" value="{% if form.data.last_name %}{{ form.data.last_name }}{% else %}{{ user.last_name }}{% endif %}" required="required">
                                    </div>
                                    <div class="form-group mb-3">
                                        <label for="username" class="control-label">Username</label>
                                        <input type="text" class="form-control rounded-0" name="username" id="username" value="{% if form.data.username %}{{ form.data.username }}{% else %}{{ user.username }}{% endif %}" required="required">
                                    </div>
                                    <div class="form-group mb-3">
                                        <label for="email" class="control-label">Email</label>
                                        <input type="email" class="form-control rounded-0" name="email" id="email" value="{% if form.data.email %}{{ form.data.email }}{% else %}{{ user.email }}{% endif %}" required="required">
                                    </div>
                                    <div class="form-group mb-3">
                                        <label for="current_password" class="control-label">Enter Password</label>
                                        <input type="password" class="form-control rounded-0" name="current_password" id="current_password" required="required">
                                    </div>
                                    {% for field in form %} {% for error in field.errors %}
                                    <div class="alert alert-danger my-2">
                                        <p>{{ error }}</p>
                                    </div>
                                    {% endfor %} {% endfor %}
                                    <div class="form-group mb-3">
                                        <div class="d-flex w-100 justify-content-end">
                                            <button class="btn btn-sm rounded-0 btn-primary col-4">
                                                    Login
                                                </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock pageContent %}

