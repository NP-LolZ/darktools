# coding=utf-8

import os

'''
Update v1.2
By NP.ID
'''

# Hapus cache
try:
    os.remove('.sampah')
except:
    pass

# Cek update
print("\x1b[0m[\x1b[92m*\x1b[0m]\x1b[93m Tunggu")
os.system('git pull --quiet ; clear')

print("""
\x1b[91m╔╦╗╔═╗╦═╗╦╔═\x1b[0m┌┬┐┌─┐┌─┐┬  ┌─┐
\x1b[91m ║║╠═╣╠╦╝╠╩╗\x1b[0m │ │ ││ ││  └─┐
\x1b[91m═╩╝╩ ╩╩╚═╩ ╩\x1b[0m ┴ └─┘└─┘┴─┘└─┘
\x1b[0m[\x1b[92m*\x1b[0m]\x1b[93m Tools akan update ke versi 1.2
\x1b[0m[\x1b[92m*\x1b[0m]\x1b[93m Untuk informasi pergantian tools, silahkan enter\x1b[0m""")
raw_input()
os.system("am start https://github.com/NP-LolZ/darktools/blob/master/README.md > .sampah")
