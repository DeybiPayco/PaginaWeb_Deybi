from flask import Flask,request,jsonify,render_template

#inicializacion de mi framework flask
app = Flask(__name__)

#rutas
@app.route('/')
def index():
    return render_template('index.html')

#ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)