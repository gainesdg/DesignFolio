Design Grid

Setup:
	Clone the repo using : git clone https://github.com/gainesdg/DesignFolio.git
	Setup a virtual environment.
	Install the necassary python modules using:  pip install –r requirements.txt.
	Navigate inside of the directory 'DesignFolio' containing 'manage.py'
	Prepare the database using:	python manage.py makemigrations
					python manage.py migrate
	Populate the databasing using:	python populate_script.py
	Run the development server using: python manage.py runserver.
	
	If images are not loading check settings.py in 'DesignFolio > design_grid > settings.py'
		Scroll down and check that DEBUG = True


Dependancies:
JQuery
https://code.jquery.com/jquery-3.4.1.min.js
	
Font
https://fonts.googleapis.com/css?family=Nunito|Quicksand&display=swap

Boostrap
https://getbootstrap.com/docs/4.4/getting-started/introduction/


Images:
All Images for Professions (home page) are labbeled for reuse.
All other images are orignal works by me, Joe Subbiani.