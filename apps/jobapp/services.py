from django.shortcuts import get_object_or_404
from jobapp.models import Job

def toggle_job_status(user_id: int, job_id: int) -> bool:
    """Marks a job as closed."""
    job = get_object_or_404(Job, id=job_id, user=user_id, is_deleted=False)
    job.is_closed = True
    job.save()
    return True
