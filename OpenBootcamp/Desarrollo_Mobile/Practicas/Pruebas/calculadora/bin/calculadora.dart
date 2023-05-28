// Calculadora en consola de Dart
// Autor: David Rodríguez

import 'dart:io'; // Imprtamos la librería "io"

void main(List<String> arguments) {
  String ? nombre; // Declaramos una variable "nombre"

  // Generamos un mensaje de bienvenida y pedimos que se ingrese un nombre
  print("Bienvenido!!!... Digita tu nombre: ");
  nombre = stdin.readLineSync()!;
  
  // Llamamos a la función "menuOpciones()" y le pasamos como parámetro el nombre del usuario
  menuOpciones(nombre);
}

void menuOpciones(String nombre) {
  // Variables a usar dentro de la función
  int ? opcion;
  int ? cantidad;
  double ? numero;
  double ? suma;
  double ? resta;
  double ? multiplicacion;
  double ? division;
  double ? porcentaje;
  bool pass = false; // Usamos esta variable como condicional para la ejecución del programa

  // Se ejcutará lo diguiente mientras "pass" sea igual a false
  while (pass == false) {
      opcion = getInt("\n$nombre digita una opción\n"
                      "\n1.) Suma."
                      "\n2.) Resta."
                      "\n3.) Multiplicación."
                      "\n4.) División."
                      "\n5.) Porcentaje de un número."
                      "\n0.) Salir."
                      "\n\nOpción:"); // Pedimos que se ingrese una opción("\n$nombre digita una opcion:\n"

    // Si no se presiona ctrl + D, el programa continuará con su ejecución
    switch (opcion) {
      case 1:
        // Si la opción ingresada es 1
        cantidad = getInt("\nDigita una cantidad de números a sumar:"); // Pedimos que se ingrese una cantidad de números
        suma = sumaOperacion(cantidad); // Enviamos dicha cantidad a "sumaOperacion()"
        print("El resultado de la suma es: $suma"); // Imprimimos el resultado de la suma
        break;
      case 2:
        // Si la opción ingresada es 2
        cantidad = getInt("\nDigita una cantidad de números a restar:"); // Pedimos que se ingrese una cantidad de números
        resta = restaOperacion(cantidad); // Enviamos dicha cantidad a "restaOperacion()"
        print("El resultado de la resta es: $resta"); // Imprimimos el resultado de la resta
        break;
      case 3:
        // Si la opción ingresada es 3
        cantidad = getInt("\nDigita una cantidad de números a sumar:"); // Pedimos que se ingrese una cantidad de números
        multiplicacion = multiplicacionOperacion(cantidad); // Enviamos dicha cantidad a "multiplicacionOperacion"
        print("El resultado de la multiplicación es: $multiplicacion"); // Imprimimos el resultado de la multiplicación
        break;
      case 4:
        // Si la opción ingresada es 4
        cantidad = getInt("\nDigita una cantidad de números a dividir:"); // Pedimos que se ingrese una cantidad de números
        division = divisionOperacion(cantidad); // Enviamos dicha cantidad a "divisionOperacion()"

        if (division == null) {
          print("Error!!!... División entre cero"); // Si "division" es igual a null, se nos muestra este error
        } else {
          print("El resultado de la división es: ${division.toStringAsFixed(3)}"); // Si no, entonces imprimimos el resultado redondeado a 3 decimales
        }

        break;
      case 5:
        // Si la opción ingresada es 5
        porcentaje = porcentajeOperacion(); // Instanciamos a la función "porcentajeOperacion()"
        print("El porcentaje de $numero es: ${porcentaje.toStringAsFixed(2)}"); // Imprimimos el porcentaje redondeado a 3 decimales
        break;
      case 0:
        // Si la opción ingresada es 0
        print("\nHasta luego..."); // Imprimimos un mensaje de despedida
        pass = true; // "pass" será igual a true y se cerrará la ejecución del programa
        break;
      default:
        print("Error!!!... Opción incorrecta"); // Imprimimos un error si la opción ingresada es incorrecta
        break;
    }
  }
}

// Creamos una función "sumaOperacion()" y le psamos como prámetro una cantidad de números
double ? sumaOperacion(int cantidad) {
  double ? numero; // Declaramos una variable "numero"
  double ? suma; // Declaramos una variable "suma"
  List listaNumeros = []; // Declaramos una lista vacia de números
  
  print(""); // Imprimimos un salto de línea

  // Haremos una iteración hasta llegar a "cantidad"
  for (int i = 0; i < cantidad; i++) {
    numero = getDouble("Digita el número ${i + 1}:"); // En cada iteración pediremos un número y lo enviaremos a "getDouble()"
    listaNumeros.add(numero); // Agregaremos el número ingresado a la lista de números
  }

  print("\nLista de números sumados: $listaNumeros\n"); // Imprimimos la lista de números

  // A continuación haremos la suma de cada número de la lista
  // Recorremos todos los elementos de la lista
  for (double num in listaNumeros) {
    if (suma == null) {
      suma = num; // Si "suma" es igual a null le agregamos el primer elemento de la lista
    } else {
      suma += num; // Hacemos la suma de lo que hay en "suma" más el siguiente elemento de la lista
    }
  }

  return suma; // Retornamos el valor de "suma"
}

