# Extracting from page
from day5_6_indeed import get_jobs as get_indeed_jobs
from day6_stackoverflow import get_jobs as get_so_jobs
from day8 import save_to_file


indeed_jobs = get_indeed_jobs()
#so_jobs = get_so_jobs()
jobs = indeed_jobs
save_to_file(jobs)
