package array;

public class ForEX {

	public static void main(String[] args) {
		
		String[] strArr = {"java", "python", "c++"};
		
		System.out.println("==�⺻ for��==");
		for (int i=0; i<strArr.length; i++) {
			System.out.println(strArr[i]);
		}

		System.out.println("==string���� ���� for��==");
		for(String s : strArr) {
			System.out.println(s);
		}
		
		System.out.println("==int���� ���� for��==");
		int[] arr = {1,2,3,4,5};
		for (int num : arr)
			System.out.println(num);
	}

}
