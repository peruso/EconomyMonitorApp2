from django.test import SimpleTestCase 
from django.urls import reverse

class HomepageTests(SimpleTestCase):#page60に関数を使って少し短くする方法の記載あるので理解したのち後でそれを修正
  def test_homepage_status_code(self):
    response = self.client.get('/') 
    self.assertEqual(response.status_code, 200)

  def test_homepage_url_name(self):
    response = self.client.get(reverse('home')) #これ何か後で調べよう
    self.assertEqual(response.status_code, 200)

  def test_homepage_template(self): 
    response = self.client.get('/') 
    self.assertTemplateUsed(response, 'home.html')

  def test_homepage_contains_correct_html(self): 
    response = self.client.get('/') 
    self.assertContains(response, 'Homepage')

  def test_homepage_does_not_contain_incorrect_html(self): 
    response = self.client.get('/')
    self.assertNotContains(
            response, 'Hi there! I should not be on the page.')