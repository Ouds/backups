package com.dingdongquan.pr;  
  
  
import java.io.BufferedReader;  
import java.io.InputStreamReader;  
import java.net.URL;  
import java.net.URLConnection;  
  
public class PageRank {  
    /* 
     * public static void main(String[] args)throws Exception { String url = 
     * "http://www.safe-drive.com/"; 
     *  
     * System.out.println(getPageRank(url)); } 
     */  
  
    public static String getPageRank(String url) {  
        String responseFromServer = "";  
        CheckSum cs = new CheckSum();  
        String s = cs.CalculateChecksum(url);  
  
        try {  
            URL openurl = new URL(  
                    "http://www.google.cn/search?client=navclient-auto&features=Rank:&q=info:"  
                            + url + "&ch=" + s);  
            URLConnection HttpWReq = openurl.openConnection();  
  
            HttpWReq.setRequestProperty("Accept", "*/*");  
            HttpWReq.setRequestProperty("User-Agent",  
                    "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)");  
  
            BufferedReader r = new BufferedReader(new InputStreamReader(  
                    HttpWReq.getInputStream()));  
  
            while ((s = r.readLine()) != null) {  
                // System.out.println(s);  
                responseFromServer = s;  
            }  
            r.close();  
        } catch (Exception e) {  
            e.printStackTrace();  
        }  
  
        String[] sp = responseFromServer.split(":");  
        String lbValue = null;  
        if (sp.length == 3)  
            lbValue = "查询成功! PR = " + sp[2].toString();  
        else  
            lbValue = "查询失败!";  
        return (lbValue);  
    }  
  
    public static void main(String[] args) {  
        System.out.println(new PageRank().getPageRank("http://sports.sina.com.cn"));  
    }  
} 