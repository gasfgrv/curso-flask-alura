import time

from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from flask_bcrypt import check_password_hash

from helpers import recupera_imagem, deleta_arquivo, FormularioJogo, FormularioUsuario
from jogoteca import app, db
from models import Jogos, Usuarios


@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo')))

    form = FormularioJogo()
    return render_template('novo.html', titulo='Novo jogo', form=form)


@app.route('/criar', methods=['POST'])
def criar():
    form = FormularioJogo(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('novo'))

    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data

    jogo = Jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash('Jogo já existente!')
        return redirect(url_for('index'))

    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{upload_path}/capa-{novo_jogo.id}-{timestamp}.jpg')

    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id_jogo):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('editar', id=id_jogo)))

    jogo = Jogos.query.filter_by(id=id_jogo).first()

    form = FormularioJogo()
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.categoria

    capa_jogo = recupera_imagem(id_jogo)
    return render_template('editar.html', titulo='Editando jogo', id=id_jogo, capa_jogo=capa_jogo, form=form)


@app.route('/atualizar', methods=['POST'])
def atualizar():
    form = FormularioJogo(request.form)

    if form.validate_on_submit():
        jogo = Jogos.query.filter_by(id=request.form['id']).first()
        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.console = form.console.data

        db.session.add(jogo)
        db.session.commit()

        arquivo = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        timestamp = time.time()
        deleta_arquivo(jogo.id)
        arquivo.save(f'{upload_path}/capa-{jogo.id}-{timestamp}.jpg')

    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id_jogo):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo')))

    Jogos.query.filter_by(id=id_jogo).delete()
    db.session.commit()
    flash('Jogo deletado com sucesso!')

    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        flash(f"{usuario.nickname} logado com sucesso")
        proxima_pagina = request.form['proxima']

        if proxima_pagina == "None":
            proxima_pagina = url_for('index')

        return redirect(proxima_pagina)

    flash('Usuário não logado')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)
