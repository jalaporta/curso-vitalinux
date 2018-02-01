from slugify import slugify
import os
import re
import bs4 as BeautifulSoup

IMAGES = 'img/'

def image_to_

for file in os.listdir("."):
    if file[-3:] = '.md':
        tmp_file = file + '1'
        file_name = file
        with open(file) as infile, open(tmp_file, 'w') as outfile:
            for line in infile:            
            if '[<img' in line:
                imgTag = BeautifulSoup(line)
                img = imgTag.find('img')
                source = slugify(img['src'].split('/')[-1][:-3]) + '.png'
                img['src'] = 'img/' + source
                line = str(imgTag)
                lineString = re.findall(r'(img/\S*)"', line)
                lineStringStringed = lineString[0]
                wholeLine = '![](' + lineStringStringed + ')'
                line = wholeLine
            elif '<img' in line and 'http' in line:
                lineString = re.findall(r'src="(\S*)"', line)
                lineStringStringed = lineString[0]
                wholeLine = '![](' + lineStringStringed + ')'
                line = wholeLine
            else:
                for src, target in replacements.iteritems():
                    line = line.replace(src, target)
            
            if 'youtube.com/embed/' in line:
                youtubeString = re.findall(r'(www\.youtube\.com/embed/\S*)"', line)
                youtubeStringStringed = youtubeString[0]
                youtubeStringFixed = 'https//' + youtubeStringStringed
                youtubeStringFixed = re.sub(r'embed/', 'watch?v=', youtubeStringFixed)
                wholeLine = '{% youtube %}' + youtubeStringFixed + '{% endyoutube %}'
                line = '\n' + wholeLine + '\n'
			
            if line.startswith('Obra publicada con'):
                line = line.replace(line, '')

            if '![' in line:
                line = '\n' + line + '\n'
