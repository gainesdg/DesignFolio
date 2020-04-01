##Design Grid

####Setup:
	
1.	Clone the repo using : 
`git clone https://github.com/gainesdg/DesignFolio.git`

2.	Setup a virtual environment.

3.	Install the necassary python modules using:  
`pip install –r requirements.txt.`

4.	Navigate inside of the directory 'DesignFolio' containing 'manage.py'

5.	Prepare the database using:	
`python manage.py makemigrations`
`python manage.py migrate`

6.	Populate the databasing using:	
`python populate_script.py`

7.	Run the development server using: 
`python manage.py runserver.`
	
If images are not loading check settings.py in 'DesignFolio > design_grid > settings.py' Scroll down and check that `DEBUG = True`


####Dependancies:
*	[JQuery](https://code.jquery.com/jquery-3.4.1.min.js)
*	[Font](https://fonts.googleapis.com/css?family=Nunito|Quicksand&display=swap)
*	[Boostrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
*	[Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)