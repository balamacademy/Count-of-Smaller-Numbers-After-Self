# Count-of-Smaller-Numbers-After-Self
Dado un arreglo de numeros enteros (**nums**), se debe regresar un nuevo arreglo de conteos (**counts**). El arreglo **counts** almacena la cantidad de elementos menores hacia la derecha del valor en **nums[i]**, en la misma posición i **counts[i]**

## **Ejemplo 1:**

      Entrada: nums = [5,2,6,1]

      Salida: [2,1,1,0]

      Explicación:

      -A la derecha de 5 hay 2 elementos más pequeños (2 and 1).

      -A la derecha de 2 hay solo 1 elemento más pequeño (1).

      -A la derecha de 6 hay 1 elemento más pequeño (1).

      -A la derecha de 1 hay 0 elementos más pequeños.



## **Ejemplo 2:**

        Entrada: nums = [-1]

        Salida: [0]

## **Ejemplo 3:**

           Entrada: nums = [-1,-1]

            Salida: [0,0]
 
## **Indicaciones:**

1. Realiza tu código en el archivo nombrado "countsmaller.py"

2. Evalúa tu código con el archivo "test_countsmaller.py" (pytest)
