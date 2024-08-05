package day_03;
import java.util.Iterator;
import java.util.Scanner;

public class my_def02 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		showDan(sc.nextInt());
		
	}
	
	static void showDan(int a) {
		for (int i = 1; i <= 9; i++) {
			System.out.println(a + " * " +i + " = " + (i * a));
		}
	}
}
