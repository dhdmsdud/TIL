package array;

public class ForEX {

	public static void main(String[] args) {
		
		String[] strArr = {"java", "python", "c++"};
		
		System.out.println("==기본 for문==");
		for (int i=0; i<strArr.length; i++) {
			System.out.println(strArr[i]);
		}

		System.out.println("==string형의 향상된 for문==");
		for(String s : strArr) {
			System.out.println(s);
		}
		
		System.out.println("==int형의 향상된 for문==");
		int[] arr = {1,2,3,4,5};
		for (int num : arr)
			System.out.println(num);
	}

}
