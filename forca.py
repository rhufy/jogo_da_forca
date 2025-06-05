from flask import Flask, request, render_template, redirect, flash, session
import json
import random

forca = Flask(__name__)
PALAVRAS = 'palavras.json'
forca.secret_key = 'none'


def palavras():
    with open(PALAVRAS, 'r') as f:
        return json.load(f)


def sorteio():
    dados = palavras()
    sorte = random.choice(dados['palavras'])
    return sorte


def palavra_oculta(palavra, letras_tentadas):
    return ' '.join([letra if letra in letras_tentadas else '_' for letra in palavra])


@forca.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        session['name'] = name
        session['tentativas'] = 5
        session.pop('sorte', None)
        session.pop('letras_tentadas', None)
        return redirect('/jogo')
    return render_template('index.html')


@forca.route('/jogo', methods=['GET', 'POST'])
def jogo():
    if 'sorte' not in session:
        session['letras_tentadas'] = []
        session['sorte'] = sorteio()
        session['tentativas'] = 5
        session['vitoria'] = False
    if request.method == 'POST':
        letra = request.form['letra'].lower()

        # Já tentou essa letra
        if letra in session['letras_tentadas']:
            flash('Letra repetida', 'info')
            return redirect('/jogo')

        session['letras_tentadas'].append(letra)

        if letra in session['sorte']:
            flash('Parabéns, acertou a letra!', 'success')

            # Verifica se todas as letras da palavra foram acertadas
            palavra = session['sorte']
            acertou_todas = all(l in session['letras_tentadas'] for l in palavra)

            if acertou_todas:
                flash('Parabéns! Você completou a palavra!', 'success')
                session['vitoria'] = True
                return redirect('/jogo')

            return redirect('/jogo')

        else:
            session['tentativas'] -= 1
            if session['tentativas'] == 0:
                flash(f"Acabaram suas tentativas. A palavra era: {session['sorte']}", 'danger')
                return redirect('/reiniciar')
            return redirect('/jogo')
    oculta = palavra_oculta(session['sorte'], session['letras_tentadas'])

    return render_template('jogo.html', oculta=oculta, letras=session['letras_tentadas'],
                           tentativas=session['tentativas'])


@forca.route('/reiniciar')
def reiniciar():
    session.clear()
    return redirect('/')

@forca.route('/palavras')
def palavras_list():
    dados = palavras()
    return render_template('palavras.html', palavras=dados['palavras'])


if __name__ == "__main__":
    forca.run(debug=True)
