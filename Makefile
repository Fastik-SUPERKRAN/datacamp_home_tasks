
migrate:
	python manage.py makemigrations
	@( read -p "Migrate? [Y/n]: " sure && case "$$sure" in [yY]) true;; *) false;; esac )
	python manage.py migrate
