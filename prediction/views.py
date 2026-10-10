import pandas as pd
import joblib

from django.shortcuts import render


# =========================
# LOAD TRAINED MODEL
# =========================

model = joblib.load("prediction/model.pkl")


# Load encoders
crop_encoder = joblib.load("prediction/crop_encoder.pkl")
season_encoder = joblib.load("prediction/season_encoder.pkl")
state_encoder = joblib.load("prediction/state_encoder.pkl")


# =========================
# HOME PAGE
# =========================

def home(request):

    return render(
        request,
        "prediction/home.html"
    )


# =========================
# PREDICTION PAGE
# =========================

def prediction_form(request):

    prediction = None


    # =========================
    # DROPDOWN VALUES
    # =========================

    crops = list(crop_encoder.classes_)

    seasons = list(season_encoder.classes_)

    states = list(state_encoder.classes_)


    # =========================
    # SELECTED VALUES
    # =========================

    selected_crop = ""

    selected_year = ""

    selected_season = ""

    selected_state = ""

    selected_area = ""

    selected_rainfall = ""

    selected_fertilizer = ""

    selected_pesticide = ""


    # =========================
    # FORM SUBMISSION
    # =========================

    if request.method == "POST":


        # Get values from form

        selected_crop = request.POST.get("crop")

        selected_year = request.POST.get("crop_year")

        selected_season = request.POST.get("season")

        selected_state = request.POST.get("state")


        selected_area = request.POST.get("area")

        selected_rainfall = request.POST.get(
            "annual_rainfall"
        )

        selected_fertilizer = request.POST.get(
            "fertilizer"
        )

        selected_pesticide = request.POST.get(
            "pesticide"
        )


        # =========================
        # CONVERT NUMERIC VALUES
        # =========================

        crop_year = int(selected_year)

        area = float(selected_area)

        annual_rainfall = float(
            selected_rainfall
        )

        fertilizer = float(
            selected_fertilizer
        )

        pesticide = float(
            selected_pesticide
        )


        # =========================
        # ENCODE CATEGORICAL VALUES
        # =========================

        crop_encoded = crop_encoder.transform(
            [selected_crop]
        )[0]


        season_encoded = season_encoder.transform(
            [selected_season]
        )[0]


        state_encoded = state_encoder.transform(
            [selected_state]
        )[0]


        # =========================
        # CREATE INPUT DATA
        # =========================

        input_data = pd.DataFrame([

            {

                "Crop": crop_encoded,

                "Crop_Year": crop_year,

                "Season": season_encoded,

                "State": state_encoded,

                "Area": area,

                "Annual_Rainfall": annual_rainfall,

                "Fertilizer": fertilizer,

                "Pesticide": pesticide

            }

        ])


        # =========================
        # PREDICT YIELD
        # =========================

        prediction = model.predict(
            input_data
        )[0]


    # =========================
    # TEMPLATE CONTEXT
    # =========================

    context = {

        "prediction": prediction,


        # Dropdown values

        "crops": crops,

        "seasons": seasons,

        "states": states,


        # Selected values

        "selected_crop": selected_crop,

        "selected_year": selected_year,

        "selected_season": selected_season,

        "selected_state": selected_state,

        "selected_area": selected_area,

        "selected_rainfall": selected_rainfall,

        "selected_fertilizer": selected_fertilizer,

        "selected_pesticide": selected_pesticide,

    }


    # =========================
    # RENDER PREDICTION PAGE
    # =========================

    return render(

        request,

        "prediction/prediction_form.html",

        context

    )