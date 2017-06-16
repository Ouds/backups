package com.hwadee.tb.util;

import java.io.IOException;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.web.filter.OncePerRequestFilter;

import com.hwadee.tb.sign.domain.Account;

public class SessionFilter extends OncePerRequestFilter {

	private static Log log = LogFactory.getLog(SessionFilter.class);

	protected void doFilterInternal(HttpServletRequest request,
			HttpServletResponse response, FilterChain filterChain)
			throws ServletException, IOException {
		log.debug("\n\n SessionFilter start ------------ " + request.getRequestURL() + " ------->\n\n");
		
		String uri = request.getRequestURI();
		HttpSession session = request.getSession();
		Account account = (Account) session.getAttribute("account");
		if (null != account || uri.equals(CONSTANT.PROJECT_URI) ||
				uri.indexOf(CONSTANT.PROJECT_SIGN_URI) >= 0 ||
				uri.indexOf(CONSTANT.PROJECT_REGISTER_URI) >= 0 ||
				uri.indexOf(CONSTANT.PROJECT_RES_URI) >= 0) {
			filterChain.doFilter(request, response);
		}
		else {
			if (uri.indexOf(CONSTANT.PROJECT_PAGE_URI) >=0 )
				response.setCharacterEncoding("GBK");
			
			StringBuilder builder = new StringBuilder();
			builder.append("<script charset=\"GBK\" type=\"text/javascript\">");
			builder.append("alert(\"\u4F1A\u8BDD\u5DF2\u8FC7\u671F\uFF0C\u8BF7\u91CD\u65B0\u767B\u5F55\u586B\u62A5\u7CFB\u7EDF\");");
			builder.append("window.top.location='" + CONSTANT.PROJECT_URI + "';");
			builder.append("</script>");
			
			response.getWriter().print(builder.toString());
		}

	}
}