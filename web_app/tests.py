from django.test import TestCase
from django.urls import reverse

from web_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.template.defaultfilters import slugify

#--------------------------------MODELS---------------------------------#

#profession
class ProfessionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Profession.objects.create(name='Artist',picture='profession_images/6351-modern-cityscape-painting.jpg.png')
    
    def test_profession_string(self):
        profession = Profession.objects.get(id=1)
        self.assertEquals('Artist', profession.name)

    def test_profession_slug(self):
        profession = Profession.objects.get(id=1)
        expected_object_slug = slugify(profession.name)
        self.assertEquals(expected_object_slug, profession.slug)

# profile
class UserProfileTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        u = User.objects.create(first_name='Joe',
            last_name='Subbiani',
            username='JoeSubbi',
            email='joe.subbiani@gmail.com',
            password=make_password('password123'))
        p = Profession.objects.create(name='Artist',picture='profession_images/6351-modern-cityscape-painting.jpg.png')
        
        UserProfile.objects.create(user=u, profession=p)

    def test_profile_string(self):
        profile = UserProfile.objects.get(id=1)
        expected_object_string = f'{profile.user.username}'
        self.assertEquals(expected_object_string, str(profile))

    def test_profile_slug(self):
        profile = UserProfile.objects.get(id=1)
        expected_object_slug = slugify(profile.user.username)
        self.assertEquals(expected_object_slug, profile.slug)


#--------------------------------VIEWS----------------------------------#

