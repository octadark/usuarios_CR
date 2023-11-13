from flask import Flask, render_template, redirect, request
from users import User

app = Flask(__name__)
#pagina principal
@app.route('/')
def index():
    return redirect('/users')

#pagina principal
@app.route('/users')
def users():
    return render_template("users.html", users=User.get_all())

#Pagina de crear usuario
@app.route('/user/new')
def new():
    return render_template("new_user.html")

#Crear usuario
@app.route('/user/create', methods=['POST'])
def create():
    print (request.form)
    User.save(request.form)
    return redirect('/users')

#Editar usuario
@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id" : id
    }
    return render_template("edit_user.html", user=User.get_one(data))

#informacion del usuario
@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id" : id
    }
    return render_template("show_user.html", user=User.get_one(data))

#Actualizar usuario
@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

#Eliminar usuario
@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        "id" : id
    }
    User.delete(data)
    return redirect('/users')

if __name__=="__main__":
    app.run(debug=True)