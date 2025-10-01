
from algoritmia.viewers.labyrinth_viewer import LabyrinthViewer
from labyrinth import process

if __name__ == "__main__":
    rows = int(input("Filas: "))
    cols = int(input("Columnas: "))
    data = (rows, cols)
    labyrinth = process(data)
    lv = LabyrinthViewer(labyrinth,
    canvas_width=100 * cols,
    canvas_height=100 * rows)
    lv.run()