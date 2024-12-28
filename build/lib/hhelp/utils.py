# hhelp/utils.py
import os
import nbformat
from nbconvert import PythonExporter, MarkdownExporter

def convert_file(file_path):
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    if ext == '.ipynb':
        py_path = file_path.replace('.ipynb', '.py')
        md_path = file_path.replace('.ipynb', '.md')
        with open(file_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        py_exporter = PythonExporter()
        script, _ = py_exporter.from_notebook_node(nb)
        with open(py_path, 'w', encoding='utf-8') as f:
            f.write(script)
        md_exporter = MarkdownExporter()
        text, _ = md_exporter.from_notebook_node(nb)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(text)
        return py_path, 'text/plain'
    elif ext == '.md':
        return file_path, 'text/markdown'
    elif ext == '.pdf':
        return file_path, 'application/pdf'
    else:
        return file_path, 'text/plain'
