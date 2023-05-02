
import random
import threading
import time
import resource
import tools
from queue import Queue

processSemaphores = [threading.Semaphore(0), threading.Semaphore(0)]
allocat_semaphore = threading.Semaphore(0)
release_semaphore = threading.Semaphore(0)
watchful = threading.Semaphore(1)
is_finishing = False
queue1 = Queue()
queue2 = Queue()

def process(index_of_process, queue1, queue2):
    global is_finishing

    while is_finishing == False:

        queue1.put(index_of_process)

        # wake up function to create and send request
        allocat_semaphore.release()

        # stop this process to check request
        processSemaphores[index_of_process].acquire()

        # working
        time.sleep(3)

        queue2.put(index_of_process)

        release_semaphore.release()

        # stop this process to release resources
        processSemaphores[index_of_process].acquire()

    print("finish process", index_of_process)


def allocator():
    global is_finishing

    while is_finishing == False:

        # stop self until wake up with a process
        allocat_semaphore.acquire()

        index_of_process = queue1.get()

        watchful.acquire()
        resource.generate_request(index_of_process)

        resource.print_process_request(index_of_process)

        if resource.check_request_can_doing(index_of_process):
            resource.allocate_resources_to_process(index_of_process)
            print("=======> allocate resource to process ", index_of_process, " : ")
        else:
            print("=======> don't allocate resource to process ", index_of_process, " : ")
        watchful.release()

        # wake up the process
        processSemaphores[index_of_process].release()


def release():
    global is_finishing

    while is_finishing == False:

        # stop self until wake up with a process
        release_semaphore.acquire()

        index_of_process = queue2.get()

        watchful.acquire()
        resource.release_resources_of_process(index_of_process)
        print("=======> release resource of process ", index_of_process, " : ")
        resource.print_process_release(index_of_process)
        resource.print_available_resources()
        watchful.release()

        # wake up the process
        processSemaphores[index_of_process].release()


def show_information():
    print("================Show information================ \n")
    resource.print_array_and_matrix()


def finishing():
    global is_finishing
    is_finishing = True
    time.sleep(5)
    print("================THE END================ \n")
    resource.print_array_and_matrix()


def user_control():
    while True:
        key_input = input("")
        if key_input == '0':
            finishing()
        else:
            if key_input == '1':
                show_information()
            else:
                print("Your is invalid!!!! Try again!\n")


if __name__ == '__main__':

    resource.initialize_sourcesـarray_and_matrix()
    resource.print_array_and_matrix()

    user_control_thread = threading.Thread(target=user_control)
    user_control_thread.start()

    allocator_thread = threading.Thread(target=allocator, )
    allocator_thread.start()

    release_thread = threading.Thread(target=release, )
    release_thread.start()

    process0_thread = threading.Thread(target=process, args=(0, queue1, queue2), name="thread_0")
    process1_thread = threading.Thread(target=process, args=(1, queue1, queue2), name="thread_1")

    process0_thread.start()
    process1_thread.start()