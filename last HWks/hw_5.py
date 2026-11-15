import csv

with open("scores.csv", encoding="utf-8", newline="") as f_in, open("top_students.csv", "w", encoding="utf-8", newline="") as f_out:
    reader = csv.DictReader(f_in)
    writer = csv.DictWriter(f_out, fieldnames=reader.fieldnames)
    writer.writeheader()
    
    # фильтруем прям на лету
    writer.writerows(row for row in reader if int(row["score"]) > 80)