#INDEX
class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(4):
            Profession.objects.create(name=f'Profession{i}',picture='profession_images/designbig.jpg.png')

    #Test correct template and URL patterns
    def test_view_url_exists_at_desired_location1(self):
        response = self.client.get('/design-grid/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_exists_at_desired_location2(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location3(self):
        response = self.client.get('/design-grid/index')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name1(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_url_accessible_by_name2(self):
        response = self.client.get(reverse('design-grid:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_app/index.html')

    #Test page content
    def test_list_of_professions_in_context(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('professions' in response.context)
        self.assertTrue(len(response.context['professions']) == 4)


#PROFESSION PAGE
class ProfessionViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(4):
            p = Profession.objects.create(name=f'Profession{i}',picture='profession_images/designbig.jpg.png')
            u = User.objects.create(username=f'user{i}', password=make_password('password123'))
            up = UserProfile.objects.create(user=u, profession=p)
            s = Section.objects.create(name='section1', user=u)
            for j in range(4):
                tag = Tags.objects.create(name=f'Tag{j}', profession=p)
                post = Posts.objects.create(section=s,picture='profession_images/designbig.jpg.png')
                PostTags.objects.create(post=post, tag=tag)

    #Test correct template and URL patterns
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/design-grid/profession/profession1/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('design-grid:profession', kwargs={'profession_name_slug': 'profession1'}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('design-grid:profession',kwargs={'profession_name_slug': 'profession1'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_app/profession.html')

    def test_correct_template_if_profession_does_not_exist(self):
        response = self.client.get(reverse('design-grid:profession',kwargs={'profession_name_slug': 'p1'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_app/missing_content.html')

    #Test page content
    def test_list_of_tags_in_context(self):
        response = self.client.get(reverse('design-grid:profession',kwargs={'profession_name_slug': 'profession1'}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('tags' in response.context)
        self.assertEquals(len(response.context['tags']), 4)

    def test_profession_in_context(self):
        response = self.client.get(reverse('design-grid:profession',kwargs={'profession_name_slug': 'profession1'}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('profession' in response.context)
        self.assertEquals(response.context['profession'].id, 2)
    

#PROFILE PAGE
class ProfileViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        p = Profession.objects.create(name=f'Profession',picture='profession_images/designbig.jpg.png')
        av=[True, False, True]
        for i in range(len(av)):
            u = User.objects.create(username=f'user{i}', password=make_password('password123'))
            up = UserProfile.objects.create(user=u, profession=p, available=av[i])

    #Test correct template and URL patterns
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/design-grid/user/user1/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('design-grid:profile', kwargs={'user_name_slug': 'user1'}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('design-grid:profile',kwargs={'user_name_slug': 'user1'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_app/profile.html')

    def test_correct_template_if_profession_does_not_exist(self):
        response = self.client.get(reverse('design-grid:profile',kwargs={'user_name_slug': 'u1'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_app/missing_content.html')

    #Test page content
    def test_user_profile_context(self):
        response = self.client.get(reverse('design-grid:profile',kwargs={'user_name_slug': 'user1'}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('profile' in response.context)
        self.assertTrue('available' in response.context)
        available=False
        if response.context['available'] == 'Available':
            available=True
        self.assertEquals(available, UserProfile.objects.get(id=2).available)

    def test_user_buttons_if_logged_in(self):
        response = self.client.get(reverse('design-grid:profile',kwargs={'user_name_slug': 'user0'}))
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        self.assertTrue('Log in to get contact details' in response.content.decode())
        self.client.login(username='user1', password='password123')
        response = self.client.get(reverse('design-grid:profile',kwargs={'user_name_slug': 'user0'}))
        self.assertFalse('Log in to get contact details' in response.content.decode())

#POST VIEWS
class PostViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        p = Profession.objects.create(name=f'Artist',picture='profession_images/designbig.jpg.png')
        for i in range(4):
            u = User.objects.create(username=f'user{i}', password=make_password('password123'))
            up = UserProfile.objects.create(user=u, profession=p)
            s = Section.objects.create(name='section1', user=u)

        s = Section.objects.get(name='section1',user=User.objects.get(username='user1'))
        for i in range(4):
            post = Posts.objects.create(section=s,picture='profession_images/designbig.jpg.png')
            for j in range(3):
                PostLikes.objects.create(post=post, user=User.objects.get(username=f'user{j}'))

    #Test correct template and URL patterns
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/design-grid/post/1/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('design-grid:post', kwargs={'posts_pid': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('design-grid:post', kwargs={'posts_pid': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_app/post.html')

    def test_correct_template_if_post_does_not_exist(self):
        response = self.client.get(reverse('design-grid:post', kwargs={'posts_pid': 6}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_app/missing_content.html')

    #Test page content
    def test_post_context(self):
        response = self.client.get(reverse('design-grid:post', kwargs={'posts_pid': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('post' in response.context)
        self.assertTrue('tags' in response.context)
        self.assertTrue('likes' in response.context)
        self.assertTrue('profile' in response.context)

    def test_likes_is_4(self):
        response = self.client.get(reverse('design-grid:post', kwargs={'posts_pid': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['likes'] , 3)

    def test_logged_in_to_like(self):
        response = self.client.get(reverse('design-grid:post', kwargs={'posts_pid': 1}))
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        self.assertTrue('Log in to Like Post' in response.content.decode())
        self.client.login(username='user1', password='password123')
        response = self.client.get(reverse('design-grid:post', kwargs={'posts_pid': 1}))
        self.assertFalse('Log in to Like Post' in response.content.decode())
        
#SEARCH
class SearchViewtest(TestCase):
    @classmethod
    def setUpTestData(cls):
        p = Profession.objects.create(name=f'Artist',picture='profession_images/designbig.jpg.png')
        loc=['Wales','England','Scotland','Ireland']
        for i in range(len(loc)):
            u = User.objects.create(username=f'user{i}', password=make_password('password123'))
            up = UserProfile.objects.create(user=u, profession=p, location=loc[i])
            s = Section.objects.create(name='section1', user=u)

        s = Section.objects.get(name='section1',user=User.objects.get(username='user1'))
        for i in range(4):
            post = Posts.objects.create(section=s,picture='profession_images/designbig.jpg.png',title=f'title{i}')

    #Test correct template and URL patterns
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/design-grid/search/e/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('design-grid:search', kwargs={'argument': 'e'}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('design-grid:search', kwargs={'argument': 'e'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_app/search.html')

    #Test page content
    def test_search_context(self):
        response = self.client.get(reverse('design-grid:search', kwargs={'argument': 'e'}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('users' in response.context)
        self.assertTrue('location' in response.context)
        self.assertTrue('posts' in response.context)

    def test_number_of_search_results(self):
        response = self.client.get(reverse('design-grid:search', kwargs={'argument': 'e'}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['users']), 4)
        self.assertEqual(len(response.context['location']), 3)
        self.assertEqual(len(response.context['posts']), 4)