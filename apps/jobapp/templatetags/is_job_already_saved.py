from django import template

from jobapp.models import BookmarkJob

register = template.Library()


@register.simple_tag(name='is_job_already_saved')
def is_job_already_saved(job, user):
    return BookmarkJob.objects.filter(job=job, user=user, is_deleted=False).exists()
