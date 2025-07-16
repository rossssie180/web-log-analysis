# Web Log Analysis Tool

This is a Python project created as part of the Bright Network Internship Experience UK (IEUK) in Engineering. The script analyses large-scale web server logs to identify the most visited pages and flag potentially suspicious IP addresses based on request volume.

## Project Files

- `log_parser.py` — Main Python script for parsing the log file and generating analytics.
- `sample-log.log` — Sample log file used for analysis (trimmed version if full file is too large).
- `suspicious_ips.txt` — Output file listing IPs with over 1000 requests.

## How to Run

1. **Install Python 3**.
2. Clone the repository or download the files.
3. Place your log file in the same directory.
4. Open a terminal in the project folder and run:

## Possible Future Improvements
- Make threshold for suspicious IPs configurable.
- Add CLI arguments for input/output files
- Integrte visual charts

## Learned Skills
- Explore regular expressions
- Log parsing
- Traffic pattern analysis
- Anomaly detection using Python
- Large real-world dataset

```bash
python log_parser.py

