package assignment;

public class operationEX3 {

	public static void main(String[] args) {
		int num1 = 10;
		int i = 2;
		boolean value = (((num1 = num1+10) < 10) && ((i = i+2) > 10 ));
		System.out.println(value);
		System.out.println(num1);
		System.out.println(i);
		
		
		int num2 = 10;
		int t = 2;
		boolean value1 = (((num2 = num2+10) < 10) || ((t = t+2) > 10 ));
		System.out.println(value1);
		System.out.println(num2);
		System.out.println(t);

	}

}
