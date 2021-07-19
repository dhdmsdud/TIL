package array;

public class BookArray {

	public static void main(String[] args) {
		
		Book[] library = new Book[5];
		
		for (int i=0; i<library.length; i++) {
			System.out.println(library[i]);
		}
		
		library[0] = new Book("토이스토리1", "픽사");
		library[1] = new Book("토이스토리2", "픽사");
		library[2] = new Book("토이스토리3", "픽사");
		library[3] = new Book("토이스토리4", "픽사");
		library[4] = new Book("토이스토리5", "픽사");

		for (int i=0; i<library.length; i++) {
			library[i].showBookInfo();
		}
	}

}
