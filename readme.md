# 🚀 Flask - Guia Rápido

Flask é um microframework Python de código aberto, criado para desenvolver aplicações web rápidas, simples e eficientes.
Ele fornece apenas o núcleo essencial, permitindo adicionar bibliotecas conforme necessário.

**Principais características:**

| Característica  | Descrição                                   |
|-----------------|---------------------------------------------|
| Simplicidade    | Menos código extra, aplicação mais leve     |
| Rapidez         | Fácil de configurar e executar              |
| Eficiência      | Maior controle sobre o código               |
| Extensibilidade | Bibliotecas adicionais podem ser integradas |

--- 

## 📦 Instalação

```shell
pip install flask
```

---

## ⚡ Primeira Aplicação

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def ola():
    return render_template('lista.html')


app.run(debug=True, port=8080)

```

**Observações:**

* Rotas: `@app.route('/rota')`
* HTML no diretório `templates`
* `render_template('arquivo.html')` vincula rota a template
* `app.run(debug=True)` ativa hot reload
* Porta padrão: 5000 (pode ser alterada com `port=8080`)

---

## 📝 Templates e Conteúdo Dinâmico

**Sintaxe básica do Jinja2:**

```html
{{ var }}       <!-- Exibe valor -->
{% for item in lista %} <!-- Loop -->
<tr>
    <td>{{ item.nome }}</td>
    <td>{{ item.categoria }}</td>
</tr>
{% endfor %}

```

**Filtros úteis:**

| Filtro             | Função                        |
|--------------------|-------------------------------|
| `upper`            | Maiúsculas                    |
| `title`            | Primeira letra maiúscula      |
| `round`            | Arredonda números             |
| `trim`             | Remove espaços                |
| `default('texto')` | Valor padrão se variável nula |

**Delimitadores importantes:**

* `{{ ... }}` → exibir valores
* `{% ... %}` → lógica/estrutura
* `{# ... #}` → comentários invisíveis no HTML

**Templates base e blocos:**

```html
{% extends "template.html" %}
{% block nome_do_bloco %}
<!-- Conteúdo substituído -->
{% endblock %}
```

---

## 🖊️ Formulários e Métodos

```python
from flask import request

console = request.form['console']  # name do input

```

**Rotas com métodos diferentes:**

```python
@app.route('/rota', methods=['GET', 'POST'])
def funcao():
    ...

```

--- 

## 🔄 Redirecionamento e Flash Messages

**Redirecionamento:**

```python
from flask import redirect

return redirect('/')
```

**Mensagens rápidas:**

```python
from flask import flash

flash('Mensagem enviada!')
```

**Template:**

```html
{% with messages = get_flashed_messages() %}
{% if messages %}
<ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}
{% endwith %}
```

--- 

## 🔐 Sessions

* Permite armazenar dados temporários entre requests.
* Requer chave secreta:

```python
app.secret_key = 'alura'
```

**Observações:**

* Não armazenar dados sensíveis
* Limite ~4 KB
* Cookies assinados criptograficamente

---

## 💾 Persistência com Banco de Dados

* Compatível com **SQLAlchemy**.
* ORM converte objetos Python em tabelas SQL.
* **Vantagens:** independente de SGBD, seguro, robusto.
* **Desvantagens:** pode criar falsa sensação de que SQL não é necessário; integração com sistemas legados pode ser
  difícil.

| Linguagem       | ORM                        |
|-----------------|----------------------------|
| Python + Flask  | SQLAlchemy                 |
| Python + Django | Django ORM                 |
| Java            | Hibernate                  |
| C#              | Dapper ORM                 |
| PHP             | Doctrine                   |
| .NET            | Microsoft Entity Framework |

---

## ⚔️ Flask vs Django

Mais detalhes: [Django ou Flask - Alura](https://www.alura.com.br/artigos/django-ou-flask)

| Aspecto  | Flask                    | Django                             |
|----------|--------------------------|------------------------------------|
| Tipo     | Microframework           | Framework completo                 |
| Ideal    | Projetos pequenos/médios | Projetos grandes                   |
| Recursos | Essencial, extensível    | ORM, autenticação, admin, completo |
