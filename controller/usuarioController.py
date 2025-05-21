from app import app
from flask import render_template,request, jsonify
from sqlalchemy.orm import sessionmaker

from model.conexao import engine
from model.usuario import *

Sesssiolocal =sessionmaker(autocommit=False,bind=engine)



@app.route("/usuarios/novo", methods=["GET"])
def novo ():
    return render_template("index.html")

@app.route('/usuarios/salvar', methods=['POST'])
def create():
    db = Sesssiolocal()
    uso = usuario(nome=request.form['nome'],
                      data=request.form['aniversario'])
    db.add(uso)
    db.commit()
    return jsonify({'msg':'salvo com sucesso'}), 200

@app.route("/usuarios", methods=["GET"])
def usuarios():
    db = Sesssiolocal()
    usuarios = db.query(usuario).all()
    return jsonify([usuario.to_dict() for usuario in usuarios]), 200

@app.route("/usuarios/<int:id>", methods =["GET"])
def get_usuarios(id):
    db = Sesssiolocal()
    usu = db.query(usuario).get(id)
    if(usu):
        return jsonify(usu.to_dict()), 200
    else:
        return jsonify({'msg': 'usuario não encontrado'}), 404

@app.route("/usuarios/<int:id>", methods =["DELETE"])
def delete_usuarios(id):
    db = Sesssiolocal()
    usu = db.query(usuario).get(id)
    if(usu):
       db.delete(usu)
       db.commit()
       return jsonify({'usuario apagado'}), 204
    else:
        return jsonify({'msg': 'usuario não encontrado'}), 404

@app.route("/usuarios", methods =["POST"])
def creat_usuarios():
    db = Sesssiolocal()
    data = request.get_json()
    usu = usuario(nome=data['nome'], data=data['aniversario'])
    db.add(usu)
    db.commit()
    return jsonify({'msg':'usuario criado com sucesso!',
                     'usu':usu.to_dict()}), 201



@app.route("/usuarios/<int:id>", methods =["PUT"])
def update_usuarios(id):
    db = Sesssiolocal()
    ub = db.query(usuario).get(id)
    data= request.get_json()
    ub.nome = data['nome']
    ub.data = data['aniversario']

    db.commit()
    return jsonify({'msg':'usuario atualizado com sucesso!',
                     'usu':ub.to_dict()}), 200

