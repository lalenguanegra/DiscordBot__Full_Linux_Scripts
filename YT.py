from subprocess import call
call(['youtube-dl','-x', '--audio-format', 'mp3', '-o 1.%(ext)s', '-a', 'URL.txt'], shell=False)
open('URL.txt', 'w').close()
