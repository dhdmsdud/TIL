package inheritance;

public class CustomerTest1 {

	public static void main(String[] args) {
		
		Customer customerlee = new Customer();
		customerlee.setCustomerID(001);
		customerlee.setCustomerName("lee");
		customerlee.bonusPoint = 10000;
		
		VIPCustomer customerkim = new VIPCustomer();
		customerkim.setCustomerID(002);
		customerkim.setCustomerName("kim");
		customerkim.bonusPoint = 50000;

		System.out.println(customerkim.showCustomerInfo());
		System.out.println(customerlee.showCustomerInfo());

	}

}
