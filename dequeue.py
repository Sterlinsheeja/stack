from pythonds.basic import Queue
def hotline(namelist,num):
    siQueue=Queue()
    for name in namelist:
        siQueue.enqueue(name)
        while siQueue.size()>1:
            for i in range(num):
                siQueue.enqueue(siQueue.dequeue())
            siQueue.dequeue()
        return siQueue.dequeue()
print(hotline(["babu","anu","priya","sai","radha","man"],7))
