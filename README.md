# Count-of-Smaller-Numbers-After-Self
Dado un arreglo de numeros enteros, se debe regresar un nuevo arreglo de conteos. El arreglo de conteos tiene la propiedad donde counts[i] es el número de elementos más pequeños a la derecha de nums[i].

## **Ejemplo 1:**

Entrada: nums = [5,2,6,1]

Salida: [2,1,1,0]

#### **Explicación:**

A la derecha de 5 hay 2 elementos más pequeños (2 and 1).

A la derecha de 2 hay solo 1 elemento más pequeño (1).

A la derecha de 6 hay 1 elemento más pequeño (1).

A la derecha de 1 hay 0 elementos más pequeños.



## **Ejemplo 2:**

Entrada: nums = [-1]

Salida: [0]

## **Ejemplo 3:**

Entrada: nums = [-1,-1]

Salida: [0,0]
 

## **Restricciones:**
1 <= nums.length <= 10<sup>5</sup>

-104 <= nums[i] <= 10<sup>4</sup>
