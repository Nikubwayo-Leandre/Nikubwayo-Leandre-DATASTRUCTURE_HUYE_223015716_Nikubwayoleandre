from collections import deque
applied_jobs_stack = []
job_postings_queue = deque()
available_jobs = []
def post_job(job):
    job_postings_queue.append(job)
    available_jobs.append(job)
    print(f"New job posted: {job}")
def process_job_posting():
    if job_postings_queue:
        job = job_postings_queue.popleft()
        print(f"Job '{job}' is now live.")
    else:
        print("No job postings to process.")
def apply_for_job(job):
    if job in available_jobs:
        available_jobs.remove(job)
        applied_jobs_stack.append(job)
        print(f"Applied for job: {job}")
    else:
        print(f"Job '{job}' is not available.")
def undo_last_application():
    if applied_jobs_stack:
        job = applied_jobs_stack.pop()
        available_jobs.append(job)
        print(f"Undo application for job: {job}")
    else:
        print("No applications to undo.")
def display_available_jobs():
    if available_jobs:
        print("Available jobs:")
        for job in available_jobs:
            print(f"- {job}")
    else:
        print("No available jobs at the moment.")
def display_applied_jobs():
    if applied_jobs_stack:
        print("Jobs you have applied for:")
        for job in applied_jobs_stack:
            print(f"- {job}")
    else:
        print("You haven't applied for any jobs yet.")
post_job("Software Engineer")
post_job("Data Scientist")
post_job("DevOps Engineer")
process_job_posting()
process_job_posting()
display_available_jobs()
apply_for_job("Software Engineer")
display_applied_jobs()
undo_last_application()
display_available_jobs()
process_job_posting()