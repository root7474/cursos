using System;
using Gtk;

namespace Prueba_GUI_C_Sharp
{
    class Program
    {
        [STAThread]
        public static void Main(string[] args)
        {
            Application.Init();

            var app = new Application("org.Prueba_GUI_C_Sharp.Prueba_GUI_C_Sharp", GLib.ApplicationFlags.None);
            app.Register(GLib.Cancellable.Current);

            var win = new MainWindow();
            app.AddWindow(win);

            win.Show();
            Application.Run();
        }
    }
}
