'''
If UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: 
invalid start byte is displayed changed the encoding of the file in VSCode
look in the status bar click in the current encoding and then select 
"Save with Encoding" 
'''

import markdown
import os
from markdown.extensions.toc import TocExtension
from bs4 import BeautifulSoup

import os
import shutil

def copy_folder_contents(src_folder, dst_folder):
    """
    Copies all contents from src_folder to dst_folder recursively.
    Creates destination folder if it doesn't exist.
    Overwrites existing files in destination.
    
    Args:
        src_folder (str): Source folder path
        dst_folder (str): Destination folder path
    """
    try:
        # Create destination folder if it doesn't exist
        os.makedirs(dst_folder, exist_ok=True)
        
        # Walk through all files and subdirectories
        for root, dirs, files in os.walk(src_folder):
            # Create corresponding directories in destination
            for dir_name in dirs:
                src_dir = os.path.join(root, dir_name)
                dst_dir = os.path.join(dst_folder, os.path.relpath(src_dir, src_folder))
                os.makedirs(dst_dir, exist_ok=True)
            
            # Copy all files
            for file_name in files:
                src_file = os.path.join(root, file_name)
                dst_file = os.path.join(dst_folder, os.path.relpath(src_file, src_folder))
                shutil.copy2(src_file, dst_file)  # copy2 preserves metadata
        
        print(f"Successfully copied all contents from '{src_folder}' to '{dst_folder}'")
    
    except Exception as e:
        print(f"Error occurred while copying: {e}")

def parse_frontmatter_from_file(file_path):
    """
    Reads a file with frontmatter content (between --- lines) and parses it into a dictionary.
    
    Args:
        file_path (str): Path to the file containing frontmatter
    
    Returns:
        dict: A dictionary containing the key/value pairs from the frontmatter
    """
    frontmatter = {}
    in_frontmatter = False
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            
            # Check for frontmatter delimiters
            if line == '---':
                if in_frontmatter:
                    break  # End of frontmatter
                in_frontmatter = True
                continue
            
            # Only process lines when we're between the --- delimiters
            if in_frontmatter and line:
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip()
    
    return frontmatter

def remove_meta(md_text: str) -> str:
    # Remove the YAML front matter (meta section) if it exists
    if md_text.startswith("---"):
        md_text = md_text.split("---", 2)[2].strip()  # Splits and removes the first block
    return md_text

def transform_filename(filename: str) -> str:
    preposicoes = {"a", "ao", "as", "da", "de", "do", "das", "dos", "e", "em", "na", "no", "nas", "nos", "para", "por", "o", "os"}
    
    # Extrai os dois primeiros dígitos e formata com " - "
    prefix = filename[:2] + " - " if filename[2] == '-' else ""
    # Remove os dois primeiros dígitos e o hífen
    without_digits = filename[3:] if filename[2] == '-' else filename
    # Remove a extensão do arquivo
    without_extension = without_digits.rsplit('.', 1)[0]
    # Substitui hífens por espaços
    with_spaces = without_extension.replace('-', ' ')
    # Divide o texto em palavras
    words = with_spaces.split()
    # Capitaliza palavras, exceto preposições (mantendo a primeira palavra sempre capitalizada)
    transformed_words = [words[0].capitalize()] + [
        word if word.lower() in preposicoes else word.capitalize() for word in words[1:]
    ]
    # Junta as palavras em uma string
    result = ' '.join(transformed_words)
    return prefix + result

metadata = parse_frontmatter_from_file('00-meta.md')

with open("html/template/header.tpl", encoding='utf8') as f:
    header = f.read()

header = header.replace('%date%', metadata['Date'])
header = header.replace('%category%', metadata['Category'])
header = header.replace('%technologies%', metadata['Technologies'])
header = header.replace('%youtube%', metadata['Video'])
header = header.replace('%github%', metadata['GitHub'])

with open("html/template/footer.tpl", encoding='utf8') as f:
    footer = f.read()

all_toc = ''
for file in os.listdir('.'):
    if file.endswith('.md'):
        with open(f'{file}', 'r', encoding='utf8') as f:
            tempMd= remove_meta(f.read())

        # Convert the input to HTML
        html = markdown.markdown(tempMd, extensions=['meta','fenced_code',TocExtension(baselevel=2, title='Contents')])
        toc = ''
        soup = BeautifulSoup(html, 'html.parser')
        section_title = transform_filename(file)
        toc += '<button class="collapsible">\n'
        toc += '    <a href="#' + file[:-3] + '" onclick="changeContent(\''+ file[:-3] + '.html\')">' + section_title + '</a>\n'
        toc += '</button>\n'
        toc += '<div class="content">\n'
        toc += '    <div>\n'
        for h3 in soup.find_all('h3'):
            section = h3.text.lower().replace(' ','-').replace('---','-').replace('?','').replace('!','').replace(',','').replace('#','')
            toc += f'        <a href="#" onclick="changeContent(\''+ file[:-3] + '.html#' + section + '\')"><li>' + h3.text + '</li></a>\n'
        toc += '    </div>\n'
        toc += '</div>\n'
        all_toc += toc

for file in os.listdir('.'):
    if file.endswith('.md'):
        with open(f'{file}', 'r', encoding='utf8') as f:
            tempMd= remove_meta(f.read())
        html = markdown.markdown(tempMd, extensions=['meta','tables','fenced_code',TocExtension(baselevel=2, title='Contents')])

        with open(f'html/{file[:-3]}.html', 'w', encoding='utf8') as f:
            f.write(header)
            f.write(html.replace('<img src="images/','<img src="../images/').replace('language-python', 'language-python line-numbers'))
            f.write(footer)

source_folder = 'images/'
destination_folder = 'html/images/'
    
copy_folder_contents(source_folder, destination_folder)
