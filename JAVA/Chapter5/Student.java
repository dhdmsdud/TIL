package classpart;

public class Student {

	int studentID;
	String studentName;
	int grade;
	String address;
	
	public Student() {}
	
	public Student(int id, String name) {
		studentID = id;
		studentName = name;
	}
	
	public void showStudentInfo() {
		System.out.println(studentName + "," + address);
	}

	/*
	 * public static void main(String[] args) {
	 * 
	 * Student ruby = new Student(); ruby.studentName = "����"; ruby.address =
	 * "��⵵ �Ⱦ��";
	 * 
	 * ruby.showStudentInfo(); }
	 */
	
	public String getStudentName() {
		return studentName;
	}
	
	public void setStudentName(String name) {
		studentName = name;
	}
	
	public static void main(String[]args) {
		Student ruby = new Student();
		ruby.studentName = "����";
		ruby.studentID = 1;
		ruby.address = "new york";
		
		ruby.showStudentInfo();
	}
}
