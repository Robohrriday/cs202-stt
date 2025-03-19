# import sys
# import subprocess
# from git import Repo

# def run_bandit_on_commits(repo_path, branch_name, num_commits):
#     # Initialize the Git repository
#     repo = Repo(repo_path)
    
#     # Check out the main branch
#     repo.git.checkout(branch_name)
    
#     # Get the last 100 non-merge commits
#     commits = list(repo.iter_commits(branch_name, max_count=num_commits))
#     non_merge_commits = [commit for commit in commits if not commit.parents or len(commit.parents) == 1]
    
#     # Ensure we have at least 100 non-merge commits
#     if len(non_merge_commits) < num_commits:
#         print(f"Found only {len(non_merge_commits)} non-merge commits.")
#         non_merge_commits = non_merge_commits[:num_commits]
#     else:
#         non_merge_commits = non_merge_commits[:num_commits]
    
#     # Run Bandit on each commit
#     for i, commit in enumerate(non_merge_commits):
#         # Checkout the commit
#         repo.git.checkout(commit.hexsha)
        
#         # Run Bandit and capture output
#         try:
#             output = subprocess.check_output(['bandit', '-r', f'{sys.argv[1]}', '>', f'../cs202-stt/reports/{sys.argv[1]}/{i}.txt'], stderr=subprocess.STDOUT).decode('utf-8')
#             print(f"Commit: {commit.hexsha}\n{output}\n")
#         except subprocess.CalledProcessError as e:
#             print(f"Error running Bandit on commit {commit.hexsha}: {e.output.decode('utf-8')}")
    
#     # Return to the main branch
#     repo.git.checkout(branch_name)

# # Run the script
# if __name__ == "__main__":
#     # Check that the script is run with the correct number of arguments
#     if len(sys.argv) != 3:
#         print("Usage: python script.py <repo_name> <branch_name>")
#         sys.exit(1)
#     repo_path = f'./{sys.argv[1]}'  # Assuming script is run from the repo root
#     branch_name = sys.argv[2] # main for open-interpreter, master for others
#     num_commits = 5
#     run_bandit_on_commits(repo_path, branch_name, num_commits)

import os
import sys
import subprocess
from git import Repo

def run_bandit_on_commits(repo_path, branch_name, num_commits):
    # Initialize the Git repository
    repo = Repo(repo_path)
    
    # Check out the main branch
    repo.git.checkout(branch_name)
    
    # Get the last 100 non-merge commits
    commits = list(repo.iter_commits(branch_name, max_count=num_commits))
    non_merge_commits = [commit for commit in commits if not commit.parents or len(commit.parents) == 1]
    
    # Ensure we have at least 100 non-merge commits
    if len(non_merge_commits) < num_commits:
        print(f"Found only {len(non_merge_commits)} non-merge commits.")
        non_merge_commits = non_merge_commits[:num_commits]
    else:
        non_merge_commits = non_merge_commits[:num_commits]
    
    # Create the report directory if it doesn't exist
    report_dir = f'../cs202-stt/reports/{sys.argv[1]}'
    os.makedirs(report_dir, exist_ok=True)

    # Run Bandit on each commit
    for i, commit in enumerate(non_merge_commits):
        # Checkout the commit
        repo.git.checkout(commit.hexsha)
        
        # Run Bandit and write output to a file
        report_file = f'{report_dir}/{i}.txt'
        try:
            with open(report_file, 'w') as f:
                subprocess.run(['bandit', '-r', f'{repo_path}'], stdout=f, stderr=f)
            print(f"Commit: {commit.hexsha} - Report saved to {report_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error running Bandit on commit {commit.hexsha}: {e}")
    
    # Return to the main branch
    repo.git.checkout(branch_name)

# Run the script
if __name__ == "__main__":
    # Check that the script is run with the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python script.py <repo_name> <branch_name> <num_commits>")
        sys.exit(1)
    repo_path = f'./{sys.argv[1]}'  # Assuming script is run from the repo root
    branch_name = sys.argv[2] # main for markitdown, ha_xiaomi_home, latexify_py
    num_commits = int(sys.argv[3]) # 133 for markitdown, 112 for ha_xiaomi_home, 100 for latexify_py
    run_bandit_on_commits(repo_path, branch_name, num_commits)
