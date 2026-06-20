def filter_seniority(jobs):
    exclude_keywords = [
        "staff",
        "principal",
        "architect",
        "director",
        "manager",
        "distinguished"
    ]

    filtered_jobs = []

    for job in jobs:
        title = job["title"].lower()

        if any(word in title for word in exclude_keywords):
            continue

        filtered_jobs.append(job)

    return filtered_jobs