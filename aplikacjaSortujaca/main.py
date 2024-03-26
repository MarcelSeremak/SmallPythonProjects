
import tkinter
import time
import random




### Sorting algorithms

def bubbleSort(arr):
    n = len(arr)
    swapped = False

    for i in range(n - 1):

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return
    return arr


def insertionSort(arr):
    n = len(arr)

    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
    return array


def selectionSort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
    return array

###

window = tkinter.Tk()
window.wm_title("Aplikacja Sortująca")
window.wm_minsize(width = 300, height = 400)
window.wm_maxsize(width = 300, height = 400)
background = tkinter.PhotoImage(file = "tlo.png")
canvas = tkinter.Canvas(window, width = 300, height = 400)
canvas.pack(fill = "both", expand = True)
canvas.create_image(0, 0, image = background, anchor="nw")

def start():
    canvas.destroy()
    window.config(bg = "#99C1F1")
    chooseText = tkinter.Label(text = "Choose how much elements \n would arrays contain")
    chooseText.grid(row = 0, column = 0, pady = 70, columnspan = 1, padx = 60)
    spinbox = tkinter.Spinbox(from_=1000, to=100000)
    spinbox.grid(row = 1, column = 0, pady = 20)

    def startingSort():
        numberOfElements = int(spinbox.get())
        window.destroy()
        listOfElements=[random.randint(0,500) for _ in range(numberOfElements)]

        start=time.time()
        bubbleSort(listOfElements[:])
        end=time.time()
        bubbleSortTime = round(end - start,5)

        start=time.time()
        insertionSort(listOfElements[:])
        end=time.time()
        insertionSortTime = round(end - start,5)

        start = time.time()
        quickSort(listOfElements[:],0,len(listOfElements)-1)
        end = time.time()
        quickSortTime = round(end - start,5)

        start = time.time()
        selectionSort(listOfElements[:],len(listOfElements))
        end = time.time()
        selectionSortTime = round(end - start,5)

        windowResult = tkinter.Tk()
        windowResult.wm_title("Wyniki sortowania")
        windowResult.wm_maxsize(width=400, height=200)
        windowResult.wm_minsize(width=400, height=200)
        windowResult.config(bg= "#99C1F1")
        resultsCanvas = tkinter.Canvas(windowResult, width=200, height=200, bg="#99C1F1")
        resultsCanvas.create_text(110,50, text=f"Bubble sort: {bubbleSortTime}",font=('Trebuchet 10 bold'))
        resultsCanvas.create_text(110, 70, text=f"Insertion sort: {insertionSortTime}",font=('Trebuchet 10 bold'))
        resultsCanvas.create_text(110, 90, text=f"Quick sort: {quickSortTime}",font=('Trebuchet 10 bold'))
        resultsCanvas.create_text(110, 110, text=f"Selection sort: {selectionSortTime}",font=('Trebuchet 10 bold'))
        resultsCanvas.grid(row = 0 , column = 0)
        def endApp():
            windowResult.destroy()
        buttonDestroy = tkinter.Button(windowResult,text="Ok, thanks",font = ("Helvetica", 15, "bold"), width = 10, height = 3, background = "lightblue", command=endApp)
        buttonDestroy.grid(row = 0, column = 1, padx=30)


        window.mainloop()


    cofirmButton = tkinter.Button(text="Confirm", font=("Helvetica", 15, "bold"), command=startingSort)
    cofirmButton.grid(row = 3, column = 0)


startingButton = tkinter.Button(window, text = "Let's begin!", font = ("Helvetica", 15, "bold"), width = 20, height = 3, background = "lightblue", command = start)
canvasStartingButton = canvas.create_window(28, 260, anchor = "nw", window = startingButton)





window.mainloop()
