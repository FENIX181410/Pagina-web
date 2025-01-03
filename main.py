from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('principal.html')

@app.route('/bioma/<var1>')
def bioma(var1):
    return render_template('bioma.html', var1=var1)
    
@app.route('/choice/<var1>/<var2>')
def choice(var1, var2):
    return render_template('choice.html', var1=var1, var2=var2)

@app.route('/misiones/<var1>/<var2>/<var3>')
def misiones(var1,var2,var3):
    return render_template('misiones.html',var1=var1,var2=var2,var3=var3)



if __name__ == '__main__':
    app.run(debug=True)