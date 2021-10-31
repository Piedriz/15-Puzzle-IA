
import sys
import time
import argparse
from Class import Tablero
from Functions import bfs, astar, guloso, hamming, manhattan


def main():
    # Comandos
    parser = argparse.ArgumentParser()
    parser.add_argument('--bfs', action='store_true')
    parser.add_argument('--astar', '--a', type=int, choices=[1, 2],
                        help='A* opciones [1,2] (1 -hamming; 2 -manhattan)')
    parser.add_argument('--greedy', '--gulosa', type=int, choices=[1, 2],
                        help='greedy opciones [1,2] (1 -hamming; 2 -manhattan)')
    parser.add_argument('--input', '-i')
    args = parser.parse_args()

 
    if args.input is None:
    
        print("Por favor escriba --input seguido de 4x4.txt y el metodo")
    else:
        # file
        try:
            numbers = []
            with open(args.input, "r") as f:
                lines = f.readlines()
                for line in lines:
                    numbers = numbers + line.split()
            inicialState = numbers[:16]
            numbers = numbers[16:]
            goalState = numbers[:16]
        except FileNotFoundError:
            sys.stderr.write("Ruta invalida del txt")
            sys.exit(1)

    # iniciar tablero
    inicialState = Tablero(inicialState)
    goalState = Tablero(goalState)
    print("\nEstado inicial:\n ")
    print(inicialState)
    print("\n")
    print("Estado final:\n")
    print(goalState)

    
   
    if args.bfs:
        print("Primero en anchura:")
        initial = time.time()
        moves, nodes = bfs(inicialState, goalState)
        fin = time.time()
        print("Tiempo computacional: ",(fin-initial))
        print(nodes, "N nodos visitados.")
        if moves:
            print("Solución:")
            print(" -> ".join(moves))
        else:
            print("No se enontró solución.")


    if args.astar:
        print("A* Busqueda:")
        comp = manhattan
        if args.astar == 1:
            comp = hamming
        initial = time.time()
        moves, nodes = astar(inicialState, goalState, comp)
        fin = time.time()
        print("Tiempo computacional: ",(fin-initial))
        print(nodes, "N nodos visitados.")
        if moves:
            print("Solución:")
            print(" -> ".join(moves))
        else:
            print("No se encontró solución.")

    if args.greedy:
        print("Primero el mejor:")
        comp = manhattan
        if args.astar == 1:
            comp = hamming
        initial = time.time()
        moves, nodes = guloso(inicialState, goalState, comp)
        fin = time.time()
        print("Tiempo computacional: ",(fin-initial))
        print(nodes, "N nodos visitados.")
        if moves:
            print("Solución:")
            print(" -> ".join(moves))
        else:
            print("No se encontró solución.")

if __name__ == '__main__':
    main()
