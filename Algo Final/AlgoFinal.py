import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from random import randint


def arraySortedOrNot(arr):
    n = len(arr)
    if n == 1 or n == 0:
        return True
    return arr[0] <= arr[1] and arraySortedOrNot(arr[1:])


def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int((index) % 10)] += 1
        yield arr

    for i in range(1, 10):
        count[i] += count[i - 1]
        yield arr

    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1
        yield arr
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
        yield arr


def counting(arr):
    n = len(arr)
    arr1 = [0] * n

    x = [0] * (max(arr)+1)

    for i in range(0, n):
        x[arr[i]] += 1

    for i in range(1, max(arr)+1):
        x[i] += x[i - 1]

    i = n - 1
    while i >= 0:
        arr1[x[arr[i]] - 1] = arr[i]
        x[arr[i]] -= 1
        i -= 1

    for i in range(0, n):
        arr[i] = arr1[i]
        yield arr



def radixSort(arr):
    max1 = max(arr)
    exp = 1

    while max1 / exp > 0:
        yield from countingSort(arr, exp)
        exp *= 10
        yield arr


def bucketSort(array):
    if (arraySortedOrNot(array)):
        print("Best Case Time Complexity = O(N+K) = ", len(array)+max(array))
    else:
        print("Average Case Time Complexity = O(N+K) = ", len(array)+max(array))

    largest = max(array)
    length = len(array)
    size = largest / length

    buckets = [[] for i in range(length)]

    for i in range(length):
        index = int(array[i] / size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])

    for i in range(len(array)):
        buckets[i] = sorted(buckets[i])

    result = []

    for i in range(length):
        result = result + buckets[i]
        array = result
        yield array


def bubble_sort(list_):

    if len(list_) == 1:
        return
    yield list_
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list_) - 1):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
                swapped = True
            yield list_


def swap(A, i, j):

    if i != j:
        A[i], A[j] = A[j], A[i]


def quick_sort(A, start, end):

    if start >= end:
        return

    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quick_sort(A, start, pivotIdx - 1)
    yield from quick_sort(A, pivotIdx + 1, end)


def insertion_sort(list_):
    for i in range(1, len(list_)):
        insert_number = list_[i]
        j = i - 1
        while j >= 0 and list_[j] > insert_number:
            list_[j + 1] = list_[j]
            j -= 1
            yield list_
        list_[j + 1] = insert_number
        yield list_


def shell_sort(list_):
    n = len(list_)
    gap = n // 2
    yield list_
    while gap > 0:
        for i in range(gap, n):
            temp = list_[i]
            j = i
            while j >= gap and list_[j - 1] > temp:
                list_[j] = list_[j - 1]
                yield list_
                j -= 1
            list_[j] = temp
            yield list_
        gap //= 2


def merge_sort(list_, left_index, right_index):
    if left_index >= right_index:
        return
    middle = (left_index + right_index) // 2
    yield from merge_sort(list_, left_index, middle)
    yield from merge_sort(list_, middle + 1, right_index)
    yield from merge(list_, left_index, right_index, middle)
    yield list_


