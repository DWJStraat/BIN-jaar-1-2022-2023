import os
import glob
import re


folder = r"C:\Users\dstra\Downloads\HIV2"

envs = []
vifs = []
count = 0
list = glob.glob(f"{folder}/*/*.*")

env_files = []
vif_files = []

def content_handler(content, name):
    content[0] = f'>{name}\n'
    content = ''.join(content)
    return content

def env(content, envs, env_files, name):
    name = re.sub(r'env', '', name, flags=re.IGNORECASE)
    name = re.sub(r'protein', '', name, flags=re.IGNORECASE)
    for token in ['_','-', '_', '[', ']']:
        name = name.lstrip(token).rstrip(token)
    env_files.append(i)
    content = content_handler(content, name)
    envs.append(content)

def vif(content, vifs, vif_files, name):
    print(f'before: {name}')
    name = re.sub(r'vif', '', name, flags=re.IGNORECASE)
    name = re.sub(r'protein', '', name, flags=re.IGNORECASE)
    for token in ['_','-', '_', '[', ']']:
        name = name.lstrip(token).rstrip(token)
    print(f'after: {name}')
    vif_files.append(i)
    content = content_handler(content, name)
    vifs.append(content)


for i in list:
    count += 1
    with open(i) as file:

        content = file.readlines()
        name = os.path.basename(i)
        name = name.split('.')[0]
        name = name.replace(' ', '_')
        if re.search(r'env', content[0], re.IGNORECASE):
            env(content, envs, env_files, name)
        elif re.search(r'vif', content[0], re.IGNORECASE):
            vif(content, vifs, vif_files, name)



env = '\n\n'.join(envs)
vif = '\n\n'.join(vifs)

with open(f'{folder}/env.fasta', 'w+') as fasta:
    fasta.write(env)

with open(f'{folder}/vif.fasta', 'w+') as fasta:
    fasta.write(vif)

for i in list:
    if i in env_files or i in vif_files:
        list.remove(i)
