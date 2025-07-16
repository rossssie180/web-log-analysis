import re
from collections import Counter 

#open the log file
with open("sample-log.log", "r") as f:
    lines = f.readlines()

#define a regex pattern to extract info from each line
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s-\s(?P<country>\w+)\s-\s\[(?P<timestamp>.*?)\]\s"(?P<method>\w+)\s(?P<url>/.*?)\sHTTP/\d.\d"\s(?P<status>\d{3})\s(?P<size>\d+)\s"-"\s"(?P<user_agent>.*?)"\s(?P<response_time>\d+)'
)

#prepare a list to store parsed data
log_entries = []

#loop through lines and parse them
for line in lines:
    match = log_pattern.match(line)
    if match:
        data = match.groupdict()
        log_entries.append(data)

#print the first few parsed lines to check if the code is working
for entry in log_entries[:5]:
    print(entry)

#count most visited URLs
url_counter = Counter(entry["url"] for entry in log_entries)
print("\n Top 5 most visited pages:")
for url, count in url_counter.most_common(30):
    print(f"{url}: {count} visits")

#count most active IPs
ip_counter = Counter(entry["ip"] for entry in log_entries)
print("\n Top 5 IPs by request count:")
for ip, count in ip_counter.most_common(30):
    print(f"{ip}: {count} requests")

with open("suspicious_ips.txt", "w") as out:
    out.write("Suspicious IPs (high request count):\n\n")
    for ip, count in ip_counter.items():
        if count > 1000:
            out.write(f"{ip}: {count} requests\n")
