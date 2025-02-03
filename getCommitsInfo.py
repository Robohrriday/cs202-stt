import sys
import csv
from pydriller import Repository

columns = ['old_file_path','new_file_path','commit_SHA', 'parent_commit_SHA', 'commit_message', 'diff']

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
hist_row = []
for commit in commits:
  i+=1
  print('[{}/{}] Mining commit {}.{}'.format(i+1,len(commits),sys.argv[1],commit.hash))
  for m in commit.modified_files:
    hist_row.append([m.old_path,m.new_path,commit.hash,commit.parents[0],commit.msg,m.diff_parsed])

with open(sys.argv[1]+f"_results/commits_info_hist.csv", 'w') as csvFile:
  writer = csv.writer(csvFile)
  writer.writerow(columns)
  writer.writerows(hist_row)
csvFile.close()

count=0
last_n=500

commits = []
for x in Repository(sys.argv[1],only_no_merge=True,order='reverse', skip_whitespaces = True, histogram_diff = False).traverse_commits():
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
myers_row = []
for commit in commits:
  i+=1
  print('[{}/{}] Mining commit {}.{}'.format(i+1,len(commits),sys.argv[1],commit.hash))
  for m in commit.modified_files:
    myers_row.append([m.old_path,m.new_path,commit.hash,commit.parents[0],commit.msg,m.diff_parsed])


with open(sys.argv[1]+f"_results/commits_info_myers.csv", 'w') as csvFile:
  writer = csv.writer(csvFile)
  writer.writerow(columns)
  writer.writerows(myers_row)
csvFile.close()

columns = ['old_file_path','new_file_path','commit_SHA', 'parent_commit_SHA', 'commit_message', 'diff_hist', 'diff_myers', 'Matches']

for i in range(len(hist_row)):
  hist_row[i].append(myers_row[i][-1])
  if hist_row[i][-2] == myers_row[i][-1]:
    hist_row[i].append("Yes")
  else:
    hist_row[i].append("No")

with open(sys.argv[1]+f"_results/final_dataset.csv", 'w') as csvFile:
  writer = csv.writer(csvFile)
  writer.writerow(columns)
  writer.writerows(hist_row)
csvFile.close()