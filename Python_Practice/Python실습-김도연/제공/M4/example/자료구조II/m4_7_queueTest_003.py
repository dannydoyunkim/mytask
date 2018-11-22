class Queue():
    def __init__(self, queue=None):
        if queue is None:           # 큐가 없으면
            self.queue = []         # 큐 생성
            
    def empty(self):                # 큐가 비어있는지 검사하는 함수        
        if(len(self.queue) == 0):   #큐가 비어있으면
            return True             # False 반환
        else:                       # 비어있지 않다면
            return False            # True 반환
        
    def size(self):                 # 큐의 사이즈를 검사하는 함수
        return len(self.queue)      # 큐의 사이즈를 반환
    
    def put(self, element):          # 큐에 값을 넣는 함수
        self.queue.append(element)   # 큐에 값을 추가        
        print("list = " + str(self.queue))
        
    def get(self):                   # 큐에서 값을 빼내는 함수
        self.queue.pop(0)            # 큐에서 첫번째 값을 제거
        print("list = " + str(self.queue))


q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

print(q.empty()) 
print(q.size())

q.get()
q.get()
q.get()
q.get()
q.get()

print(q.empty()) 
