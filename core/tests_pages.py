from django.test import TestCase
from django.urls import reverse


class IndexPage(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')

    def test_index_page_contains_correct_html(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response,
                            '<p>Welcom to gym wourkout app</p>')

    def test_index_page_does_not_contains_incorrect_html(self):
        response = self.client.get(reverse('index'))
        self.assertNotContains(response, 'This is not correct html')


class LoginPage(TestCase):

    def test_status_code(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')

    def test_contains_correct_html(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, '<h2>Log in</h2>')

    def test_does_not_contains_incorrect_html(self):
        response = self.client.get(reverse('login'))
        self.assertNotContains(response, 'This is not a login page')


class SignupPage(TestCase):

    def test_status_code(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_cortect_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html')

    def test_contains_correct_html(self):
        response = self.client.get(reverse('signup'))
        self.assertContains(response, '<h2>Sign up</h2>')

    def test_does_not_contains_incorrect_html(self):
        response = self.client.get(reverse('signup'))
        self.assertNotContains(response, 'Some bad code in here.')
