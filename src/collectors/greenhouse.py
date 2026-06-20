import requests


def get_jobs():
    companies = [
        "hudl",
        "mongodb",
        "elastic",
        "grammarly",
        "datadog"
    ]

    jobs = []

    for company in companies:
        url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

        try:
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                print(f"Skipping {company} - Status {response.status_code}")
                continue

            data = response.json()

            if "jobs" not in data:
                print(f"No jobs found for {company}")
                continue

            for job in data["jobs"]:
                jobs.append({
                    "company": job.get("company_name", company),
                    "title": job.get("title", ""),
                    "location": job.get("location", {}).get("name", ""),
                    "url": job.get("absolute_url", ""),
                    "posted_date": job.get("first_published", "")
                })

            print(f"Collected {len(data['jobs'])} jobs from {company}")

        except Exception as e:
            print(f"Error with {company}: {e}")

    return jobs
