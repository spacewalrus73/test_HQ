MANAGE := poetry run python3 manage.py

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

.PHONY: migrations
migrations:
	@$(MANAGE) makemigrations

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: install
install:
	@poetry install

.PHONY: db-clean
db-clean:
	@rm db.sqlite3 || true

.PHONY: run
run:
	@$(MANAGE) runserver

.PHONY: lint
lint:
	@poetry run flake8 test_HQ

.PHONY: port-clean
port-clean:
	sudo fuser -k 8000/tcp

.PHONY: test
test:
	@$(MANAGE) test --parallel auto