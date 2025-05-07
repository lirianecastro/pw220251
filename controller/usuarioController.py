from app import app
from flask import render_template,request, jsonify
from sqlalchemy.orm import sessionmaker

from model.conexao import engine
from model.usuario import *

Sesssiolocal =sessionmaker(autocommit=False,bind=engine)

@app.route("/usuarios", methods=["GET"])
def usuarios():
    db = Sesssiolocal()
    usuarios = db.query(usuario).all()
    return jsonify([usuario.to_dict() for usuario in usuarios]), 200

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
