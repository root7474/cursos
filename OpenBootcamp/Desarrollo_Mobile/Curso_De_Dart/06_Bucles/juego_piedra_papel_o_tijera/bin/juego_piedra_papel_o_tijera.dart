import "dart:math";
import "dart:io";

void main(List<String> arguments) {
  var user_name_1;
  var user_wins_1;
  var user_name_2;
  var user_wins_2;
  var computer_wins;
  var eleccion_usuario_1;
  var eleccion_usuario_2;
  var eleccion_ordenador;
  var intentos;
  var pass = false;
  var menu;
  var opciones = ["piedra", "papel", "tijeras"];

  Random random = new Random();

  print("Bienvenido... Digita tu nombre:");
  user_name_1 = stdin.readLineSync();


  while (pass == false) {
    try {
      print("\n$user_name_1 elige una opción:\n"
            "\n1.) Jugar contra la IA"
            "\n2.) Jugar contra un amigo"
            "\n0.) Salir");
      menu = int.parse(stdin.readLineSync()!);

      switch (menu) {
        case 1:
          user_wins_1 = 0;
          computer_wins = 0;

          print("\nCuantos intentos deseas agregar?:");
          intentos = int.parse(stdin.readLineSync()!);

          for (var i = 0; i < intentos; i++) {
            print("\nIntento número ${i + 1}. $user_name_1 elige piedra, papel o tijeras.");
            eleccion_usuario_1 = stdin.readLineSync()!.toLowerCase();
            
            if (!opciones.contains(eleccion_usuario_1)) {
              print("Error!!!... $user_name_1 elige entre piedra, papel o tijeras");
              i--;
              continue;
            }

            eleccion_ordenador = opciones[random.nextInt(opciones.length)];
            print("\nLa IA a elegido: $eleccion_ordenador");

            if (eleccion_usuario_1 == "piedra" && eleccion_ordenador == "tijeras") {
              user_wins_1++;
              print("$user_name_1 has ganado +1 puntos");
              print("$user_name_1: $user_wins_1 vs IA: $computer_wins");
            } else if (eleccion_usuario_1 == "papel" && eleccion_ordenador == "piedra") {
              user_wins_1++;
              print("$user_name_1 has ganado +1 puntos");
              print("$user_name_1: $user_wins_1 vs IA: $computer_wins");
            } else if (eleccion_usuario_1 == "tijeras" && eleccion_ordenador == "papel") {
              user_wins_1++;
              print("$user_name_1 has ganado +1 puntos");
              print("$user_name_1: $user_wins_1 vs IA: $computer_wins");
            } else if (eleccion_usuario_1 == eleccion_ordenador) {
              print("Empate");
              print("$user_name_1: $user_wins_1 vs IA: $computer_wins");
            } else {
              computer_wins++;
              print("Has perdido");
              print("$user_name_1: $user_wins_1 vs IA: $computer_wins");
            }
          }

          print("\nPuntos de $user_name_1: $user_wins_1" +
                "\nPuntos de la IA: $computer_wins");

          if (computer_wins > user_wins_1) {
            print("\nHa ganado la IA");
          } else if (computer_wins == user_wins_1) {
            print("\nEmpate");
          } else {
            print("\n$user_name_1 has ganado!!!");
          }

          break;

        case 2:
          user_wins_1 = 0;
          user_wins_2 = 0;

          print("Jugador 2 digita tu nombre:");
          user_name_2 = stdin.readLineSync();

          print("\nCuantos intentos deseas agregar?:");
          intentos = int.parse(stdin.readLineSync()!);

          for (var i = 0; i < intentos; i++) {
            print("\nIntento número ${i + 1}."
                  "\nElige $user_name_1: Piedra, papel o tijeras.");
            eleccion_usuario_1 = stdin.readLineSync()!.toLowerCase();

            print("\nElige $user_name_2: Piedra, papel o tijeras.");
            eleccion_usuario_2 = stdin.readLineSync()!.toLowerCase();

            if (!opciones.contains(eleccion_usuario_1)) {
              print("\nError!!!... $user_name_1 elige entre piedra, papel o tijeras");
              i--;
              continue;
            } else if (!opciones.contains(eleccion_usuario_2)) {
              print("\nError!!!... $user_name_2 elige entre piedra, papel o tijeras");
              i--;
              continue;
            }

            /* eleccion_ordenador = opciones[random.nextInt(2)];
            print("\nLa IA a elegido: $eleccion_ordenador"); */

            if (eleccion_usuario_1 == "piedra" && eleccion_usuario_2 == "tijeras") {
              user_wins_1++;
              print("\n$user_name_1 has ganado +1 puntos");
              print("$user_name_1: $user_wins_1 vs $user_name_2: $user_wins_2");
            } else if (eleccion_usuario_1 == "papel" && eleccion_usuario_2 == "piedra") {
              user_wins_1++;
              print("\n$user_name_1 has ganado +1 puntos");
              print("$user_name_1: $user_wins_1 vs $user_name_2: $user_wins_2");
            } else if (eleccion_usuario_1 == "tijeras" && eleccion_usuario_2 == "papel") {
              user_wins_1++;
              print("\n$user_name_1 has ganado +1 puntos");
              print("$user_name_1: $user_wins_1 vs $user_name_2: $user_wins_2");
            } else if (eleccion_usuario_2 == "piedra" && eleccion_usuario_1 == "tijeras") {
              user_wins_2++;
              print("\n$user_name_2 has ganado +1 puntos");
              print("$user_name_1: $user_wins_1 vs $user_name_2: $user_wins_2");
            } else if (eleccion_usuario_2 == "papel" && eleccion_usuario_1 == "piedra") {
              user_wins_2++;
              print("\n$user_name_2 has ganado +1 puntos");
              print("$user_name_1: $user_wins_1 vs $user_name_2: $user_wins_2");
            } else if (eleccion_usuario_2 == "tijeras" && eleccion_usuario_1 == "papel") {
              user_wins_2++;
              print("\n$user_name_2 has ganado +1 puntos");
              print("$user_name_1: $user_wins_1 vs $user_name_2: $user_wins_2");
            } else {
              print("\nEmpate");
              print("$user_name_1: $user_wins_1 vs $user_name_2: $user_wins_2");
            }
          }

          print("\nPuntos de $user_name_1: $user_wins_1"
                "\nPuntos de $user_name_2: $user_wins_2");

          if (user_wins_2 > user_wins_1) {
            print("\n$user_name_2 has ganado!!!");
          } else if (user_wins_2 == user_wins_1) {
            print("\nEmpate");
          } else {
            print("\n$user_name_1 has ganado!!!");
          }

          break;

        case 0:
          print("\nHasta pronto...");
          pass = true;
          break;
        
        default:
          print("\nError!!!... Opción incorrecta");
          break;
      }
    } catch (FormatException) {
      print("\nError!!!... Solo debes ingresar números que no sean decimales");
    }
  }
}
