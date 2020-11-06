package kr.smhrd.model;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class MemberDAOImpl implements MemberDAO {

	@Autowired
	private SqlSessionFactory sqlSessionFactory;
	
	@Override
	public List<MemberVO> memberList() {
		SqlSession session =sqlSessionFactory.openSession();
		List<MemberVO> list = null;
		try {
			list = session.selectList("memberList"); //Sql
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			session.close();
		}
		return list;
	}

	@Override
	public int memberInsert(MemberVO vo) {
		SqlSession session =sqlSessionFactory.openSession();
		int cnt = -1;
		try {
			cnt = session.insert("memberInsert", vo);
			session.commit();
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			session.close();
		}
		return cnt;
	}

	@Override
	public MemberVO memberContent(int num) {
		SqlSession session =sqlSessionFactory.openSession();
		MemberVO vo = null;
		try {
			vo = session.selectOne("memberContent", num);
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			session.close();
		}
		return vo;
	}

	@Override
	public int memberDelete(int num) {
		SqlSession session =sqlSessionFactory.openSession();
		int cnt = -1;
		try {
			cnt = session.delete("memberDelete", num);
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			session.close();
		}
		return cnt;
	}

	@Override
	public int memberUpdate(MemberVO vo) {
		SqlSession session =sqlSessionFactory.openSession();
		int cnt =-1;
		try {
			cnt = session.update("memberUpdate",vo);
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			session.close();
		}
		return cnt;
	}

}
