import time
import os

def main():
    
    var_one = os.environ.get('var_one', None)
    
    try:
        print("start")
        print(var_one)
        print("succeeded")
        main()
        
    except:
        print("error")
        time.sleep(5)
        print("restarting")
        main()


main()
