from flask import Flask, render_template


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)


@app.route('/inicio')
def ola():
    jogo1 = Jogo(nome='Tetris', categoria='Puzzle', console='Atari')
    jogo2 = Jogo(nome='God of War', categoria='Rack n Slash', console='PS2')
    jogo3 = Jogo(nome='Mortal Kombat', categoria='Luta', console='PS2')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run()
