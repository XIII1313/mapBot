import time

def main():
    
    try:
        print("start")
        print(var_one)
        
    except:
        print("error")
        time.sleep(5)
        print("restarting")
        main()


main()
