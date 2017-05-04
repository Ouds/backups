package com.dingdongquan.pr;  
  
/// <summary>  
/// Google PageRank的Checksum算法。  
///   
///   
///   
/// </summary>  
public class CheckSum {  
  
  public CheckSum()  
  {  
  }  
  
  long GOOGLE_MAGIC = 0xE6359A60l;  
  
  private long zeroFill(long a, long b)  
  {  
      long z = 0x80000000l;  
      if ((z & a)!=0)  
      {  
          a = (a >> 1);  
          a &= (~z);  
          a |= 0x40000000;  
          a = (a >> (b - 1));  
      }  
      else  
      {  
          a = (a >> b);  
      }  
        
      return a;  
  }  
  
  private long[] mix(long a, long b, long c)  
  {  
      a -= b;  
      a &= 0xFFFFFFFFl;  
      a -= c;  
      a &= 0xFFFFFFFFl;  
      
      a ^= (zeroFill(c, 13));  
  
      b -= c;   
      b &= 0xFFFFFFFFl;  
      b -= a;  
      b &= 0xFFFFFFFFl;  
      b ^= (a << 8);  
      b &= 0xFFFFFFFFl;  
        
      c -= a;   
      c &= 0xFFFFFFFFl;  
      c -= b;   
      c &= 0xFFFFFFFFl;  
      c ^= (zeroFill(b, 13));  
        
      a -= b;  
      a &= 0xFFFFFFFFl;  
      a -= c;   
      a &= 0xFFFFFFFFl;  
      a ^= (zeroFill(c, 12));  
        
      b -= c;  
      b &= 0xFFFFFFFFl;  
      b -= a;  
      b &= 0xFFFFFFFFl;  
      b ^= (a << 16);  
      b &= 0xFFFFFFFFl;  
        
      c -= a;  
      c &= 0xFFFFFFFFl;  
      c -= b;   
      c &= 0xFFFFFFFFl;  
      c ^= (zeroFill(b, 5));  
        
      a -= b;  
      a &= 0xFFFFFFFFl;  
      a -= c;  
      a &= 0xFFFFFFFFl;  
      a ^= (zeroFill(c, 3));  
        
      b -= c;  
      b &= 0xFFFFFFFFl;  
      b -= a;  
      b &= 0xFFFFFFFFl;  
      b ^= (a << 10);  
      b &= 0xFFFFFFFFl;  
        
      c -= a;  
      c &= 0xFFFFFFFFl;  
      c -= b;  
      c &= 0xFFFFFFFFl;  
      c ^= (zeroFill(b, 15));  
      
//      a &= 0xFFFFFFFFl;  
//    b &= 0xFFFFFFFFl;  
//    c &= 0xFFFFFFFFl;  
//    System.out.println("a:@" + a);  
//    System.out.println("b:@" + b);  
//    System.out.println("c:@" + c);  
      long[] ret = { a, b, c };  
      return(ret) ;  
  }  
  
