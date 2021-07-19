package array;

public class ObjectCopy2 {

	public static void main(String[] args) {
		
		Book[] bookArray1 = new Book[3];
		Book[] bookArray2 = new Book[3];
		
		bookArray1[0] = new Book("toystory1", "pixar");
		bookArray1[1] = new Book("toystory2", "pixar");
		bookArray1[2] = new Book("toystory3", "pixar");
		
		bookArray2[0] = new Book();
		bookArray2[1] = new Book();
		bookArray2[2] = new Book();
		
		
		for (int i=0; i<bookArray1.length; i++) {
			bookArray2[i].setAuthor(bookArray1[i].getAuthor());
			bookArray2[i].setBookname(bookArray1[i].getBookname());
		}
		
		bookArray1[0].setBookname("¶óÇ¬Á©");
		bookArray1[0].setAuthor("µðÁî´Ï");
		
		System.out.println("===±íÀºº¹»ç bookArray1===");
		for (int i=0; i<bookArray1.length; i++) {
			bookArray1[i].showBookInfo();
		}
		
		System.out.println("===±íÀºº¹»ç bookArray2===");
		for (int i=0; i<bookArray2.length; i++) {
			bookArray2[i].showBookInfo();
		}
	}
	

}
