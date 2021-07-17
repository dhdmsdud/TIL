package staticEX;

public class Student {

	private static int serialNum = 10000;
	int studentID;
	String studentName;
	
	public Student( ) {
	serialNum++;
	studentID = serialNum;
	}
	
	public static int getSerialNum() {
		int i = 10; //지역변수
		
		i++;
		System.out.println(i);
		
		//studentName = "은영"; //멤버변수, 인스턴스 변수
		return serialNum; // static변수, 클래스 변수
	}
}
