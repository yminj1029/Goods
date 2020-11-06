package kr.smhrd.model;

import java.util.List;

public interface MemberDAO {

	public List<MemberVO> memberList();
	public int memberInsert(MemberVO vo);
	public MemberVO memberContent(int num);
	public int memberDelete(int num);
	public int memberUpdate(MemberVO vo);
}
