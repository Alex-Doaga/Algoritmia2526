from random import seed
from tkinter.font import names

from algoritmia.viewers.labyrinth_viewer import LabyrinthViewer

from shortest_path import process , Data,  Result

if __name__ == '__main__':
    seed(42)
    n_rows  = 30
    n_cols = 40
    data: Data = (n_rows,n_cols)

    result: Result = process(data)
    lab, path = result

    lv = LabyrinthViewer(lab, canvas_width= 1024, canvas_height=760, margin=10)
    lv.add_path(path, color='red')

    lv.run()
    print("Hola")