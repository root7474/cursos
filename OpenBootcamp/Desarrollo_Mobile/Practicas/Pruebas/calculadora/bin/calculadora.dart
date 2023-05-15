// Calculadora en consola de Dart
// Autor: David Rodríguez

import 'dart:io'; // Imprtamos la librería "io"

void main(List<String> arguments) {
  // Variables a usar dentro de la aplicaión
  String ? nombre;
  int ? opcion;
  int ? cantidad;
  double ? numero;
  double ? suma;
  double ? resta;
  double ? multiplicacion;
  double ? division;
  double ? porcentaje;
  bool pass = false; // Usamos esta variable como condicional para la ejecución del programa
  List listaNumeros; // Declaramos un variable tipo lista para guardar un cantidad de números

  // Generamos un mensaje de bienvenida y pedimos que se ingrese un nombre
  print("Bienvenido!!!... Digita tu nombre: ");
  nombre = stdin.readLineSync();

  // Se ejcutará lo diguiente mientras "pass" sea igual a false
  while (pass == false) {
    print("\n$nombre digita una opcion:\n"
          "\n1.) Suma."
          "\n2.) Resta."
          "\n3.) Multiplicación."
          "\n4.) División."
          "\n5.) Porcentaje de un número."
          "\n0.) Salir."
          "\n\nOpción:"); // Imprimimos un menú de opciones

    try {
      // Si no se presiona ctrl + D, el programa continuará con su ejecución
      opcion = int.tryParse(stdin.readLineSync()!); // Pedimos que se ingrese una opción

      // Si la opción ingresada es 1
      if (opcion == 1) {
        suma = null; // "suma" será igual a null
        listaNumeros = []; // En cada iteración pondremos una lista vacia en "listaNumeros"

        // Lo siguiente se ejecutará hasta que la cantidad ingresada sea un número
        while (true) {
          print("\nDigita una cantidad de números a sumar:");
          cantidad = int.tryParse(stdin.readLineSync()!);

          if (cantidad == null) {
            print("Error!!!... Debes digitar números");
          } else {
            break;
          }
        }

        print(""); // Imprimimos un salto de línea

        // Haremos una iteración hasta llegar a "cantidad"
        for (int i = 0; i < cantidad; i++) {
          print("Digita el número ${i + 1}:"); // Pedimos que se ingrese un número
          numero = double.tryParse(stdin.readLineSync()!); // Intentaremos convertir ese número a double

          // Evaluamos que lo que se ha ingresado sea un número
          if (numero == null) {
            print("Error!!!... Debes digitar números");
            i--; // Retrocederemos -1 si no se ha ingresado un número
          } else {
            listaNumeros.add(numero); // Si se ha ingresado un número, lo agregamos a la lista
          }
        }

        print("\nLista de números sumados: $listaNumeros\n"); // Imprimimos la lista de números

        // A continuación haremos la operación de suma de cada número de la lista
        // Recorremos todos los elementos de la lista
        for (double num in listaNumeros) {
          if (suma == null) {
            suma = num; // Si "suma" es igual a null le agregamos el primer elemento de la lista
          } else {
            suma += num; // Hacemos la suma de lo que hay en "suma" + el siguiente elemento de la lista
          }
        }

        print("El resultado de la suma es: $suma"); // Imprimimos el resultado de la suma
      } else if (opcion == 2) {
        // Si la opción ingresada es 2
        resta = null; // "resta" será igual a null
        listaNumeros = []; // En cada iteración pondremos una lista vacia en "listaNumeros"

        // Lo siguiente se ejecutará hasta que la cantidad ingresada sea un número
        while (true) {
          print("\nDigita una cantidad de números a restar:");
          cantidad = int.tryParse(stdin.readLineSync()!);

          if (cantidad == null) {
            print("Error!!!... Debes digitar números");
          } else {
            break;
          }
        }

        print(""); // Imprimimos un salto de línea

        // Haremos una iteración hasta llegar a "cantidad"
        for (int i = 0; i < cantidad; i++) {
          print("Digita el número ${i + 1}:"); // Pedimos que se ingrese un número
          numero = double.tryParse(stdin.readLineSync()!); // Intentaremos convertir ese número a double

          // Evaluamos que lo que se ha ingresado sea un número
          if (numero == null) {
            print("Error!!!... Debes digitar números");
            i--; // Retrocederemos -1 si no se ha ingresado un número
          } else {
            listaNumeros.add(numero); // Si se ha ingresado un número, lo agregamos a la lista
          }
        }

        print("\nLista de números a restar: $listaNumeros\n"); // Imprimimos la lista de números

        // A continuación haremos la operación de resta de cada número de la lista
        // Recorremos todos los elementos de la lista
        for (double num in listaNumeros) {
          if (resta == null) {
            resta = num; // Si "resta" es igual a null le agregamos el primer elemento de la lista
          } else {
            resta -= num; // Hacemos la resta de lo que hay en "resta" - el siguiente elemento de la lista
          }
        }

        print("El resultado de la resta es: $resta"); // Imprimimos el resultado de la resta
      } else if (opcion == 3) {
        // Si la opción ingresada es 2
        multiplicacion = null; // "multiplicacion" será igual a null
        listaNumeros = []; // En cada iteración pondremos una lista vacia en "listaNumeros"

        // Lo siguiente se ejecutará hasta que la cantidad ingresada sea un número
        while (true) {
          print("\nDigita una cantidad de números a multiplicar:");
          cantidad = int.tryParse(stdin.readLineSync()!);

          if (cantidad == null) {
            print("Error!!!... Debes digitar números");
          } else {
            break;
          }
        }

        print(""); // Imprimimos un salto de línea

        // Haremos una iteración hasta llegar a "cantidad"
        for (int i = 0; i < cantidad; i++) {
          print("Digita el número ${i + 1}:"); // Pedimos que se ingrese un número
          numero = double.tryParse(stdin.readLineSync()!); // Intentaremos convertir ese número a double

          // Evaluamos que lo que se ha ingresado sea un número
          if (numero == null) {
            print("Error!!!... Debes digitar números");
            i--; // Retrocederemos -1 si no se ha ingresado un número
          } else {
            listaNumeros.add(numero); // Si se ha ingresado un número, lo agregamos a la lista
          }
        }

        print("\nLista de números a multiplicar: $listaNumeros\n"); // Imprimimos la lista de números

        // A continuación haremos la operación de multiplicación de cada número de la lista
        // Recorremos todos los elementos de la lista
        for (double num in listaNumeros) {
          if (multiplicacion == null) {
            multiplicacion = num; // Si "multiplicacion" es igual a null le agregamos el primer elemento de la lista
          } else {
            multiplicacion *= num; // Hacemos la multiplicación de lo que hay en "multiplicacion" - el siguiente elemento de la lista
          }
        }

        print("El resultado de la multiplicación es: $multiplicacion"); // Imprimimos el resultado de la multiplicación
      } else if (opcion == 4) {
        // Si la opción ingresada es 2
        division = null; // "division" será igual a null
        listaNumeros = []; // En cada iteración pondremos una lista vacia en "listaNumeros"

        // Lo siguiente se ejecutará hasta que la cantidad ingresada sea un número
        while (true) {
          print("\nDigita una cantidad de números a dividir:");
          cantidad = int.tryParse(stdin.readLineSync()!);

          if (cantidad == null) {
            print("Error!!!... Debes digitar números");
          } else {
            break;
          }
        }

        print(""); // Imprimimos un salto de línea

        // Haremos una iteración hasta llegar a "cantidad"
        for (int i = 0; i < cantidad; i++) {
          print("Digita el número ${i + 1}:"); // Pedimos que se ingrese un número
          numero = double.tryParse(stdin.readLineSync()!); // Intentaremos convertir ese número a double

          // Evaluamos que lo que se ha ingresado sea un número
          if (numero == null) {
            print("Error!!!... Debes digitar números");
            i--; // Retrocederemos -1 si no se ha ingresado un número
          } else {
            listaNumeros.add(numero); // Si se ha ingresado un número, lo agregamos a la lista
          }
        }

        print("\nLista de números a dividir: $listaNumeros\n"); // Imprimimos la lista de números

        // A continuación haremos la operación de división de cada número de la lista
        // Recorremos todos los elementos de la lista
        for (double num in listaNumeros) {
          if (division == null) {
            division = num; // Si "division" es igual a null le agregamos el primer elemento de la lista
          } else {
            division /= num; // Hacemos la división de lo que hay en "division" - el siguiente elemento de la lista
          }
        }

        if (division == double.infinity) {
          print("Error!!!... División por cero"); // SI "división" es igual a infinito, se nos muestra este error
        } else {
          print("El resultado de la división es: $division"); // Imprimimos el resultado de la división
        }
      } else if (opcion == 5) {
        while (true) {
          // Si la opción ingresada es 5, ejecutamos un  ciclo while()
          // Pedimos que se ingrese un número
          print("\nDigita un número para calcular su porcentaje:");
          numero = double.tryParse(stdin.readLineSync()!);

          // Evalumaos lo que se ha ingresado
          // Si no se ha ingresado un número
          if (numero == null) {
            print("Error!!!.. Debes digitar números"); // En cada iteración se nos muestra este error hasta ingresar un número
          } else {
            porcentaje = numero / 100; // Si se ha ingresado un número, se hará el calculo del porcentaje de dicho número
            print("\nEl porcentaje de $numero es: $porcentaje"); // Imprimimos el resultado en consola
            break; // Rompemos el ciclo
          }
        }
      } else if (opcion == 0) {
        // Si la opción ingresada es 0
        print("\nHasta luego...");
        pass = true; // "pass" será igual a true y se cerrará la ejecución del programa
      } else {
        print("Error!!!... Opción incorrecta"); // Imprimimos un error si la opción ingresada es incorrecta
      }
    } catch (e) {
      // Si se presiona ctrl + D el programa cerrará su ejecución
      print("\nHasta luego...");
      exit(0);
    }
  }
}
