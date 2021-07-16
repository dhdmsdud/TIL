package cooperation;

public class Taketrans {

	public static void main(String[] args) {
		Student ruby = new Student("ruby", 10000);
		Student jenny = new Student("jenny", 5000);
		
		Bus bus100 = new Bus(100);
		
		ruby.takeBus(bus100);
		ruby.showInfo();
		bus100.showInfo();

		Subway subwayPink = new Subway(1);
		jenny.takeSubway(subwayPink);
		jenny.showInfo();
		subwayPink.showInfo();
	}

}
