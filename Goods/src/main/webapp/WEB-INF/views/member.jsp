<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value="${pageContext.request.contextPath}"/>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>회원가입</title>
<style type="text/css">
   body{
      font-size: 12px;
      font-family: sans-serif;
      }
</style>
</head>
<body>
<h2>-회원가입-</h2>
   <form action = "${cpath}/insert.do" method ="post">
      <table border = "0">
         <tr>
            <td>이름</td>
            <td><input type = "text" name = "name"></td>
         </tr>
          <tr>
            <td>아이디</td>
            <td><input type = "text" name = "id"></td>
         </tr>
          <tr>
            <td>이메일</td>
            <td><input type = "text" name = "email"></td>
         </tr>
         <tr>
            <td>전화번호</td>
            <td><input type = "text" name = "phone"></td>
         </tr>
         <tr>
            <td colspan = "2" align = "center">
               <input type="submit" value = "가입">               
               <input type="reset" value = "취소">               
            </td>
         </tr>
      </table>
   </form>
</body>
</html>