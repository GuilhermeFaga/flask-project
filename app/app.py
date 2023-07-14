from flask import Flask, redirect, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import Regexp, InputRequired, NumberRange
from jinja2 import Environment, FileSystemLoader, select_autoescape
import requests
import json
import os
import re

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

SECRET_KEY = os.urandom(32)

app = Flask(__name__, 
	template_folder='templates', 
	static_folder='static', 
	static_url_path='')

app.config['SECRET_KEY'] = SECRET_KEY


class BuscarCEPForm(FlaskForm):
	cep = IntegerField('CEP', validators=[InputRequired()], render_kw={"placeholder": "01409000"})

class BuscarIPForm(FlaskForm):
	ip = StringField('IP', validators=[InputRequired()], render_kw={"placeholder": "8.8.8.8"})


@app.route('/')
def root():
	return redirect(url_for('busca'))


@app.route('/busca')
def busca():
	cepform = BuscarCEPForm()
	ipform = BuscarIPForm()
	return env.get_template("busca.html").render(cepform=cepform, ipform=ipform)


@app.route('/api/busca-cep')
def api_busca_cep():

	if (request.method != 'GET'):
		return 'Method not allowed', 405

	cep = request.args.get('cep', '')

	if not re.match(r'^\d{8}$', cep):
		return 'CEP inválido', 400

	if (cep == ''):
		return 'CEP não informado', 400

	url = 'https://viacep.com.br/ws/{}/json/'.format(cep)

	response = requests.get(url)

	if response.status_code != 200:
		return 'Erro ao consultar CEP', 500

	data = response.json()

	return data


@app.route('/api/busca-ip')
def api_busca_ip():

	if (request.method != 'GET'):
		return 'Method not allowed', 405

	ip = request.args.get('ip', '')

	if not re.match(r'^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$', ip):
		return 'IP inválido', 400

	if (ip == ''):
		return 'IP não informado', 400

	url = 'https://ipapi.co/{}/json/'.format(ip)

	response = requests.get(url)

	if response.status_code != 200:
		return 'Erro ao consultar IP', 500

	data = response.json()

	return data


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
