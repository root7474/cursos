void main(List<String> arguments) {
  final ahora = DateTime.now();
  print(ahora);
  
  final aterrizajeLuna = DateTime(1969, 7, 20, 20, 0, 0);
  final caidaMuroBerlin = DateTime(1989, 11, 9);
  final aterrizajeLuna2 = DateTime.parse("1969-07-20 20:18:04Z");

  print(aterrizajeLuna.day);
  print(aterrizajeLuna.month);
  print(aterrizajeLuna.year);

  final nacimientoDavid = DateTime.parse("1996-02-05");
  nacimientoDavid.weekday == DateTime.monday
                             ? print("David nació un lunes")
                             : print("Nom sé cuándo nací");
  
  print(nacimientoDavid.isUtc);
  print(ahora.isUtc);

  final nacimientoDavid2 = DateTime.utc(1996, 2, 5);
  print(nacimientoDavid2.isUtc);

  print(nacimientoDavid);
  print(nacimientoDavid.toUtc());

  print(nacimientoDavid.timeZoneName);
  print(nacimientoDavid.timeZoneOffset);

  print(aterrizajeLuna.isBefore(nacimientoDavid));

  var diferenciaLunaLuis = nacimientoDavid.difference(aterrizajeLuna);
  print(diferenciaLunaLuis.inDays / 365.25);
}
