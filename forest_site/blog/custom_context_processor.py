from .models import Post


def latest_news(request):
    newsest_news = Post.objects.first()
    return {
       'newsest_news': newsest_news
    }
