package day_03;

public class Oop_test02 {
	public static void main(String[] args) {
		Human hum = new Human();
		System.out.println("flagM "+ hum.flagM +" skill_commnication : " + hum.skill_commnication );
		
		hum.gotoThai(); // Object 
		hum.momstouch(30);
		
		if(hum.flagM)System.out.println("남자");
		else System.out.println("여자");
		
		System.out.println("flagM "+ hum.flagM +" skill_commnication : " + hum.skill_commnication );
	}
}
