from flask import Flask, render_template, request,url_for,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/login.html')

@app.route('/check', methods=['POST'])
def check():
    nombre_usuario = request.form['nombre_usuario']
    contra = request.form['pass']
    if nombre_usuario[0].isupper() and any(char.isalpha() for char in contra) and any(char.isdigit() for char in contra):
        print(nombre_usuario + contra)
        return redirect(url_for('success'))
    else:
        return redirect(url_for("index"))

@app.route('/success')
def success():
    nombre_usuario = request.args.get('nombre_usuario')
    return render_template('success.html', nombre_usuario=nombre_usuario)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=5000)