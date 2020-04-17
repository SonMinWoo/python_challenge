# Extracting from page
from day5_indeed import extract_indeed_pages, extract_indeed_jobs


## request many pages
last_indeed_pages = extract_indeed_pages()

extract_indeed_jobs(last_indeed_pages)
