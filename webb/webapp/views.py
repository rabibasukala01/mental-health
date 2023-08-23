from django.shortcuts import render
import pandas as pd
import pickle
import logging
import os


# Create your views here.


def home(request):
    if request.method == "POST":
        data = {
            "Age": [float(request.POST["age"])],
            "Primary streaming service": [request.POST["streamingservice"]],
            "Hours per day": [request.POST["hours"]],
            "While working": [request.POST["working"]],
            "Instrumentalist": [request.POST["Instrumentalist"]],
            "Composer": [request.POST["Composer"]],
            "Fav genre": [request.POST["Favgenre"]],
            "Exploratory": [request.POST["Exploratory"]],
            "Foreign languages": [request.POST["Foreignlanguages"]],
            "BPM": [request.POST["bpm"]],
            "Frequency [Classical]": [request.POST["Frequency[Classical]"]],
            "Frequency [Country]": [request.POST["Frequency[Country]"]],
            "Frequency [EDM]": [request.POST["Frequency[EDM]"]],
            "Frequency [Folk]": [request.POST["Frequency[Folk]"]],
            "Frequency [Gospel]": [request.POST["Frequency[Gospel]"]],
            "Frequency [Hip hop]": [request.POST["Frequency[Hip hop]"]],
            "Frequency [Jazz]": [request.POST["Frequency[Jazz]"]],
            "Frequency [K pop]": [request.POST["Frequency[K pop]"]],
            "Frequency [Latin]": [request.POST["Frequency[Latin]"]],
            "Frequency [Lofi]": [request.POST["Frequency[Lofi]"]],
            "Frequency [Metal]": [request.POST["Frequency[Metal]"]],
            "Frequency [Pop]": [request.POST["Frequency[Pop]"]],
            "Frequency [R&B]": [request.POST["Frequency[R&B]"]],
            "Frequency [Rap]": [request.POST["Frequency[Rap]"]],
            "Frequency [Rock]": [request.POST["Frequency[Rock]"]],
            "Frequency [Video game music]": [
                request.POST["Frequency[Video game music]"]
            ],
            "Music effects": [request.POST["Musiceffects"]],
        }
        logging.info("home page served")
        # print((request.POST["Musiceffects"]))

        current_file_path = os.path.abspath(__file__)
        model_path = os.path.join(
            os.path.dirname(current_file_path), "..", "..", "notebook", "model.pkl"
        )
        transformer_path = os.path.join(
            os.path.dirname(current_file_path),
            "..",
            "..",
            "notebook",
            "transformer.pkl",
        )
        try:
            model = pickle.load(open(model_path, "rb"))
            transformer = pickle.load(open(transformer_path, "rb"))

            tempdf = pd.DataFrame(data)
            df = transformer.transform(tempdf)

            prediction = model.predict(df)

        except Exception as e:
            logging.info("cannot load model or transformer")
            print(e)
            prediction = "error"

        # print(prediction)
        return render(request, "result.html", {"prediction": prediction})
    return render(request, "home.html", {})
