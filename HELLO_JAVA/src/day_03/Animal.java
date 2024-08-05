package day_03;

public class Animal {
	boolean flagM = true;
	
	void gotoThai() {
		flagM =! flagM;
	}
	
	public static void main(String[] args) {
		Animal ani = new Animal();
		
		System.out.println("2"+ani.flagM);
		
		ani.gotoThai();
		
		System.out.println("2"+ani.flagM);
	}
}
