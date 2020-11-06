package kr.smhrd.model;
//번호(num), 이름(name), 아이디(id), 이메일(email), 전번 phone
public class MemberVO {

	private int num;
	private String name;
	private String id;
	private String email;
	private String phone;
	
	public MemberVO() {}

	public int getNum() {
		return num;
	}

	public void setNum(int num) {
		this.num = num;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}

	@Override
	public String toString() {
		return "MemberVO [num=" + num + ", name=" + name + ", id=" + id + ", email=" + email + ", phone=" + phone + "]";
	}
	
	
}
