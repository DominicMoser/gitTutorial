from datetime import datetime

def log(message:str):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print( ( ( "|" + current_time ) + ("| " + message) ) )
    with open("test.log", "a") as f:
        f.write(( ( "|" + current_time ) + ("| " + message) + "\n" ))

if __name__ == "__main__":
    log("Script Running")