#!/venv/bin/python3
from flask import Flask, render_template, g

PATH = ('/db/jobs.sqlite')

engine = create_engine('sqlite:///jobs.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

open_connection = get_addr('_connection')
if _connection == None:
	set _connection == session
	pass

app = Flask(__name__) 

@app.route('/')
@app.route('/jobs')
def jobs():
	return render_template('index.html')
