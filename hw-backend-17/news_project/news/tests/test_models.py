from django.test import TestCase

from news.models import News, Comment


class TestNewsModel(TestCase):

    def test_has_comments_returns_true(self):
        """Test if has_comments returns True when there are comments."""
        news = News.objects.create(title="Test News", content="Some content")
        Comment.objects.create(news=news, content="Test comment")

        self.assertTrue(news.has_comments())

    def test_has_comments_returns_false(self):
        """Test if has_comments returns False when there are no comments."""
        news = News.objects.create(title="Test News", content="Some content")

        self.assertFalse(news.has_comments())
