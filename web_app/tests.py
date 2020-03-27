from django.test import TestCase

# Create your tests here.

#UNPOPULATED

#INDEX
#message saying no professions exist
#drop down menu saying no professions exist

#PROFESSIONS
#missing content page

#USERS
#missing content page

#POSTS
#missing content page


#------------------------------------------------------------------------#

#POPULATED

#INDEX
#all professions are there. 
#base nav bar drop down menu contains professions

#PROFESSIONS
#display list of tags
#display posts. first post should be ___

#USERS
#user profile has expected url
#user profile has expected username, first and last name, location and bio
#user is available
    #if logged in
        #email visible
    #else
        #email not visible
#check button to add link is not available on 1 profile

#POSTS
#check post 1
#correct title
#correct description
#correct number of likes
#like button
    #if logged in like button available
        #if post has been liked by user does it say 'unlike'
            #if click does it say 'like' and have likes gone down
    #if not
        #does it tell user to log in
    
#display image
#correct message if image does not exist (has been deleted from media files)

#SEARCH
#search 'an'
#users returns tanisha89
#location returns none
#posts return mandolorian, alita and spartan


