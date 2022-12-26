'''
import sys
import time
import gc
from tgdhstruct import MemberAgent
from memory_profiler import profile

@profile
def create(size):

    group_tree = MemberAgent(size)
    for i in range(10):
        group_tree.join_protocol()
    for i in range(10):
        group_tree.leave_protocol(i+1)
        gc.collect()
    group_tree.close()
    time.sleep(2)
    del group_tree
    gc.collect()

def main(argv):

    # starting the monitoring
    tracemalloc.start()
  
    create(int(argv[1]))

    # displaying the memory
    print(tracemalloc.get_traced_memory())

    tracemalloc.stop()
    
if __name__=='__main__':
    main(sys.argv)
'''

import sys
from pytictoc import TicToc
from tgdhstruct import MemberAgent

def main(argv):

    # create the initial group
    #
    group_tree = MemberAgent(int(argv[1]))

    # starting the monitoring
    #
    t = TicToc()
    t.tic()

    group_tree.leave_protocol(2)
    group_tree.close()

    # display the traced memory
    #
    time = t.tocvalue()

    # write data to files
    #
    with open('iters_t_leave.txt', 'a') as f:
        f.write(str(int(argv[1])))
        f.write('\n')

    with open('times_leave.txt', 'a') as f:
        f.write(str(time))
        f.write('\n')

    # exit gracefully
    #
    return 0
    
# begin gracefully
#
if __name__=='__main__':
    main(sys.argv)

#
# end file
