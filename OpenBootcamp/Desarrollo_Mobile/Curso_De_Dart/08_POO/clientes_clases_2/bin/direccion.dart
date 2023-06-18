class Direccion {
  int? _numeroVia;
  String? _nombreCalle;
  String? _codPostal;
  String? _ciudad;

  Direccion(this._numeroVia, this._nombreCalle, this._codPostal, this._ciudad);

  get getNumeroVia => this._numeroVia;
  set setNumeroVia(int? numeroVia) => this._numeroVia = numeroVia;

  get getNombreCalle => this._nombreCalle;
  set setNombreCalle(String? nombreCalle) => this._nombreCalle = nombreCalle;

  get getCodPostal => this._codPostal;
  set setCodPostal(String? codPostal) => this._codPostal = codPostal;

  get getCiudad => this._ciudad;
  set setCiudad(String? ciudad) => this._ciudad = ciudad;
}
