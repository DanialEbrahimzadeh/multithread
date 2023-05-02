
import tools
from operator import sub

sources_matrix = []
request_sources_matrix = []
available_sources_array = []
process_possess_sources_matrix = []
process_release_sources_matrix = []

def initialize_sourcesـarray_and_matrix():
    generate_source_matrix()
    initialize_process_possess_sources_matrix()
    initialize_process_release_sources_matrix()
    initialize_request_matrix()
    global available_sources_array
    available_sources_array = number_of_example_of_sources(sources_matrix)

def initialize_request_matrix():
    for i in range(5):
        request_sources_matrix.append([])
    for i in range(5):
        for j in range(10):
            request_sources_matrix[i].append(-1)

def initialize_process_possess_sources_matrix():
    for i in range(5):
        process_possess_sources_matrix.append([])
    for i in range(5):
        for j in range(10):
            process_possess_sources_matrix[i].append(0)


def initialize_process_release_sources_matrix():
    for i in range(5):
        process_release_sources_matrix.append([])
    for i in range(5):
        for j in range(10):
            process_release_sources_matrix[i].append(0)


def generate_source_matrix():
    for i in range(10):
        sources_matrix.append([])
    for i in range(10):
        for j in range(5):
            sources_matrix[i].append(-1)

    for i in range(10):
        x = tools.generate_random_number_between_a_and_b(1, 5)
        for j in range(x):
            sources_matrix[i][j]=0

def generate_request(_indexofprocess):
    global available_sources_array
    for i in range(10):
        n = tools.generate_random_number_between_a_and_b(0, available_sources_array[i])
        request_sources_matrix[_indexofprocess][i] = n
    request_sources_matrix[_indexofprocess] = list(map(int.__sub__, request_sources_matrix[_indexofprocess], process_possess_sources_matrix[_indexofprocess]))
    arrangement_request_after_subtracting(_indexofprocess)

def arrangement_request_after_subtracting(index_of_process):
    for i in range(10):
        if request_sources_matrix[index_of_process][i] < 0:
            #request_sources_matrix[index_of_process][i] = abs(request_sources_matrix[index_of_process][i])
            request_sources_matrix[index_of_process][i] = 0

def generate_random_array_for_release(index_of_process):
    temp_array = []
    for i in range(10):
        n = tools.generate_random_number_between_a_and_b(0, process_possess_sources_matrix[index_of_process][i])
        temp_array.append(n)
    return temp_array

def number_of_example_of_sources(sources_matrix):
    result = []
    for i in range(10):
        result.append(0)
    for i in range(10):
        for j in range(5):
            if sources_matrix[i][j] == 0:
                result[i] += 1
    return result

def check_request_can_doing(index_of_process):
    global available_sources_array
    if(request_sources_matrix[index_of_process] <= available_sources_array):
        return True
    return False


def allocate_resources_to_process(index_of_process):
    global available_sources_array
    available_sources_array = list(map(int.__sub__, available_sources_array, request_sources_matrix[index_of_process]))
    process_possess_sources_matrix[index_of_process] = list(map(int.__add__, process_possess_sources_matrix[index_of_process], request_sources_matrix[index_of_process]))


def release_resources_of_process(index_of_process):
    process_release_sources_matrix[index_of_process] = generate_random_array_for_release(index_of_process)
    global available_sources_array
    available_sources_array = list(map(int.__add__, available_sources_array, process_release_sources_matrix[index_of_process]))
    process_possess_sources_matrix[index_of_process] = list(map(int.__sub__, process_possess_sources_matrix[index_of_process], process_release_sources_matrix[index_of_process]))


def print_array_and_matrix():
    global available_sources_array

    print("sources_matrix : ")
    for i in range(10):
        print("\t", sources_matrix[i])
    '''
    print("allocate_sources_array : ")
    print("\t", available_sources_array)

    print("request_sources_matrix : ")
    for i in range(5):
        print("\t", request_sources_matrix[i])

    print("process_possess_sources_matrix : ")
    for i in range(5):
        print("\t", process_possess_sources_matrix[i])

    print("process_release_sources_matrix : ")
    for i in range(5):
        print("\t", process_release_sources_matrix[i])
    '''


def print_process_request(i):
    print("request_sources_array", str(i), " : ", request_sources_matrix[i])


def print_process_release(i):
    print("release_sources_array", str(i), " : ", process_release_sources_matrix[i])

def print_available_resources():
    print("available_sources_array : ", available_sources_array)