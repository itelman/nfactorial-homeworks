from django.test import TestCase
from django.urls import reverse

from news.models import News, Comment


class TestViewsModel(TestCase):

    def setUp(self):
        """Create test data."""
        self.news1 = News.objects.create(title="News 1", content="Content 1")
        self.news2 = News.objects.create(title="News 2", content="Content 2")

        self.comment1 = Comment.objects.create(news=self.news1, content="Comment 1")
        self.comment2 = Comment.objects.create(news=self.news1, content="Comment 2")

    def test_news_list_ordering(self):
        """Test if news list is ordered by created_at (newest first)."""
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)
        news_list = response.context['news']
        self.assertEqual(news_list[0], self.news2)  # Newest first
        self.assertEqual(news_list[1], self.news1)  # Oldest second

    def test_news_detail(self):
        """Test if news detail page shows the correct news item."""
        response = self.client.get(reverse('news_detail', args=[self.news1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.news1.title)
        self.assertContains(response, self.news1.content)

    def test_news_detail_shows_sorted_comments(self):
        """Test if comments on news detail page are sorted by created_at (newest first)."""
        response = self.client.get(reverse('news_detail', args=[self.news1.id]))
        self.assertEqual(response.status_code, 200)
        comments = response.context['comments']
        self.assertEqual(comments[0], self.comment2)  # Newest first
        self.assertEqual(comments[1], self.comment1)  # Oldest second
