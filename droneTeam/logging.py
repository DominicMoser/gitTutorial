from datetime import datetime

def log(message:str):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print( ( ( "|" + current_time ) + ("| " + message) ) )

if __name__ == "__main__":
    log("Script Running")