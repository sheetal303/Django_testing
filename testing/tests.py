from django.test import TestCase
from .models import Post

# Create your tests here.


class Model_test(TestCase):
    def setUp(self):
        self.blog = Post.objects.create(title="flutter", author="gangu")

    def test_post_model(self):
        d = self.blog
        self.assertEqual(str(d), "flutter")
        self.assertTrue(isinstance(d, Post))
