from os import popen, system
from time import sleep
from Frames import Frame

def ping(addr = '8.8.8.8', decs=0) -> float:
    """Performs a ping."""

    res = popen(f'ping {addr} -c 1 -w 2').read()
    
    try: res = round(float(res.split('v = ')[1].split('/')[0]), decs)
    except: res = '-'
    
    return res


def main() -> None:
    try:
        _ping = ping()
        
        color = '\033[91m'
        
        if not _ping == '-':
            
            if _ping < 30: color = '\033[92m'
            elif _ping < 130: color = '\033[93m'
            else: color = '\033[91m'
            
            _ping = str(int(_ping))
        
        frame = Frame(' ')
        frame.border(['─', '│'], ['┌', '┐', '└', '┘'], 4, [7, 0])
        frame.text(0, 0, _ping, True, color)
        frame.text(0, -2, '> PING <', True)
        frame.text(4, 0, 'ms', True, '\033[87m')
        frame.make()
        
        sleep(0.3)
    
    except KeyboardInterrupt:
        system('clear')
        exit()
    
    main()

main()