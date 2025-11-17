import time
def animate_line(text, delay=0.08):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()
lyrics = [
        
        ("Él llegó conmigo y conmigo se va",0.6)
        ("Sus ojos son mío', eso no va a cambiar",0.10)
        ("Me quiere a mí y no importan las demás",0.6)
        ("No, no, no, no, no, no, no, no, no",0.8)
        ("Él llegó conmigo y conmigo se va",0.6)
        ("Sus ojos son mío', eso no va a cambiar",0.10)
        ("Me quiere a mí y no importan las demás",0.6)
        ("No, no, no, no, no, no, no, no, no",0.8)
]
start_line = time.time()
for line, lyric_time in lyrics:
    while time.time() - start_line < lyric_time:
        time.sleep(0.3)
    animate_line(line, delay=0.09)