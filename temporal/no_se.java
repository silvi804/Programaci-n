public class Cocinero:
{
	// Asociaciones
	private Pizza pizza_1;
	private Pizza pizza_2;
	//Atributos
	private String nombre;
	
	public int darUnidadesProducidas()
	{
	return pizza_1.darCantidadProducida() + pizza_2.darCantidadProducida()
	}
}

public class Pizza
{
	// Atributos
	private String nombre;
	private double costoDeProduccion;
	private int cantidadProducida;
	private double precioVenta;
	//constructor
	public Pizza(string nNombre, double nCosto, double nPrecio) 
	{
		nombre = nNombre;
		costoDeProduccion = nCosto;
		precioVenta = nPrecio;
		cantidadProducida = 0;
	}
	//Métodos
	public void modificarPrecioVenta(double nuevoPrecio)
	{
	precioDeVenta = nuevoPrecio
	}
    public int darCantidadProducida(){
        return cantidadProducida;
    }

	public double darGananciaUnitaria()
	{
	//double resta = precioDeVenta -costoDeProduccion;
	return precioDeVenta -costoDeProduccion;
	}

	public double darGananciaTotal()
	{
	// llama metodo dentro de la clase
	double resta = darGananciaUnitaria()
	return resta * cantidadProducida
	}
}

// creación de objetos

