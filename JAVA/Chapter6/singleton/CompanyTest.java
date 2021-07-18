package singleton;

import java.util.Calendar;

public class CompanyTest {

	public static void main(String[] args) {
		
		Company c1 = Company.getInstaance();
		Company c2 = Company.getInstaance();

		System.out.println(c1);
		System.out.println(c2);
		
		Calendar cal = Calendar.getInstance();
		
		
	}

}
