from celery import shared_task
from django.utils import timezone


@shared_task
def check_published_posts():
    from .models import Post

    unpublished_posts = Post.objects.filter(
        published__lte=timezone.now(), status="draft"
    )
    for post in unpublished_posts:
        post.status = "published"
        post.save()
