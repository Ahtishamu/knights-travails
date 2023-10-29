from tkinter import *
from tkinter import messagebox

# define the movement function 
def move_knight(coords):
    for coord in coords:
        start = coord[0]
        end = coord[1]
        x, y = (start[0]-1) * 50 + 25, (start[1]-1) * 50 + 25
        dx = (end[0] - start[0]) * 50
        dy = (end[1] - start[1]) * 50
        canvas.coords(knight_id, x, y)
        canvas.update()
        canvas.after(500)  # pause for half a second
        canvas.move(knight_id, dx, dy)
        canvas.update()
        canvas.after(500)  # pause for half a second


def enqueue(queue, item):
    queue.append(item)

def dequeue(queue): 
    return queue.pop(0)

def dijkstra_shortest_paths(graph, start, end):
    
    if start not in graph and end not in graph:
        return "Both " + str(start) + " and " + str(end) + " do not exist in the chessboard."
    elif start not in graph:
        return "The Block " + str(start) + " does not exist in the chessboard"
    elif end not in graph:
        return "The Block " + str(end) + " does not exist in the chessboard"
    
    # Create a priority queue for Dijkstra's algorithm
    queue = [(0, start, [])]
 
    # Mark the starting node as visited
    visited = [start]
    
    while queue:
        # Dequeue a vertex with the smallest distance from start
        distance, node, path = dequeue(queue)
 
        if node == end:
            # If the dequeued node is the end node, add the path to shortest_paths
            return path + [(node, distance)]
            break
        else:
            # Otherwise, get all adjacent vertices of the dequeued node
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    # Mark the current node as visited
                    visited.append(neighbor)
                    # Add the path and distance to the neighbor to the queue
                    enqueue(queue, (distance + weight, neighbor, path + [(node, neighbor, weight)]))


# Define a function to handle the button click
def button_clicked():
    # Get the input values from the text boxes
    xx1 = input_box1.get()
    yy1 = input_box2.get()
    xx2 = input_box3.get()
    yy2 = input_box4.get()
    begin=(int(xx1),int(yy1))
    stop=(int(xx2),int(yy2))
    print(begin)
    print(stop)
    coords=dijkstra_shortest_paths(chessGraph, begin, stop)
    if isinstance(coords,str):
        print(coords)
    else:
        steps=coords.pop()
        # move the knight image to the final tile
        for z in range(3):
            move_knight(coords)
        message= "The knight needs",steps[1],"moves to get from the ",begin," to ",stop
        messagebox.showinfo("Message", message)

# create a window and canvas
root = Tk()
root.title("Chessboard")
canvas = Canvas(root, width=400, height=400)
canvas.pack()


# create the chessboard squares
for row in range(8):
    for col in range(8):
        x1 = col * 50
        y1 = row * 50
        x2 = x1 + 50
        y2 = y1 + 50
        if (row + col) % 2 == 0:
            canvas.create_rectangle(x1, y1, x2, y2, fill="white")
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill="black")



# create the knight image and resize it 
knight_img = PhotoImage(file="white_knight.png")
knight_img = knight_img.subsample(2, 2)
knight_id = canvas.create_image(0, 0, image=knight_img)

# add a button to close the window
button = Button(root, text="Close", command=root.destroy)
button.pack()

# root.lift()
# root.attributes('-topmost', True)
# root.after_idle(root.attributes, '-topmost', False)

# Initilize the Graph on which the board is desgined
chessGraph = {}
start = 1
end = 8
for row in range(start, end + 1):
    for column in range(start, end + 1):
        chessGraph[(row, column)] = []

# Create the connections between the Graph
for keys in chessGraph:
    approach1 = (keys[0] - 1, keys[1] - 2)
    if (approach1[0] < start) or (approach1[0] > end) or (approach1[1] < start) or (approach1[1] > end):
        pass
    else:
        chessGraph[keys].append((approach1, 1))
    approach2 = (keys[0] + 1, keys[1] - 2)
    if (approach2[0] < start) or (approach2[0] > end) or (approach2[1] < start) or (approach2[1] > end):
        pass
    else:
        chessGraph[keys].append((approach2, 1))
    approach3 = (keys[0] - 2, keys[1] - 1)
    if (approach3[0] < start) or (approach3[0] > end) or (approach3[1] < start) or (approach3[1] > end):
        pass
    else:
        chessGraph[keys].append((approach3, 1))
    approach4 = (keys[0] + 2, keys[1] - 1)
    if (approach4[0] < start) or (approach4[0] > end) or (approach4[1] < start) or (approach4[1] > end):
        pass
    else:
        chessGraph[keys].append((approach4, 1))
    approach5 = (keys[0] - 2, keys[1] + 1)
    if (approach5[0] < start) or (approach5[0] > end) or (approach5[1] < start) or (approach5[1] > end):
        pass
    else:
        chessGraph[keys].append((approach5, 1))
    approach6 = (keys[0] + 2, keys[1] + 1)
    if (approach6[0] < start) or (approach6[0] > end) or (approach6[1] < start) or (approach6[1] > end):
        pass
    else:
        chessGraph[keys].append((approach6, 1))
    approach7 = (keys[0] - 1, keys[1] + 2)
    if (approach7[0] < start) or (approach7[0] > end) or (approach7[1] < start) or (approach7[1] > end):
        pass
    else:
        chessGraph[keys].append((approach7, 1))
    approach8 = (keys[0] + 1, keys[1] + 2)
    if (approach8[0] < start) or (approach8[0] > end) or (approach8[1] < start) or (approach8[1] > end):
        pass
    else:
        chessGraph[keys].append((approach8, 1))



# Create a Tkinter window
window = Tk()

# Set the window title
window.title("Input Window")

# Create four text boxes for input
input_box1 = Entry(window)
input_box2 = Entry(window)
input_box3 = Entry(window)
input_box4 = Entry(window)

# Set the position of the text boxes
input_box1.grid(row=0, column=1)
input_box2.grid(row=1, column=1)
input_box3.grid(row=2, column=1)
input_box4.grid(row=3, column=1)

# Create four labels for the text boxes
label1 = Label(window, text="x component of starting point:")
label2 = Label(window, text="y component of starting point:")
label3 = Label(window, text="x component of ending point:")
label4 = Label(window, text="y component of ending point:")

# Set the position of the labels
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)

# Create a button for submitting the inputs
submit_button = Button(window, text="Submit", command=button_clicked)

# Set the position of the button
submit_button.grid(row=4, column=0, columnspan=2)




# x1=int(input("Enter the x coordinate of the starting tile: "))
# y1=int(input("Enter the y coordinate of the starting tile: "))
# x2=int(input("Enter the x coordinate of the ending tile: "))
# y2=int(input("Enter the y coordinate of the ending tile: "))
# starttup=(x1,y1)
# endtup=(x2,y2)



# start the Tkinter mainloop    
root.mainloop()