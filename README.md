##Design Grid

####What is Design Grid?

You can think of Design Grid as a professional Instagram in the same way Linkedin is a professional Facebook. Design Grid is a website where people can upload Images and build up a portfolio. You can find the posts seperated by the professions of users (e.g you can find posts by Artists in the Artist section). This website is also for potential employers. If someone is looking to commision someone for a piece of art and design, they can filter posts in each profession by a series of Tags as to find what they are looking for and from their can get in contact with the user if they are available for commisions.

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

####Running Tests:

Close the server if it is running.
Run the test using:
`python manage.py test`


####Dependancies:
*	[JQuery](https://code.jquery.com/jquery-3.4.1.min.js)
*	[Font](https://fonts.googleapis.com/css?family=Nunito|Quicksand&display=swap)
*	[Boostrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
*	[Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)