import sys
import csv
from tqdm import tqdm
from pydriller import Repository

def get_old_complexity(commits, m):
  for x in reversed(commits):
    for y in x.modified_files:
      if y.new_path == m.old_path:
        return y.complexity
  return None

columns = ['old_file_path','new_file_path','commit_SHA', 'parent_commit_SHA', 'commit_message', 'diff_hist', 'old_file_mcc', 'new_file_mcc']

rows = []
count=0
last_n=500

commits = []
for x in Repository(sys.argv[1],only_no_merge=True,order='reverse', skip_whitespaces = True, histogram_diff = True).traverse_commits():
  if (x.in_main_branch==True):
    count=count+1
    commits.append(x)
    if count == last_n:
      break

in_order = []
for value in range(len(commits)):
  in_order.append(commits.pop())

commits=in_order
i=-1
row = []

for commit in tqdm(commits, desc='Mining commits', colour='green', unit='commit'):
  i+=1
  for m in commit.modified_files:
    old_complexity = get_old_complexity(commits[:i], m)
    row.append([m.old_path,m.new_path,commit.hash,commit.parents[0],commit.msg,m.diff_parsed,old_complexity,m.complexity])
print("Number of modifications: ", len(row))
with open(sys.argv[1]+f"_results/commits_info.csv", 'w') as csvFile:
  writer = csv.writer(csvFile)
  writer.writerow(columns)
  writer.writerows(row)
csvFile.close()
