import xbmc,os
caminho=os.popen("(mount | grep -i '/dev/sda1' | cut -d ' ' -f 3)").read().replace('/var','').strip()
xbmc.executebuiltin('xbmc.PlayMedia("{0}","isdir")'.format(caminho))
xbmc.executebuiltin('xbmc.PlayerControl(RepeatAll)')
