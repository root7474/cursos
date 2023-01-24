// Autor: David Rodríguez
string? nombre;
string? telefono;
string? direccion;
string? email;
int nuevoClienteInt;
bool nuevoClienteBool;

Console.Write("\nDigita tu nombre: ");
nombre  = Console.ReadLine();

Console.Write("Digita tu teléfono: ");
telefono  = Console.ReadLine();

Console.Write("Digita tu dirección: ");
direccion = Console.ReadLine();

Console.Write("Digita tu email: ");
email = Console.ReadLine();

Console.Write("Eres nuevo cliente? (1 si) (0 no): ");
nuevoClienteInt = int.Parse(Console.ReadLine()!);
nuevoClienteBool = Convert.ToBoolean(nuevoClienteInt);

Cliente cliente = new Cliente(nombre!, telefono!, direccion!, email!, nuevoClienteBool);
Console.WriteLine(cliente.ToString());

public struct Cliente
{
    public Cliente(string nombre, string telefono, string direccion, string email, 
                   bool nuevoCliente)
    {
        Nombre = nombre;
        Telefono = telefono;
        Direccion = direccion;
        Email = email;
        NuevoCliente = nuevoCliente;
    }

    public string Nombre { get; set; }
    public string Telefono { get; set; }
    public string Direccion { get; set; }
    public string Email { get; set; }
    public bool NuevoCliente { get; set; }

    public override string ToString() {
        string mensaje = $"\nNombre: {Nombre} \nTeléfono: {Telefono} \nDirección: {Direccion} \nEmail: {Email} \nNuevo cliente?: {NuevoCliente}\n";
        return mensaje;
    }
}
