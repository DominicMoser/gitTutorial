from datetime import datetime

def log(message:str):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print( ( ( "|" + current_time ) + ("| " + message) ) )

log("es geht")