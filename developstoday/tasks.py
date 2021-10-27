from celery import shared_task

from news.models import News


@shared_task
def clean_upvotes():
    for news in News.objects.all():
        news.upvotes = 0
        news.save()
    return "Upvotes cleaned!"


@shared_task
def test_func():
    return 'Test!'