// Creamos una función "restaOperacion()" y le psamos como prámetro una cantidad de números
double ? restaOperacion(int cantidad) {
  double ? numero; // Declaramos una variable "numero"
  double ? resta; // Declaramos una variable "resta"
  List listaNumeros = []; // Declaramos una lista vacia de números
  
  print(""); // Imprimimos un salto de línea
  
  // Haremos una iteración hasta llegar a "cantidad"
  for (int i = 0; i < cantidad; i++) {
    numero = getDouble("Digita el número ${i + 1}:"); // Pedimos un número en cada iteración
    listaNumeros.add(numero); // Agregamos el número ingresado a la lista de números
  }

  print("\nLista de números a restar: $listaNumeros\n"); // Imprimimos la lista de números

  // A continuación haremos la operación de resta de cada número de la lista
  // Recorremos todos los elementos de la lista
  for (double num in listaNumeros) {
    if (resta == null) {
      resta = num; // Si "resta" es igual a null le agregamos el primer elemento de la lista
    } else {
      resta -= num; // Hacemos la resta de lo que hay en "resta" menos el siguiente elemento de la lista
    }
  }

  return resta; // Retornamos el valor de "resta"
}

// Creamos una función "multiplicacionOperacion()" y le psamos como prámetro una cantidad de números
double ? multiplicacionOperacion(int cantidad) {
  double ? numero; // Declaramos una variable "numero"
  double ? multiplicacion; // Declaramos una variable "multiplicacion"
  List listaNumeros = []; // Pondremos una lista vacia en "listaNumeros"

  print(""); // Imprimimos un salto de línea

  // Haremos una iteración hasta llegar a "cantidad"
  for (int i = 0; i < cantidad; i++) {
    numero = getDouble("Digita el número ${i + 1}:"); // En cada iteración pediremos un número y lo enviaremos a "getDouble()"
    listaNumeros.add(numero); // Agregaremos el número ingresado a la lista de números
  }

  print("\nLista de números a multiplicar: $listaNumeros\n"); // Imprimimos la lista de números

  // A continuación haremos la operación de multiplicación de cada número de la lista
  // Recorremos todos los elementos de la lista
  for (double num in listaNumeros) {
    if (multiplicacion == null) {
      multiplicacion = num; // Si "multiplicacion" es igual a null le agregamos el primer elemento de la lista
    } else {
      multiplicacion *= num; // Hacemos la multiplicación de lo que hay en "multiplicacion" por el siguiente elemento de la lista
    }
  }

  return multiplicacion; // Retornamos el valor de "multiplicacion"
}

// Creamos una función "divisionOperacion()" y le psamos como prámetro una cantidad de números
double ? divisionOperacion(int cantidad) {
  double ? numero; // Declaramos una variable "numero"
  double ? division; // Declaramos una variable "division"
  List listaNumeros = []; // Pondremos una lista vacia en "listaNumeros"
  

  print(""); // Imprimimos un salto de línea

  // Haremos una iteración hasta llegar a "cantidad"
  for (int i = 0; i < cantidad; i++) {
    numero = getDouble("Digita el número ${i + 1}:"); // En cada iteración pediremos un número y lo enviaremos a "getDouble()"
    listaNumeros.add(numero); // Pondremos una lista vacia en "listaNumeros"
  }

  print("\nLista de números a dividir: $listaNumeros\n"); // Imprimimos la lista de números

  // A continuación haremos la operación de división de cada número de la lista
  // Recorremos todos los elementos de la lista
  for (double num in listaNumeros) {
    if (division == null) {
      division = num; // Si "division" es igual a null le agregamos el primer elemento de la lista
    } else {
      division /= num; // Hacemos la división de entre lo que hay en "division" y el siguiente elemento de la lista
    }
  }

  if (division == double.infinity) {
    return null; // Si la división retorna un valor de infinito, retornamos null
  } else {
    return division; // Si no, retornamos el valor de "division"
  }
}

// Porcentaje
double porcentajeOperacion() {
  double ? numero; // Declaramos una variable "numero"
  double ? porcentaje; // Declaramos una variable "division"
  numero = getDouble("Digita un número para calcular su porcentaje:"); // Aquí solo pediremos un número y lo enviaremos a "getDouble()"
  porcentaje = numero / 100; // Calculamos el porcentaje de "Numero"
  
  return porcentaje; // Retornamos el valor de "porcentaje"
}

// A continuación evaluaremos todo lo que el usuario ingrese por teclado
// Creamos una fución "getInt()" que recibe como parámetro una cadena de texto
int getInt(String message) {
  int data = 0; // Declaramos una variable data y la inicializamos en cero
  bool pass = false; // Esta variable nos servirá como condición para esta función

  // Mientras que pass sea igual a false, haremos lo siguiente
  while (pass == false) {
    print(message); // Imprimimos la cadena texto
    
    // Evaluamos lo que se ha ingresado por consola
    try {
      data = int.tryParse(stdin.readLineSync()!)!; // Pedimos que se ingrese un dato y lo convertimos a entero
      pass = true; // Si se ha ingresado un número, entonces "pass" será igual a true y se romperá el ciclo
    } catch (e) {
      print("Error!!!.. Debes digitar un número"); // Si se han ingresado espacios o caracteres, generamos un error hasta que se ingrese un número
    }
  }

  return data; // Retornamos el valor de "data"
}

// Creamos una fución "getDouble()" que recibe como parámetro una cadena de texto
double getDouble(String message) {
  double data = 0; // Declaramos una variable data y la inicializamos en cero
  bool pass = false; // Esta variable nos servirá como condición para esta función

  while (pass == false) {
    print(message); // Imprimimos la cadena texto
    
    // Evalumaos lo que se ha ingresado
    try {
      data = double.tryParse(stdin.readLineSync()!)!; // Pedimos que se ingrese un dato y lo convertimos a entero
      pass = true; // Si se ha ingresado un número, entonces "pass" será igual a true y se romperá el ciclo
    } catch (e) {
      print("Error!!!.. Debes digitar un número"); // Si se han ingresado espacios o caracteres, generamos un error hasta que se ingrese un número
    }
  }

  return data; // Retornamos el valor de "data"
}
