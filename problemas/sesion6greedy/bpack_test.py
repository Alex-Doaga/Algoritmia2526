#!/usr/bin/env python3

from types import ModuleType
from typing import Callable
from traceback import print_tb
import sys

INSTANCE_DIR = "binpacking"
INSTANCES = ["small", "medium", "large"]
PROCESSES = ['process_mq', 'process_pqq', 'process_pqqo']
SOURCE = "binpacking"

type Data = tuple[int, list[int]]
type Result = list[int]
type Process = Callable[[Data], Result]


def warning(m: str, tb=None):
    message("Aviso", m, tb)


def error(m: str, tb=None):
    message("Error", m, tb)


def message(type: str, m: str, tb):
    sys.stderr.write(f"{type}: {m}\n")
    if tb is not None:
        print_tb(tb, file=sys.stderr)
    sys.stderr.write("\n")


def launch_process(process: str, instance: str, data: Data) -> bool:
    # Utilizamos el process() del módulo
    nc = -1
    result = []
    try:
        exec(f"from binpacking import {process}")
        result = eval(f"{process} (data)")
    except Exception as e:
        warning(f"no se ha podido importar {process}")
        return False

    C, w = data
    error = None
    if not isinstance(result, list):
        error = f"{process} no ha devuelto una lista"
    elif len(result) == 0:
        error = f"{process} ha devuelto una lista vacía"
    else:
        nc = max(result) + 1
        sres = set(result)
        if len(result) != len(w):
            error = f"{process} no devuelve una lista de la longitud adecuada"
        elif min(result) < 0:
            error = f"{process} devuelve un contenedor de índice negativo"
        elif len(sres) != nc:
            for c in range(nc):
                if c not in sres:
                    error = f"{process} devuelve, al menos, un contenedor vacío: {c}"
                    break
    # Mostramos el resultado del módulo
    if error is not None:
        print(f"  - {process:19}- {error}")
    else:
        print(f"  - {process:19}- Contenedores: {nc}")
    return error is None


def treat_instance(instance: str, fails_read: set[str], fails_process: set[str]):
    print(f"INSTANCIA '{instance}':")
    try:
        with open(instance) as f:
            ref = (int(f.readline()), [int(l) for l in f.readlines()])
    except Exception as e:
        tb = sys.exc_info()[2]
        warning(f"no se ha cargado {instance} por la excepción {e}", tb)
        return

    for process in PROCESSES:
        if process not in fails_process:
            if not launch_process(process, instance, ref):
                fails_process.add(process)
    C, w = ref
    print(f"  - Como líquido       - Contenedores: {(sum(w) + C - 1) // C}")


def main():
    instances = [f"{INSTANCE_DIR}/{i}.bpk" for i in INSTANCES]
    fails_read = set()
    fails_process = set()
    for instance in instances:
        treat_instance(instance, fails_read, fails_process)


if __name__ == "__main__":
    main()
