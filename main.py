from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('lomake.html')

@app.route("/vastaus")
def vastaus():
    uusi_nimi = request.args['nimi']
    uusi_nimi= uusi_nimi*5
    
    #return render_template('vastaus.html', nimi=request.args['nimi'])
    return render_template('vastaus.html', nimi=uusi_nimi)
if __name__ == '__main__':
    app.run()
    
    #muutoskia. Tallenna versio.
    # jotta menee nettiin = git commit -a -m "viesti" sen jälkeen git push