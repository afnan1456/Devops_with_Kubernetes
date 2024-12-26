import uuid
import time
from datetime import datetime

def main():
    random_string = str(uuid.uuid4())
    
    while True:
        current_time = datetime.utcnow().isoformat() + "Z"
        print(f"{current_time}: {random_string}")
        time.sleep(5)

if __name__ == "__main__":
    main()
