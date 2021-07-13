package classpart;

public class StudentTest {

	public static void main(String[] args) {
		
		  Student ruby = new Student(1, "은영"); 
		  ruby.address = "경기도 안양시";
		  
		  Student jenny = new Student();
		  jenny.studentName = "제니";
		  jenny.studentID = 2;
		  jenny.address = "송파구 문정동";
		  
		  ruby.showStudentInfo(); 
		  jenny.showStudentInfo();
		  
		  System.out.println(ruby);
		  System.out.println(jenny);
		}
		 
	}


