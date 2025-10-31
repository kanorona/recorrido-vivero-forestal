from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Cargar etiquetas desde CSV
    df = pd.read_csv('data/etiquetas.csv')
    etiquetas = df.to_dict(orient='records')
    return render_template('index.html', etiquetas=etiquetas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
