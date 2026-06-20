from config import US_ONLY

def filter_locations(jobs):
    if not US_ONLY:
        return jobs

    filtered_jobs = []

    for job in jobs:
        location = str(job.get("location", "")).lower()

        if (
            "united states" in location
            or "usa" in location
            or "united states (remote)" in location
        ):
            filtered_jobs.append(job)

    return filtered_jobs