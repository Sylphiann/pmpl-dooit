from unittest import mock
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.contrib import auth
from unittest import mock
from .views import login
from .models import CustomUser


mock_message = mock.MagicMock()
mock_login = mock.MagicMock()
mock_authenticate = mock.MagicMock()
mock_render = mock.MagicMock()

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
        mock_render.reset_mock()
    
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

    def test_logout_success(self):
        pass

    def test_register_already_authenticated(self):
        pass

    def test_register_success(self):
        pass

    def test_register_invalid_form(self):
        pass

    def test_register_non_post_request(self):
        pass

class AuthFormsTest(TestCase):
    def setup():
        pass

    def userform_clean_success(self):
        pass

    def userform_clean_incorrect_password(self):
        pass

class AuthModelsTest(TestCase):
    pass

class AuthSignalsTest(TestCase):
    pass

class AuthValidatorsTest(TestCase):
    pass