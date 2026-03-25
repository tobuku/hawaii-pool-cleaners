import os, re

count_files = 0
BASE = '/hawaii-pool-cleaners/'

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if not fname.endswith('.html'):
            continue
        path = os.path.join(root, fname)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        # Add /hawaii-pool-cleaners/ prefix to root-relative href/src/action that don't already have it
        new_content = re.sub(
            r'(href|src|action)="/((?!hawaii-pool-cleaners)(?!http)(?!//)[^"]*)',
            r'\1="/hawaii-pool-cleaners/\2',
            content
        )
        if new_content != content:
            count_files += 1
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)

print(f'Restored /hawaii-pool-cleaners/ prefix in {count_files} HTML files')
