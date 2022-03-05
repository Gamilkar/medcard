server:
	pipenv run flask run


migrate:
	pipenv run flask db migrate


db upgrade:
	pipenv run flask db upgrade

shell:
	pipenv run flask shell

