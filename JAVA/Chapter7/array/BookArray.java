package array;

public class BookArray {

	public static void main(String[] args) {
		
		Book[] library = new Book[5];
		
		for (int i=0; i<library.length; i++) {
			System.out.println(library[i]);
		}
		
		library[0] = new Book("���̽��丮1", "�Ȼ�");
		library[1] = new Book("���̽��丮2", "�Ȼ�");
		library[2] = new Book("���̽��丮3", "�Ȼ�");
		library[3] = new Book("���̽��丮4", "�Ȼ�");
		library[4] = new Book("���̽��丮5", "�Ȼ�");

		for (int i=0; i<library.length; i++) {
			library[i].showBookInfo();
		}
	}

}
