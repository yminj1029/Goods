<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<c:set var="cpath" value="${pageContext.request.contextPath}"/>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<script type="text/javascript">
	function listFn(){
		location.href="${cpath}/list.do";
	}
	function deleteFn(num){
		location.href="${cpath}/delete.do?num="+num;
	}

</script>
<body>
- ȸ������ �󼼺��� (View) -
<form action='${cpath}/update.do' method='post'><table>
         <input type='hidden' name='num' value="${vo.num}"/>
         <tr>
         <td>��ȣ</td>
         <td>${vo.num}</td>
         </tr>
         <tr>
         <td>�̸�</td>
         <td>${vo.name}</td>
         </tr>
          <tr>
         <td>���̵�</td>
         <td>${vo.id}</td>
         </tr>
         <tr>
         <td>�̸���</td>
         <td><input type='text' name='email' value='${vo.email}'/></td>
         </tr>
         <tr>
         <td>��ȭ��ȣ</td>
         <td><input type='text' name='phone' value='${vo.phone}'/></td>
         </tr>
         <tr>
         <td align='center' colspan='2'>
         <input type='submit' value='�����ϱ�'/> 
         <input type='button' value='����' onclick="deleteFn(${vo.num})"/>
         <input type='reset' value='���'/> 
         <input type='button' value='����Ʈ' onclick="listFn()"/>
         </tr>
         </table></form>

</body>
</html>