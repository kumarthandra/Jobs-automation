from src.collectors.greenhouse import get_jobs
from src.filters.location_filter import filter_locations
from src.filters.role_filter import filter_roles
from src.filters.seniority_filter import filter_seniority
from src.exporters.csv_exporter import export_to_csv

jobs = get_jobs()

# Apply filters
location_filtered_jobs = filter_locations(jobs)

role_filtered_jobs = filter_roles(location_filtered_jobs)

seniority_filtered_jobs = filter_seniority(role_filtered_jobs)

# Final jobs
final_jobs = seniority_filtered_jobs

print(f"\nTotal Jobs: {len(jobs)}")
print(f"Location Matched Jobs: {len(location_filtered_jobs)}")
print(f"Role Matched Jobs: {len(role_filtered_jobs)}")
print(f"Seniority Matched Jobs: {len(seniority_filtered_jobs)}")

print("\nFinal Jobs:\n")

for job in final_jobs:
    print("-" * 60)
    print(f"Company : {job['company']}")
    print(f"Title    : {job['title']}")
    print(f"Location : {job['location']}")
    print(f"Posted   : {job['posted_date']}")
    print(f"URL      : {job['url']}")

# Export to CSV
export_to_csv(final_jobs)

print("\nCSV file created successfully!")
print("Location: output/jobs.csv")