  private long GoogleCH(long[] url, int length, long init)  
  {  
      if (length == 0)  
      {  
          length = (int)url.length;  
      }  
      long a, b;  
      a = b = 0x9E3779B9l;  
      long c = init;  
  
  
      int k = 0;  
      int len = length;  
      long[] m_mix = new long[3];  
        
  
//      System.out.println("a:"+a);  
//      System.out.println("b:"+b);  
//      System.out.println("c:"+c);  
        
        
      while (len >= 12)  
      {  
          a += url[k + 0];  
          //System.out.println("a1:"+a);  
          a += ((long)url[k + 1]) << 8 ;  
          //System.out.println("a2:"+a);  
  
          a += (((long)url[k + 2]) << 16);  
          //System.out.println("a3:"+a);  
          a += (((long)url[k + 3]) << 24);  
          //System.out.println("a4:"+a);  
          a &= 0xFFFFFFFFl;  
          b += (url[k + 4] + (long)(url[k + 5] << 8) + (long)(url[k + 6] << 16) + (long)(url[k + 7] << 24));  
          c += (url[k + 8] + (long)(url[k + 9] << 8) + (long)(url[k + 10] << 16) + (long)(url[k + 11] << 24));  
            
          b &= 0xFFFFFFFFl;  
          c &= 0xFFFFFFFFl;  
            
//          System.out.println("a:"+a);  
//          System.out.println("b:"+b);  
//          System.out.println("c:"+c);  
            
          m_mix = mix(a, b, c);  
          a = m_mix[0]; b = m_mix[1]; c = m_mix[2];  
//          a &= 0xFFFFFFFFl;  
//        b &= 0xFFFFFFFFl;  
//        c &= 0xFFFFFFFFl;  
          k += 12;  
          len -= 12;  
  
      }  
  
      //System.out.println("a:"+a);  
      //System.out.println("b:"+b);  
      //System.out.println("c:"+c);  
  
      c += length;  
  
      //System.out.println("len:"+len);  
      switch (len)              /* all the case statements fall through */  
      {  
          case 11:  
              {  
                  c += (long)(url[k + 10] << 24);  
                  c &= 0xFFFFFFFFl;  
                  c += (long)(url[k + 9] << 16);  
                  c &= 0xFFFFFFFFl;  
                  c += (long)(url[k + 8] << 8);  
                  c &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 7] << 24);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 6] << 16);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 5] << 8);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 4]);  
                  b &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 3] << 24);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 2] << 16);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 1] << 8);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 0]);  
                  a &= 0xFFFFFFFFl;  
                  break;  
              }  
          case 10:  
              {  
                  c += (long)(url[k + 9] << 16);  
                  c &= 0xFFFFFFFFl;  
                  c += (long)(url[k + 8] << 8);  
                  c &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 7] << 24);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 6] << 16);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 5] << 8);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 4]);  
                  b &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 3] << 24);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 2] << 16);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 1] << 8);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 0]);  
                  a &= 0xFFFFFFFFl;  
                  break;  
              }  
          case 9:  
              {  
                  c += (long)(url[k + 8] << 8);  
                  c &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 7] << 24);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 6] << 16);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 5] << 8);  
                  b &= 0xFFFFFFFFl;                    
                  b += (long)(url[k + 4]);  
                  b &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 3] << 24);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 2] << 16);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 1] << 8);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 0]);  
                  a &= 0xFFFFFFFFl;  
                  break;  
              }  
          /* the first byte of c is reserved for the length */  
          case 8:  
              {  
                  b += (long)(url[k + 7] << 24);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 6] << 16);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 5] << 8);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 4]);  
                  b &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 3] << 24);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 2] << 16);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 1] << 8);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 0]);  
                  a &= 0xFFFFFFFFl;  
                  break;  
              }  
          case 7:  
              {  
                  b += (long)(url[k + 6] << 16);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 5] << 8);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 4]);  
                  b &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 3] << 24);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 2] << 16);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 1] << 8);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 0]);  
                  a &= 0xFFFFFFFFl;  
                  break;  
              }  
          case 6:  
              {  
                  b += (long)(url[k + 5] << 8);  
                  b &= 0xFFFFFFFFl;  
                  b += (long)(url[k + 4]);  
                  b &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 3] << 24);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 2] << 16);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 1] << 8);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 0]);  
                  a &= 0xFFFFFFFFl;  
                  break;  
              }  
          case 5:  
              {  
                  b += (long)(url[k + 4]);  
                  b &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 3] << 24);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 2] << 16);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 1] << 8);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 0]);  
                  a &= 0xFFFFFFFFl;  
                  break;  
              }  
          case 4:  
              {  
                  a += (long)(url[k + 3] << 24);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 2] << 16);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 1] << 8);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 0]);  
                  a &= 0xFFFFFFFFl;  
                  break;  
              }  
          case 3:  
              {  
                  a += (long)(url[k + 2] << 16);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 1] << 8);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 0]);  
                  a &= 0xFFFFFFFFl;  
                  //System.out.println("a:!!!!"+a);  
                  break;  
              }  
          case 2:  
              {  
                  a += (long)(url[k + 1] << 8);  
                  a &= 0xFFFFFFFFl;  
                  a += (long)(url[k + 0]);  
                  a &= 0xFFFFFFFFl;  
                  break;  
              }  
          case 1:  
              {  
                  a += (long)(url[k + 0]);  
                  a &= 0xFFFFFFFFl;  
                  break;  
              }  
          /* case 0: nothing left to add */  
      }  
      m_mix = mix(a, b, c);  
      /*-------------------------------------------- report the result */  
      return m_mix[2];  
  }  
  
  private long GoogleCH(String url, int length)  
  {  
      long[] m_urlint = new long[url.length()];  
        
      for (int i = 0; i < url.length(); i++)  
      {  
          m_urlint[i] = url.charAt(i);  
          //System.out.println("m_urlint[i]:"+m_urlint[i]);  
      }  
      return GoogleCH(m_urlint, length, GOOGLE_MAGIC);  
  }  
  
  private long GoogleCH(String sURL)  
  {  
      return GoogleCH(sURL, 0);  
  }  
  private long GoogleCH(long[] url, int length)  
  {  
      return GoogleCH(url, length, GOOGLE_MAGIC);  
  }  
  
  private long[] c32to8bit(long[] arr32)  
  {  
      long[] arr8 = new long[arr32.length * 4 + 3];  
  
      for (int i = 0; i < arr32.length; i++)  
      {  
          for (int bitOrder = i * 4; bitOrder <= i * 4 + 3; bitOrder++)  
          {  
              arr8[bitOrder] = arr32[i] & 255;  
              arr32[i] = zeroFill(arr32[i], 8);  
          }  
      }  
      return arr8;  
  }  
  
  //新算法,ToolBar 版本>>=2.0.114  
  public String CalculateChecksum(String sURL)  
  {  
      long ch = GoogleCH("info:" + sURL);  
      //System.out.println("ch:"+ch);  
        
      ch = (((ch / 7) << 2) | (((int)(ch % 13)) & 7));  
      //System.out.println("ch2:"+ch);  
      long[] prbuf = new long[20];  
      prbuf[0] = ch;  
      for (int i = 1; i < 20; i++)  
      {  
          prbuf[i] = prbuf[i - 1] - 9;  
          //System.out.println("prbuf[i]:"+prbuf[i]);  
      }  
        
      ch = GoogleCH(c32to8bit(prbuf), 80);  
      return "6"+ch;  
  }  
  
  //老算法,ToolBar 版本<2.0.114  
  /*public String CalculateChecksumOld(String sURL) 
  { 
      int ch = GoogleCH("info:" + sURL); 
 
      String CalculateChecksum = "6" + ((ch)); 
      return CalculateChecksum; 
  }*/  
}  