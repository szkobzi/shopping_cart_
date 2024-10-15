from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

def betolt_kosar():
    if os.path.exists('kosar.json'):
        with open('kosar.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def mentes_kosar(kosar):
    with open('kosar.json', 'w', encoding="utf-8") as file:
        json.dump(kosar, file, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    kosar = betolt_kosar()
    return render_template('index.html', kosar=kosar)

@app.route('/hozzaad', methods=['POST'])
def hozzaad_termek():
    termek_nev = request.form.get('termek')
    termek_ar = request.form.get('ar')
    
    if termek_nev and termek_ar:
        kosar = betolt_kosar()
        kosar.append({"termek": termek_nev, "ar": int(termek_ar)})
        mentes_kosar(kosar)
    return redirect(url_for('index'))

@app.route('/torol/<int:index>')
def torol_termek(index):
    kosar = betolt_kosar()
    if 0 <= index < len(kosar):
        del kosar[index]
        mentes_kosar(kosar)
    return redirect(url_for('index'))

@app.route('/modosit/<int:index>', methods=['POST'])
def modosit_termek(index):
    kosar = betolt_kosar()
    if 0 <= index < len(kosar):
        uj_termek_nev = request.form.get('uj_termek_nev')
        uj_termek_ar = request.form.get('uj_termek_ar')

        if uj_termek_nev.strip():
            kosar[index]['termek'] = uj_termek_nev

        if uj_termek_ar.strip():
            try:
                kosar[index]['ar'] = int(uj_termek_ar)
            except ValueError:
                pass 

        mentes_kosar(kosar)
    return redirect(url_for('index'))

@app.route('/torol_kosar', methods=['POST'])
def torol_kosar():
    mentes_kosar([])  
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
