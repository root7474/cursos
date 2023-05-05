from cx_Freeze import setup, Executable

def main():
    
    """ setup(name="Juego Piedra Papel o Tijeras",
          version="0.1",
          description="Juega a piedra, papel o tijeras contra la IA",
          exec) """
    setup(name="Juego Piedra Papel o Tijeras",
          version="0.1",
          description="Juega a piedra, papel o tijeras contra la IA",
          executables = [Executable("/home/root7474/Documents/Cursos/Proyectos_Python/Juego_Piedra_Papel_Tijeras/Main.py")])

if __name__ == "__main__":
    main()
