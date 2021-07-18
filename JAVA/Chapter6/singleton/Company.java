package singleton;

public class Company {

	private static Company instance = new Company();
	
	private Company(){}
	
	public static Company getInstaance() {
		if(instance == null)
			instance = new Company();
		return instance;
	}
}