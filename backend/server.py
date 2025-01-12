from flask import Flask, render_template, request # type: ignore
import requests # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = 'votre_clé_api'  # Remplacez par votre clé API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()

    if response['cod'] == 200:
        data = {
            'city': city,
            'temperature': response['main']['temp'],
            'weather': response['weather'][0]['description'],
        }
        return render_template('result.html', data=data)
    else:
        return f"Erreur: {response['message']}"

if __name__ == "__main__":
    app.run(debug=True)