def merge(list_, left_index, right_index, middle):
    left_copy = list_[left_index:middle + 1]
    right_copy = list_[middle + 1:right_index + 1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            list_[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1

        else:
            list_[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1
        sorted_index += 1
        yield list_
    while left_copy_index < len(left_copy):
        list_[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1
        yield list_
    while right_copy_index < len(right_copy):
        list_[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1
        yield list_


def heapify(list_, heap_size, index):
    largest = index
    left = index * 2 + 1
    right = index * 2 + 2

    if left < heap_size and list_[largest] < list_[left]:
        largest = left
    if right < heap_size and list_[largest] < list_[right]:
        largest = right

    if largest != index:
        list_[index], list_[largest] = list_[largest], list_[index]
        yield list_
        yield from heapify(list_, heap_size, largest)


def heap_sort(list_):
    heap_size = len(list_)
    for i in range(heap_size, -1, -1):
        yield from heapify(list_, heap_size, i)
    for i in range(heap_size - 1, 0, -1):
        list_[0], list_[i] = list_[i], list_[0]
        yield from heapify(list_, i, 0)
        yield list_

##########################################
def insertion_sort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val
        yield arr

def partition(arr, low, high):
    pivot = arr[high]
    i = j = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j



def hybrid_quick_sort(arr, low, high):
    while low < high:

        if high - low + 1 < 10:
            yield from insertion_sort(arr, low, high)
            break

        else:
            pivot = partition(arr, low, high)
            yield arr

            if pivot - low < high - pivot:
                yield from hybrid_quick_sort(arr, low, pivot - 1)
                low = pivot + 1
            else:
                yield from hybrid_quick_sort(arr, pivot + 1, high)
                high = pivot - 1
                yield arr
################################################
def Advanced_Counting_Sort(array):
    size = len(array)
    output = [0] * size
    count = [0] * (max(array)+1)

    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, max(array)+1):
        count[i] += count[i - 1]


    a = int(input("Enter range a: "))
    b = int(input("Enter range b: "))
    answer = count[b] - count[a]
    print(answer)

class getRange:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x400')
        self.root.title('Anas and Bari Visual Sorter')
        self.root.resizable(0, 0)
        self.alg = StringVar()
        self.var_size = StringVar()
        self.var_alg = StringVar()
        self.label_alg = Label(self.root, textvariable=self.var_alg)
        self.label_alg.place(x=198, y=8)
        self.var_alg.set('Choose sorting algorithm:')
        self.box2 = ttk.Combobox(self.root, width=20, textvariable=self.alg,
                                 state='readonly', height=8)

        self.box_values = ('Bubble Sort', 'Insertion Sort',
                           'Merge Sort', 'Radix Sort', 'Heap Sort', 'Counting Sort',
                           'Quick Sort', 'Bucket Sort', 'Advanced Quick Sort (7.4-5)',
                           'Advanced Counting Sort (8.2.4)')
        self.box2['values'] = self.box_values
        self.box2.bind('<<ComboboxSelected>>', self.sort_alg)
        self.box2.place(x=200, y=30, width=150)
        self.butt = Button(self.root, text='Sort', command=self.Entry, relief=GROOVE)
        self.butt.place(x=240, y=350, width=60, height=25)
        self.butt2 = Button(self.root, text='Cancel', command=self.root.destroy, relief=GROOVE)
        self.butt2.place(x=310, y=350, width=60, height=25)
        self.butt3 = Button(self.root, text='Generate Files', command=self.GenerateFiles, relief=GROOVE)
        self.butt3.place(x=140, y=350, width=90, height=25)
        self.Algorithm = None
        self.temp = None
        self.Range = None
        self.root.mainloop()

    def sort_alg(self, event):
        self.Algorithm = self.box2.get()

    def size(self, event):
        self.temp = self.size_box.get()
        self.Range = int(self.temp)

    def Entry(self):
        try:
            self.animate()
        except TypeError:
            pass

    def GenerateFiles(self):
        # GENERATE THREE FILES
        print("Generating Files.....")

        f1 = open("small.txt", "w")
        for i in range(10):
            i = randint(100, 150)
            i = str(i)
            f1.write(i + "\n")
        f1.close()

        f1 = open("medium.txt", "w")
        for i in range(1000):
            i = randint(100, 999)
            i = str(i)
            f1.write(i + "\n")
        f1.close()

        f1 = open("high.txt", "w")
        for i in range(1000000):
            i = randint(100000, 999999)
            i = str(i)
            f1.write(i + "\n")
        f1.close()

        print("Small, Medium and High files generated successfully.....")

    def animate(self):
        filepath = filedialog.askopenfilename()
        file = open(filepath, 'r')
        A = []
        for number in file:
            A.append(int(number))

        if self.Algorithm == 'Bubble Sort':
            if (arraySortedOrNot(A)):
                complexity = str(len(A))
                title = "Bubble Sort. Best Case Time Complexity = O(N) " + complexity
            else:
                complexity = str(len(A) * len(A))
                title = "Bubble Sort. Average Case Time Complexity = O(N*N) = " + complexity
            generator = bubble_sort(A)
        elif self.Algorithm == 'Insertion Sort':
            if (arraySortedOrNot(A)):
                complexity = str(len(A))
                title = "Insertion Sort. Best Case Time Complexity = O(N) = "+ complexity
            else:
                complexity = str(len(A) * len(A))
                title = "Insertion Sort. Average Case Time Complexity = O(N*N) = ", complexity
            generator = insertion_sort(A)
        elif self.Algorithm == 'Merge Sort':

            if (arraySortedOrNot(A)):
                complexity = str(len(A) * math.log(len(A)))
                title = "Merge Sort. Best Case Time Complexity = O(N*log(N)) = " + complexity
            else:
                complexity = str(len(A) * math.log(len(A)))
                title = "Merge Sort. Average Case Time Complexity = O(N*log(N)) = " + complexity

            generator = merge_sort(A, 0, len(A) - 1)
        elif self.Algorithm == 'Heap Sort':
            if (arraySortedOrNot(A)):
                complexity = str(len(A) * math.log(len(A)))
                title = "Heap Sort. Best Case Time Complexity = O(N*log(N)) = "+ complexity
            else:
                complexity = str(len(A) * math.log(len(A)))
                title = "Heap Sort. Average Case Time Complexity = O(N*log(N)) = "+complexity
            generator = heap_sort(A)
        elif self.Algorithm == 'Quick Sort':
            title = 'Quick Sort'
            if (arraySortedOrNot(A)):
                complexity = str(len(A) * math.log(len(A)))
                title = "Quick Sort. Best Case Time Complexity = O(N*log(N)) = "+ complexity
            else:
                complexity =  str(len(A) * len(A))
                title = "Quick Sort. Average Case Time Complexity = O(N^2) = "+complexity

            generator = quick_sort(A, 0, len(A)-1)
        elif self.Algorithm == 'Radix Sort':
            if (arraySortedOrNot(A)):
                complexity = str(len(A) * max(A))
                title = "Radix Sort. Best Case Time Complexity = O(Nk) = "+ complexity
            else:
                complexity =  str(len(A) * max(A))
                title = "Radix Sort. Average Case Time Complexity = O(Nk) = "+complexity
            generator = radixSort(A)
        elif self.Algorithm == 'Bucket Sort':
            if (arraySortedOrNot(A)):
                complexity = str(len(A) * len(A))
                title = "Bucket Sort. Best Case Time Complexity = O(N^2) = "+complexity
            else:
                complexity = str(len(A) + max(A))
                title = "Bucket Sort. Average Case Time Complexity = O(N+K) = "+complexity

            generator = bucketSort(A)

        elif self.Algorithm == 'Counting Sort':
            if (arraySortedOrNot(A)):
                complexity = str(len(A))
                title = "Counting Sort. Best Case Time Complexity = O(N) = " + complexity
            else:
                complexity = str(len(A) + max(A))
                title = "Counting Sort. Average Case Time Complexity = O(N+K) = " + complexity
            generator = counting(A)
        elif self.Algorithm == 'Advanced Quick Sort (7.4-5)':
            complexity = str(len(A) * math.log(len(A)))
            title = 'Advanced Quick Sort. Average Case Time Complexity = O(N*log(N)) = '+ complexity
            generator = hybrid_quick_sort(A,0,len(A)-1)

        elif self.Algorithm == 'Advanced Counting Sort (8.2.4)':
            Advanced_Counting_Sort(A)
            exit()
        fig, ax = plt.subplots()
        title_ = plt.title(title)
        bar_ = ax.bar(range(len(A)), A, align='edge', color='blue')
        ax.set_xlim(0, len(A))
        ax.set_ylim(0, int(1.05 * max(A)))
        iterations = [0]

        def update_fig(list_, rect, iteration):
            for bar_rect, val in zip(rect, list_):
                bar_rect.set_height(val)
            iteration[0] += 1
            plt.pause(0.2)

        anim = animation.FuncAnimation(fig, func=update_fig,
                                       fargs=(bar_, iterations),
                                       frames=generator, interval=10,
                                       repeat=False)
        plt.show()
getRange()
