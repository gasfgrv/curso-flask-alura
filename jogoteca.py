from flask import Flask, render_template, request, redirect, session, flash


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo(nome='Tetris', categoria='Puzzle', console='Atari')
jogo2 = Jogo(nome='God of War', categoria='Rack n Slash', console='PS2')
jogo3 = Jogo(nome='Mortal Kombat', categoria='Luta', console='PS2')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'jogoteca'


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'mario' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(f"{session['usuario_logado']} logado com sucesso")
        return redirect('/')

    flash('Usuário não logado logado')
    return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect('/')


app.run(debug=True)
