from threading import Thread
import time

start = time.time()
print('*****************************')
def get_movie_ticket():
    time.sleep(7)
    print('Got movie ticket')
    
def like_ig_post():
    time.sleep(5)
    print('liked ig post')
    
def main():
    task1 = Thread( target=get_movie_ticket )
    task2 = Thread( target=like_ig_post )
    task1.start()
    task2.start() 
    task1.join()
    task2.join()

main()

end = time.time()
print(end-start, '******************************')
