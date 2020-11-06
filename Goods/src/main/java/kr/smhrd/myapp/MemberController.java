package kr.smhrd.myapp;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import kr.smhrd.model.MemberDAO;
import kr.smhrd.model.MemberVO;

@Controller
public class MemberController {

	@Autowired
	private MemberDAO memberDAO;
	
	@RequestMapping("/list.do")
	public String memberList(Model model) {
		List<MemberVO> list = memberDAO.memberList();
		model.addAttribute("list",list);
		return "memberList";
	}
	
	@RequestMapping("/insertForm.do")
	public String memberInsertForm() {
		
		return "member";
	} 
	
	@RequestMapping("/insert.do")
	public String memberInsert(MemberVO vo) {
		//System.out.println(vo.toString());
		memberDAO.memberInsert(vo);
		return "redirect:/list.do";
	} 
	
//	@RequestMapping("/content.do")
//	public String memberContent(@RequestParam("num") int aaa) {
//		System.out.println(aaa);
//		return "";
//	} 
	
	@RequestMapping("/content.do")
	public String memberContent(@RequestParam("num") int num, Model model) {
		MemberVO vo = memberDAO.memberContent(num);
		model.addAttribute("vo", vo);
		return "memberContent";
	} 
	
	@RequestMapping("/delete.do")
	public String memberDelete(int num) {
		memberDAO.memberDelete(num);
		System.out.println(num+"삭제성공!");
		return "redirect:list.do";
	} 
	@RequestMapping("/update.do")
	public String memberUpdate(MemberVO vo) {
		memberDAO.memberUpdate(vo);
		System.out.println(vo+"업데이트성공!");
		return "redirect:list.do";
	} 
//	//login.do 에서 겟방식일때 처리
//	@RequestMapping(value="/login.do", method=RequestMethod.GET)
//	public String loginProcess() {
//		return "loginForm";
//	}
//	//login.do에서 포스트방식일 때 처리. 
//	@RequestMapping(value="/login.do", method=RequestMethod.POST)
//	public String loginProcess(MemberVO vo, HttpServletRequest request) {
//		HttpSession session = request.getSession()
//		return "redirect:list.do";
//	} 
}
