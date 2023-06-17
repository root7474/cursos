class GalletaDeJengibre {
  String ? name;
  int ? _edad;
  String ? tipo;
  bool ? volteretas;

  GalletaDeJengibre(this.name, this._edad);
  GalletaDeJengibre.avanzada(this.name, this._edad, {this.tipo, this.volteretas});
  GalletaDeJengibre.sinDatos(this._edad, {this.name, this.tipo, this.volteretas});

  /* void setEdad(int edad) {
    _edad = edad;
  } */

  /* set setEdad(int edad) {
    _edad = edad;
  } */

  /* int getEdad() {
    return _edad!;
  } */

  /* get getEdad {
    return _edad!;
  } */

  // get getEdad => _edad;

  get getName => name;
  set setName(String name) => this.name = name;

  get getEdad => _edad;
  set setEdad(int edad) => _edad = edad;

  get getTipo => tipo;
  set setTipo(String tipo) => this.tipo = tipo;

  get getVolteretas => _aprenderVolteretas();

  bool _aprenderVolteretas() {
    if (_edad! > 20) {
      volteretas == true;
      return true;
    } else {
      return false;
    }
  }
}
