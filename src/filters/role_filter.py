from config import ROLES


def filter_roles(jobs):
    exclude_keywords = [
        "manager",
        "lead",
        "director",
        "head",
        "vp",
        "vice president"
    ]

    filtered_jobs = []

    for job in jobs:
        title = job["title"].lower()

        if any(word in title for word in exclude_keywords):
            continue

        if any(role in title for role in ROLES):
            filtered_jobs.append(job)

    return filtered_jobs