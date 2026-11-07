#!/usr/bin/env python3
"""Optional offline entity replacement. Python 3 standard library only."""
import argparse, json, re, shutil
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--map',default='entity-map.json')
p.add_argument('--output',default='personalized')
a=p.parse_args()
root=Path(__file__).resolve().parent
mapping=json.loads((root/a.map).read_text())
pattern=re.compile(r'\b[a-z_]+\.replace_me_[a-z0-9_]+\b')
for old,new in mapping.items():
 if not pattern.fullmatch(old):p.error('Invalid placeholder: '+old)
 if new and (not re.fullmatch(r'[a-z_]+\.[a-z0-9_]+',new) or '.replace_me_' in new or old.split('.')[0]!=new.split('.')[0]):
  p.error('Use an actual entity ID of the same domain for '+old)
dest=Path(a.output).resolve()
if dest.exists():p.error('Output already exists; choose a new folder with --output.')
files=list(root.glob('dashboards/*.yaml'))+list(root.glob('examples/*.yaml'))
rendered={f:pattern.sub(lambda m:mapping.get(m[0]) or m[0],f.read_text()) for f in files}
remaining=sorted(set(pattern.findall('\n'.join(rendered.values()))))
dest.mkdir(parents=True)
for f,content in rendered.items():
 target=dest/f.relative_to(root);target.parent.mkdir(exist_ok=True,parents=True);target.write_text(content)
shutil.copytree(root/'themes',dest/'themes')
shutil.copy2(root/'configuration-snippet.yaml',dest)
(dest/'UNRESOLVED.txt').write_text('\n'.join(remaining)+'\n')
print('Created:',dest)
print('Unmapped placeholders:',len(remaining),'- see UNRESOLVED.txt. Map them or remove their cards before installing.')
