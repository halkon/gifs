import pathlib
import requests
source = pathlib.Path('cartoon-gifs-to-save')
print("Source: {}".format(source))
gifs = {}
with source.open() as f: f.readline()
	print("f")
with source.open() as f: f.readline()
print("f")
with source.open() as f: f.readline()
  print("f")
with source.open() as f: f.readline()
with source.open() as f: 
	line = f.readline()
	if line == '':
with source.open() as f: 
	content = f.read()
print("Content: {}".format(content))
for f in content: 
	if f.trim() == "":
		print("blank")
strip('  fdsasfd')
' fdfdsaf'.strip()
for f in content:
content
content.split('\n')
for c in content.split('\n'):
	if c.strip() == '':
		continue
	if c[0] == ';':
		gifs[c[1:].strip] = []
		continue
gifs
for c in content.split('\n'):
	if c.strip() == '':
		continue
	if c[0] == ';':
		folder_name = c[1:].strip()
		gifs[folder_name] = []
		continue
	gifs[folder_name] = c.strip()
gifs
for c in content.split('\n'):
     if c.strip() == '':
             continue
     if c[0] == ';':
             folder_name = c[1:].strip()
             gifs[folder_name] = []
             continue
     gifs[folder_name].append(c.strip())
gifs
gifs = {}
for c in content.split('\n'):
     if c.strip() == '':
             continue
     if c[0] == ';':
             folder_name = c[1:].strip()
             gifs[folder_name] = []
             continue
     gifs[folder_name].append(c.strip())
gifs
for f in gifs:
for f, gif_list in gifs:
	print("f: {}".format(f))
for gif_list in gifs:
	print("gif_list: {}".format(gif_list))
for f in gifs:
	folder_path = pathlib.Path(f)
	folder_path.mkdir(exist_ok=True)
	for g in gifs[f]:
		folder_path.joinpath(pathlib.Path(g.replace('/', '_').replace(':', '_').replace('?', '_')).with_suffix('.gif').write_bytes(requests.get(g).content)
for f in gifs:
    folder_path = pathlib.Path(f)
    folder_path.mkdir(exist_ok=True)
    for g in gifs[f]:
            safe_name = pathlib.Path(g.replace('/', '_').replace(':', '_').replace('?', '_'))
            folder_path.joinpath(safe_name).with_suffix('.gif').write_bytes(requests.get(g).content)
for f in gifs:
    folder_path = pathlib.Path(f)
    folder_path.mkdir(exist_ok=True)
    for g in gifs[f]:
            safe_name = pathlib.Path(g.replace('/', '_').replace(':', '_').replace('?', '_'))
            try:
                c = requests.get(g).content
                folder_path.joinpath(safe_name).with_suffix('.gif').write_bytes(c)
            except:
                continue
for f in gifs:
    folder_path = pathlib.Path(f)
    folder_path.mkdir(exist_ok=True)
    error_path = folder_path.joinpath('error')
    for g in gifs[f]:
            safe_name = pathlib.Path(g.replace('/', '_').replace(':', '_').replace('?', '_'))
            try:
                c = requests.get(g).content
                folder_path.joinpath(safe_name).with_suffix('.gif').write_bytes(c)
            except:
                error_path.write_text("{}\n".format(g))
                continue
for f in gifs:
    folder_path = pathlib.Path(f)
    folder_path.mkdir(exist_ok=True)
    error_path = folder_path.joinpath('error')
    success_path = folder_path.joinpath('success')
    for g in gifs[f]:
            safe_name = pathlib.Path(g.replace('/', '_').replace(':', '_').replace('?', '_'))
            try:
                c = requests.get(g).content
                bytes_written = folder_path.joinpath(safe_name).with_suffix('.gif').write_bytes(c)
                success_path.write_text("{} - {}\n".format(bytes_written, g))
            except:
                error_path.write_text("{}\n".format(g))
                continue
for f in gifs:
    folder_path = pathlib.Path(f)
    folder_path.mkdir(exist_ok=True)
    error_path = folder_path.joinpath('error')
    success_path = folder_path.joinpath('success')
    error = []
    success = []
    for g in gifs[f]:
            safe_name = pathlib.Path(g.replace('/', '_').replace(':', '_').replace('?', '_'))
            try:
                c = requests.get(g).content
                bytes_written = folder_path.joinpath(safe_name).with_suffix('.gif').write_bytes(c)
                success.append("{} - {}\n".format(bytes_written, g)
            except:
                error.append("{}\n".format(g))
                continue
    
    success_path.write_text(success.join('\n'))
    error_path.write_text(error.join('\n'))
for f in gifs:
    folder_path = pathlib.Path(f)
    folder_path.mkdir(exist_ok=True)
    error_path = folder_path.joinpath('error')
    success_path = folder_path.joinpath('success')
    error = []
    success = []
    for g in gifs[f]:
            safe_name = pathlib.Path(g.replace('/', '_').replace(':', '_').replace('?', '_'))
            try:
                c = requests.get(g).content
                bytes_written = folder_path.joinpath(safe_name).with_suffix('.gif').write_bytes(c)
                success.append("{} - {}\n".format(bytes_written, g)
            except:
                error.append("{}\n".format(g))
                continue
    success_path.write_text(success.join('\n'))
    error_path.write_text(error.join('\n'))
for f in gifs:
    folder_path = pathlib.Path(f)
    folder_path.mkdir(exist_ok=True)
    error_path = folder_path.joinpath('error')
    success_path = folder_path.joinpath('success')
    error = []
    success = []
    for g in gifs[f]:
            safe_name = pathlib.Path(g.replace('/', '_').replace(':', '_').replace('?', '_'))
            try:
                c = requests.get(g).content
                bytes_written = folder_path.joinpath(safe_name).with_suffix('.gif').write_bytes(c)
                success.append("{} - {}\n".format(bytes_written, g))
            except:
                error.append("{}\n".format(g))
                continue
    success_path.write_text(success.join('\n'))
    error_path.write_text(error.join('\n'))
for f in gifs:
    folder_path = pathlib.Path(f)
    folder_path.mkdir(exist_ok=True)
    error_path = folder_path.joinpath('error')
    success_path = folder_path.joinpath('success')
    error = []
    success = []
    for g in gifs[f]:
            safe_name = pathlib.Path(g.replace('/', '_').replace(':', '_').replace('?', '_'))
            try:
                c = requests.get(g).content
                bytes_written = folder_path.joinpath(safe_name).with_suffix('.gif').write_bytes(c)
                success.append("{} - {}\n".format(bytes_written, g))
            except:
                error.append("{}\n".format(g))
                continue
    success_path.write_text('\n'.join(success))
    error_path.write_text('\n'.join(error))