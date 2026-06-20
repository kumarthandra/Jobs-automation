import csv


def export_to_csv(jobs, filename="output/jobs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Company",
            "Title",
            "Location",
            "Posted Date",
            "URL"
        ])

        for job in jobs:
            writer.writerow([
                job.get("company", ""),
                job.get("title", ""),
                job.get("location", ""),
                job.get("posted_date", ""),
                job.get("url", "")
            ])

    print(f"CSV saved: {filename}")