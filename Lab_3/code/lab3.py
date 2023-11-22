import tkinter as tk
import time

class LineDrawingApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Line Drawing with Bresenham's Algorithm")
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.scale = 15  # Initial scale
        self.start_point = None
        self.selected_algorithm = None  # Initially no algorithm is selected

        # Dropdown menu for selecting the algorithm
        self.algo_choice = tk.StringVar(value="bresenham")
        self.algo_menu = tk.OptionMenu(self.root, self.algo_choice, "bresenham", "step_by_step", command=self.select_algorithm)
        self.algo_menu.pack()

        self.draw_time_label()

        self.canvas.bind("<Button-1>", self.set_start_point)
        self.canvas.bind("<Button-3>", self.draw_line)
        self.canvas.bind("<MouseWheel>", self.zoom)

        self.draw_grid()  

    def plot(self, x, y, color='black'):
        scaled_x, scaled_y = x * self.scale, y * self.scale
        self.canvas.create_rectangle(scaled_x, scaled_y, scaled_x + self.scale, scaled_y + self.scale, fill=color, outline=color)

    def set_start_point(self, event):
        grid_x, grid_y = event.x // self.scale, event.y // self.scale
        self.start_point = (int(grid_x), int(grid_y))
        print(self.start_point)

    def draw_bresenham_line(self, event):
        if self.start_point:
            start_time = time.time()
            x_start, y_start = self.start_point
            x_end, y_end = int(event.x // self.scale), int(event.y // self.scale)

            dx = int(abs(x_end - x_start))
            dy = int(abs(y_end - y_start))
            x, y = x_start, y_start

            # Bresenham's line drawing algorithm
            if dx > dy:
                p = 2 * dy - dx
                for i in range(dx+1):
                    self.plot(x, y, 'orange')
                    if p >= 0:
                        y += 1 if y_end > y_start else -1
                        p -= 2 * dx
                    x += 1 if x_end > x_start else -1
                    p += 2 * dy
            else:
                p = 2 * dx - dy
                for i in range(dy+1):
                    self.plot(x, y, 'orange')
                    if p >= 0:
                        x += 1 if x_end > x_start else -1
                        p -= 2 * dy
                    y += 1 if y_end > y_start else -1
                    p += 2 * dx

            end_time = time.time()
            draw_time = end_time - start_time
            self.time_label.config(text=f"Time taken: {draw_time} sec")

    def draw_step_by_step_line(self, event):
        if self.start_point:
            start_time = time.time()
            x_start, y_start = self.start_point
            x_end, y_end = event.x // self.scale, event.y // self.scale

            dx = abs(x_end - x_start)
            dy = abs(y_end - y_start)

            if dx >= dy:
                m = dx
            else:
                m = dy
            m = int(m)
            dx = (x_end - x_start) / m
            dy = (y_end - y_start) / m
            x, y = x_start, y_start

            for _ in range(m+1):
                self.plot(int(x), int(y), 'pink')
                x += dx
                y += dy

            end_time = time.time()
            draw_time = end_time - start_time
            self.time_label.config(text=f"Time taken: {draw_time} sec")

    def select_algorithm(self, choice):
        if choice == "bresenham":
            self.selected_algorithm = self.draw_bresenham_line
        elif choice == "step_by_step":
            self.selected_algorithm = self.draw_step_by_step_line

    def draw_line(self, event):
        if self.selected_algorithm:
            self.selected_algorithm(event)

    def zoom(self, event):
        factor = 1.1 if event.delta > 0 else 0.9  # Zoom factor
        self.scale *= factor
        self.canvas.scale("all", event.x, event.y, factor, factor)

    def draw_grid(self):
        for i in range(0, 600):
            self.canvas.create_line(i * self.scale, 0, i * self.scale, 400 * self.scale, fill="lightgray", tags="grid")
        for i in range(0, 400):
            self.canvas.create_line(0, i * self.scale, 600 * self.scale, i * self.scale, fill="lightgray", tags="grid")
            
    

    def draw_time_label(self):
        self.time_label = tk.Label(self.root, text="Time taken: ")
        self.time_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = LineDrawingApp(root)
    root.mainloop()

