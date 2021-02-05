import csv


def save_to_file(jobs):
  file = open("job_info.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["TITLE","COMPANY","LOCATION","Link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  print(jobs)
  return