#!/usr/bin/env python3
"""Offline checksum, JSON, locale completeness and local Markdown link checks."""
from pathlib import Path
import hashlib,json,re,sys
root=Path(__file__).resolve().parents[1]
manifest=root/'manifest.json'
errors=[]
if not manifest.exists():
 print('manifest.json missing; run against the assembled standalone package')
 raise SystemExit(2)
m=json.loads(manifest.read_text())
for row in m['files']:
 p=root/row['path']
 if not p.is_file():errors.append('missing: '+row['path']);continue
 b=p.read_bytes()
 if hashlib.sha256(b).hexdigest()!=row['sha256'] or len(b)!=row['bytes']:errors.append('hash/size: '+row['path'])
actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p.name!='manifest.json' and '__pycache__' not in p.parts}
expected={x['path'] for x in m['files']}
if actual!=expected:errors.append('manifest membership mismatch')
for p in root.rglob('*.json'):
 try:json.loads(p.read_text())
 except Exception:errors.append('invalid JSON: '+str(p.relative_to(root)))
status=json.loads((root/'locale-status.v1.json').read_text())
source=root/status['source_path'];sha=hashlib.sha256(source.read_bytes()).hexdigest()
for loc,d in status['locales'].items():
 p=root/d['guide_path'];text=p.read_text()
 if re.findall(r'<!-- suti:section:(.*?) -->',text)!=status['required_section_ids']:errors.append('section mismatch: '+loc)
 review=json.loads((root/d['review_path']).read_text())
 if review['source_sha256']!=sha:errors.append('source mismatch: '+loc)
for p in root.rglob('*.md'):
 for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',p.read_text()):
  if re.match(r'^[a-z][a-z0-9+.-]*:',target,re.I) or target.startswith('#'):continue
  dest=(p.parent/target.strip('<>').split('#')[0].split('?')[0]).resolve()
  if not dest.is_relative_to(root.resolve()) or not dest.exists():errors.append('broken/outside link '+str(p.relative_to(root))+': '+target)
print(json.dumps({'scope':'offline package structure, hashes, JSON, section inventory, source fingerprints and links','status':'PASS' if not errors else 'FAIL','file_count':len(m['files']),'locales':len(status['locales']),'errors':errors},ensure_ascii=False))
raise SystemExit(1 if errors else 0)
