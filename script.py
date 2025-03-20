import os
import sys
import subprocess
from git import Repo

def run_bandit_on_commits(repo_path, branch_name, num_commits):
    repo = Repo(repo_path)
    repo.git.checkout(branch_name)
    
    commits = list(repo.iter_commits(branch_name, max_count=num_commits))
    non_merge_commits = [commit for commit in commits if not commit.parents or len(commit.parents) == 1]
    
    if len(non_merge_commits) < num_commits:
        print(f"Found only {len(non_merge_commits)} non-merge commits.")
        non_merge_commits = non_merge_commits[:num_commits]
    else:
        non_merge_commits = non_merge_commits[:num_commits]
    
    report_dir = f'../cs202-stt/reports/{sys.argv[1]}'
    os.makedirs(report_dir, exist_ok=True)

    for i, commit in enumerate(non_merge_commits):
        repo.git.checkout(commit.hexsha)
        
        report_file = f'{report_dir}/{i}.txt'
        try:
            with open(report_file, 'w') as f:
                subprocess.run(['bandit', '-r', f'{repo_path}'], stdout=f, stderr=f)
            print(f"Commit: {commit.hexsha} - Report saved to {report_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error running Bandit on commit {commit.hexsha}: {e}")
    
    repo.git.checkout(branch_name)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <repo_name> <branch_name> <num_commits>")
        sys.exit(1)
    repo_path = f'./{sys.argv[1]}'  # Assuming script is run from folder just outside the repo
    branch_name = sys.argv[2]       # main for markitdown, ha_xiaomi_home, latexify_py
    num_commits = int(sys.argv[3])  # 133 for markitdown, 112 for ha_xiaomi_home, 100 for latexify_py
    run_bandit_on_commits(repo_path, branch_name, num_commits)
