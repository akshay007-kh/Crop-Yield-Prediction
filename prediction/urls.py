from django.urls import path

from . import views


urlpatterns = [

    # Home page
    path(
        "",
        views.home,
        name="home"
    ),


    # Crop yield prediction page
    path(
        "predict/",
        views.prediction_form,
        name="prediction_form"
    ),

]