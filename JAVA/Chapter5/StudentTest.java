package classpart;

public class StudentTest {

	public static void main(String[] args) {
		
		  Student ruby = new Student(1, "����"); 
		  ruby.address = "��⵵ �Ⱦ��";
		  
		  Student jenny = new Student();
		  jenny.studentName = "����";
		  jenny.studentID = 2;
		  jenny.address = "���ı� ������";
		  
		  ruby.showStudentInfo(); 
		  jenny.showStudentInfo();
		  
		  System.out.println(ruby);
		  System.out.println(jenny);
		}
		 
	}


