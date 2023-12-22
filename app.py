from flask import Flask,request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline



application = Flask(__name__)
app = application

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/predict", methods = ['GET','POST'])
def predict_datapoint():

    if request.method == "GET":
        return render_template('form.html')
    else:
        data = CustomData(
            Median_Sale_Price_House = float(request.form.get('Median_Sale_Price_House')),
            Personal_Income_Per_Capita = float(request.form.get('Personal_Income_Per_Capita')),
            Property_Tax = float(request.form.get('Property_Tax')),
            Nasdaqcom = float(request.form.get('Nasdaqcom')),
            Construction_Employment_Cost = float(request.form.get('Construction_Employment_Cost')),
            Population = float(request.form.get('Population')),
            New_House_Units_Construction = float(request.form.get('New_House_Units_Construction')),
            CPI = float(request.form.get('CPI')),
            Mortage_Rate = float(request.form.get('Mortage_Rate')),
            Unemployment_Rate = float(request.form.get('Unemployment_Rate')),
            Household_Debt_Payment = float(request.form.get('Household_Debt_Payment')),
            Recession_Rate = float(request.form.get('Recession_Rate')),
            Date_Quarter = request.form.get('Date_Quarter'),
            Date_Year = request.form.get('Date_Year'),


        )
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)

        results = round(pred[0],2)

        return render_template('result.html',final_result = results)
         






if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)