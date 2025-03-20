# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CommentForm
from .forms import NewsForm
from .models import Comment
from .models import News


# View to list all news (sorted by newest first)
def news_list(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': news})


# View to show full news details
def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    comments = Comment.objects.filter(news=news)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('news_detail', news_id=news.id)
    else:
        comment_form = CommentForm()

    return render(request, 'news/news_detail.html', {'news': news, 'comments': comments, 'comment_form': comment_form})


# View to add news
def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('news_detail', news_id=news.id)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})


class NewsUpdateView(View):
    def get(self, request, news_id):
        news = get_object_or_404(News, id=news_id)
        form = NewsForm(instance=news)
        return render(request, 'news/edit_news.html', {'form': form, 'news': news})

    def post(self, request, news_id):
        news = get_object_or_404(News, id=news_id)
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect(f'/news/{news.id}/')  # Redirect to updated news
        return render(request, 'news/edit_news.html', {'form': form, 'news': news})
