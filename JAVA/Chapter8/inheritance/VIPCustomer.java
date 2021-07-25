package inheritance;

public class VIPCustomer extends Customer{

	private double saleRatio;
	private int agentID;
	
	
	public VIPCustomer() {
		customerGrade = "VIP";
		bonusRatio = 0.05;
		saleRatio = 0.1;
	}
	
	public int getAgentID() {
		return agentID;
	}
}


