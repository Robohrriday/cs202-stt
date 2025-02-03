import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

hist = pd.read_csv(f"./{sys.argv[1]}_results/commits_info_hist.csv")
myers = pd.read_csv(f"./{sys.argv[1]}_results/commits_info_myers.csv")
final = pd.read_csv(f"./{sys.argv[1]}_results/final_dataset.csv")

# Code Artifacts
code_artifacts = [
    'py', 'mdx', 'json', 'eslintrc', 'nvmrc', 'j2', 'sh', 'css', 'Makefile', 
    'tsx', 'jsonl', 'js', 'jinja', 'ts', 'puml', 'containers/app/Dockerfile'
]

# Non-Code Artifacts
non_code_artifacts = [
    'yml', 'MD', 'gitignore', 'lock', 'svg', 'md', 'toml', 'openhands_instructions'
]

# Stats
# Artifact Types: Code, Non-Code, Mixed, Unhandled
# Code: Code Artifacts
# Non-Code: Non-Code Artifacts
# Mixed: Code/Non-Code and Non-Code/Code Artifacts in old and new file paths
# Unhandled: Any other case

for i in range(len(final)):
    if type(final.loc[i, 'old_file_path']) == str:
        ext1 = final.loc[i, 'old_file_path'].split('.')[-1]
    else:
        ext1 = None
    if type(final.loc[i, 'new_file_path']) == str:
        ext2 = final.loc[i, 'new_file_path'].split('.')[-1]
    else:
        ext2 = None
    
    if ext1 != None and ext1 != None:
        if ext1 in code_artifacts and ext2 in code_artifacts:
            final.loc[i, 'artifact_type'] = 'Code'
        elif ext1 in non_code_artifacts and ext2 in non_code_artifacts:
            final.loc[i, 'artifact_type'] = 'Non-Code'
        else:
            final.loc[i, 'artifact_type'] = 'Mixed'
    elif ext1 == None and ext2 != None:
        if ext2 in code_artifacts:
            final.loc[i, 'artifact_type'] = 'Code'
        elif ext2 in non_code_artifacts:
            final.loc[i, 'artifact_type'] = 'Non-Code'
        else:
            final.loc[i, 'artifact_type'] = 'Unhandled'
    elif ext1 != None and ext2 == None:
        if ext1 in code_artifacts:
            final.loc[i, 'artifact_type'] = 'Code'
        elif ext1 in non_code_artifacts:
            final.loc[i, 'artifact_type'] = 'Non-Code'
        else:
            final.loc[i, 'artifact_type'] = 'Unhandled'
    else:
        final.loc[i, 'artifact_type'] = 'Unhandled'

# Matches for non-code artifacts
final_non_code_matches = final[(final['artifact_type'] == 'Non-Code') & (final['Matches'] == 'Yes')]

# No matches for non-code artifacts
final_non_code_no_matches = final[(final['artifact_type'] == 'Non-Code') & (final['Matches'] == 'No')]

# Matches for code artifacts
final_code_matches = final[(final['artifact_type'] == 'Code') & (final['Matches'] == 'Yes')]

# No matches for code artifacts
final_code_no_matches = final[(final['artifact_type'] == 'Code') & (final['Matches'] == 'No')]

# Plotting
plt.figure(figsize=(10, 10))
plt.bar(['Non-Code\nMatches', 'Non-Code\nNo Matches', 'Code\nMatches', 'Code\nNo Matches'],
        [len(final_non_code_matches), len(final_non_code_no_matches), len(final_code_matches), len(final_code_no_matches)])
plt.xlabel('Artifact Type')
plt.ylabel('Count')
plt.title('Matches and No Matches for Code and Non-Code Artifacts')
plt.savefig(f"./{sys.argv[1]}_results/artifacts_and_matches.png")
plt.close()