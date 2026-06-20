from datetime import datetime, timezone
from config import POSTED_HOURS


def filter_by_date(jobs):
    filtered_jobs = []

    for job in jobs:
        posted_date = job.get("posted_date")

        if not posted_date:
            continue

        try:
            posted_datetime = datetime.fromisoformat(
                posted_date.replace("Z", "+00:00")
            )

            hours_old = (
                datetime.now(timezone.utc) - posted_datetime.astimezone(timezone.utc)
            ).total_seconds() / 3600

            if hours_old <= POSTED_HOURS:
                filtered_jobs.append(job)

        except Exception:
            continue

    return filtered_jobs