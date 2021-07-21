package array;

public class StudentTest {

	public static void main(String[] args) {
		
		Student studentlee = new Student(001, "lee");
		studentlee.addSubject("math", 100);
		studentlee.addSubject("english", 90);
		studentlee.showStudentInfo();
		
		Student studentkim = new Student(001, "kim");
		studentkim.addSubject("math", 70);
		studentkim.addSubject("english", 100);
		studentkim.showStudentInfo();
		
	}

}
