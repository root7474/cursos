import "dart:math";
import "dart:io";

void main(List<String> arguments) {
  var nombre;
  var opcion;
  var valor_max;
  var numero_aleatorio;
  var numero_intentos = 0;
  var numero_introducido;
  var pass = false;
  var pass_intentos;

  Random random = new Random();

  print("Bienvenido... Ingresa tu nombre:");
  nombre = stdin.readLineSync();
  
  while (pass == false) {
    print("\n$nombre quieres jugar?: " +
          "\n1.) Sí." +
          "\n2.) No.");

    try{
      opcion = int.parse(stdin.readLineSync()!);

      switch (opcion) {
        case 1:
          while (true) {
            print("\nIntroduce un número:");

            try {
              valor_max = int.parse(stdin.readLineSync()!);

              if (valor_max <= 0) {
                print("\nIntroduce un número mayor que 0");
              } else {
                numero_aleatorio = random.nextInt(valor_max);
                pass_intentos = false;
                break;
              }
            } catch (FormatException) {
              print("\nDebes introducir números que no sean decimales");
            }
          }

          while (pass_intentos == false) {
            for (var i = valor_max; i > 0; i--) {
              print("\nIntroduce tu respuesta:");

              try {
                numero_introducido = int.parse(stdin.readLineSync()!);

                if (numero_introducido == numero_aleatorio) {
                  print("Lo has acertado!!!");
                  break;
                } else if (numero_introducido < numero_aleatorio) {
                  print("El número secreto es mayor, vuelve a intentarlo" +
                        "\nTe quedan ${i - 1} intentos");
                } else {
                  print("El número secreto es menor, vuelve a intentarlo" +
                        "\nTe quedan ${i - 1} intentos");
                }
              } catch (FormatException) {
                print("\nDebes introducir números que no sean decimales" +
                      "\nTe quedan ${i - 1} intentos");
              }
            }

            if (numero_introducido == numero_aleatorio) {
              pass_intentos = true;
            } else {
              print("Perdiste!!!...");
              pass_intentos = true;
            }
          }

          break;
        
        case 2:
          print("\nHasta pronto...");
          pass = true;
          break;
        
        default:
          print("\nError!!!... Opción incorrecta");
          break;
      }
    } catch (FormatException) {
      print("\nDebes introducir números que no sean decimales");
    }
  }
}
