from unittest import mock
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from unittest import mock
from .views import *
from .models import CustomUser


mock_message = mock.MagicMock()
mock_login = mock.MagicMock()
mock_authenticate = mock.MagicMock()
mock_form = mock.MagicMock()
mock_populate_category = mock.MagicMock()

# Create your tests here.
class AuthViewsTest(TestCase):

    # Set up
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.company_name = "test_company"
        self.username = "test_username"
        self.email = "test@email.com"
        self.password = "test_password"
        self.role = CustomUser.PENCATAT
        self.user = CustomUser.objects.create_user(
            company_name = self.company_name,
            username = self.username,
            email = self.email,
            password = self.password
        )

    def tearDown(self):
        mock_message.reset_mock()
        mock_login.reset_mock()
        mock_authenticate.reset_mock()
        mock_form.reset_mock()
        mock_populate_category.reset_mock()
    
    def test_login_page_renders_correct_template(self):
        # Make a GET request to the login view
        response = self.client.get(reverse('login'))

        # Check the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check the correct template was used
        self.assertTemplateUsed(response, 'login.html')

    @mock.patch('django.contrib.messages.warning', mock_message)
    def test_login_already_authenticated(self):
        # Mock the requests
        request = self.factory.post(reverse('login'))
        request.user = mock.MagicMock(is_authenticated=True)

        mock_message.side_effect = [""]

        # Call the view
        response = login(request)

        # Check the response
        self.assertEqual(response.status_code, 302) # Redirects
        self.assertEqual(response['Location'], '/')

    @mock.patch('django.contrib.auth.authenticate', mock_authenticate)
    @mock.patch('django.contrib.auth.login', mock_login)
    @mock.patch('django.contrib.messages.success', mock_message)
    def test_login_success(self):
        mock_authenticate.side_effect = [self.user]
        mock_login.side_effect = [None]
        mock_message.side_effect = [""]

        response = self.client.post(reverse('login'), {
            'email': 'test@email.com',
            'password': 'test_password',
        })
        
        self.assertTrue(self.user.is_authenticated)
        self.assertEqual(response.status_code, 302) # Redirects
    
    @mock.patch('django.contrib.auth.authenticate', mock_authenticate)
    @mock.patch('django.contrib.auth.login', mock_login)
    @mock.patch('django.contrib.messages.error', mock_message)
    def test_login_incorrect_credentials(self):
        mock_authenticate.side_effect = [None]
        mock_login.side_effect = [None]
        mock_message.side_effect = [""]

        response = self.client.post(reverse('login'), {
            'email': 'test@email.com',
            'password': 'test_password',
        })

        # Check the response
        self.assertEqual(response.status_code, 302) # Redirects
        self.assertEqual(response['Location'], '/login/')

    @mock.patch('django.contrib.auth.logout', mock_login)
    @mock.patch('django.contrib.messages.info', mock_message)
    def test_logout_success(self):
        mock_login.side_effect = [None]
        mock_message.side_effect = [""]

        response = self.client.post(reverse('logout'))

        # Check the response
        self.assertEqual(response.status_code, 302) # Redirects
        self.assertEqual(response['Location'], '/login/')
    
    @mock.patch('django.contrib.messages.warning', mock_message)
    def test_register_already_authenticated(self):
        # Mock the requests
        request = self.factory.post(reverse('register'))
        request.user = mock.MagicMock(is_authenticated=True)

        mock_message.side_effect = [""]

        # Call the view
        response = register(request)

        # Check the response
        self.assertEqual(response.status_code, 302) # Redirects
        self.assertEqual(response['Location'], '/')

    # @mock.patch('users.forms.UserForm.is_valid', mock_form)
    # @mock.patch('django.contrib.messages.success', mock_message)
    def test_register_success(self):
        # register_form = {
        #     'company_name' : 'test_company',
        #     'username' : 'test_username',
        #     'email' : 'test@email.com',
        #     'password' : 'test_password',
        # }
        # custom_form = UserForm(register_form)
        # self.assertTrue(custom_form.is_valid)

        # mock_form.side_effect = [register_form]
        # mock_populate_category.side_effect = [None]
        # mock_message.side_effect = [""]
        # response = self.client.post(reverse('register'), register_form)
        pass

    @mock.patch('users.forms.UserForm.is_valid', mock_form)
    @mock.patch('django.contrib.messages.error', mock_message)
    def test_register_invalid_form(self):
        mock_form.side_effect = [False]
        mock_message.side_effect = [""]

        response = self.client.post(reverse('register'))

        # Check the response
        self.assertEqual(response.status_code, 302) # Redirects
        self.assertEqual(response['Location'], '/register/')

    def test_register_page_renders_correct_template(self):
        # Make a GET request to the login view
        response = self.client.get(reverse('register'))

        # Check the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check the correct template was used
        self.assertTemplateUsed(response, 'register.html')