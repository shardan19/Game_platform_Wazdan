import time
import threading
from collections import deque


class MainState():
    def __init__(self):
        self.maintanance = 0
        self.requests_counter=0 
        self.requests_history=deque(maxlen=10)

        self.refresh_thread = threading.Thread(target=self.update_history_loop)
        self.refresh_thread.daemon = True
        self.refresh_thread.start()

    def increment_requests(self):
        self.requests_counter += 1
    def update_requests_history(self):
        self.requests_history.append(self.requests_counter)
        self.requests_counter =0    
    def get_requests_counter(self):
        return self.requests_counter
    def get_requests_counter_list(self):
        return list(self.requests_history)
    

    def change_maintanance_mode(self,mode):
        if mode in (0, 1):
            self.maintanance = mode

    def get_maintanance(self):
        return self.maintanance
    
    def update_history_loop(self):
        while True:
            self.update_requests_history()
            time.sleep(60)
    
    