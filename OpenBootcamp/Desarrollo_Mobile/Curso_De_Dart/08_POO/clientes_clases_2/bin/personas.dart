import 'direccion.dart';

class Personas {
  String? _nombre;
  int? edad;
  Direccion? direccion;
  String? telefono;

  Personas(this._nombre, {this.edad, this.direccion, this.telefono});

  get getNombre => this._nombre;
  set setNombre(String? nombre) => this._nombre = nombre;
}
