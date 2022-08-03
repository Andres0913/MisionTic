import java.util.Scanner;

public class reto1 {

	private static Scanner leer;

	public static void main(String[] args) {
		leer = new Scanner(System.in);
		int[] elementos = null;
		//Es mas facil con un ArrayList
		int cantElementos=0;
		float promedio=0;
		int maximo=0;
		int minimo=0;

		while(cantElementos==0) {
			//System.out.println("Ingrese la cantidad de elemenos a validar");
			cantElementos=leer.nextInt();
			elementos = new int[cantElementos];
		}

		for (int i = 0; i < elementos.length; i++) {
			elementos[i] = leer.nextInt();
		}
		
		for (int i = 0; i < elementos.length; i++) {
			promedio= promedio+elementos[i];
		}
		promedio = promedio/elementos.length;

		for (int i = 0; i < elementos.length; i++) {
			if(elementos[i]>maximo) {
				maximo=minimo=elementos[i];
			}
		}

		for (int i = 0; i < elementos.length; i++) {
			if(elementos[i]<minimo) {
				minimo=elementos[i];
			}
		}

		System.out.println(clasificacionIRCA((int)promedio));
		System.out.println(clasificacionIRCA(maximo));
		System.out.println(clasificacionIRCA(minimo));

	}

	public static String clasificacionIRCA(int valor){
		String res="";
		
		if(valor>=0 && valor<=5)
			res="SIN RIESGO";
		else if(valor>5 && valor<=14)
			res="BAJO";
		else if(valor>14 && valor<=35)
			res="MEDIO";
		else if(valor>35 && valor<=80)
			res="ALTO";
		else if(valor>80 && valor<=100)
			res="INVIABLE SANITARIAMENTE";

		return res;
	}
}
