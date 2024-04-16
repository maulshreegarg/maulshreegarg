class Solution {
    public boolean isValid(String s) {
       char stack[]=new char[s.length()];
       int t=-1;
       for(int i=0;i<s.length();i++)
       {
        if("({[".indexOf(s.charAt(i))!=-1)
        {
            t++;
            stack[t]=s.charAt(i);

        }
        else if(')'==s.charAt(i)&&t!=-1&&'('==stack[t])
        {
            t=t-1;
        }
        else if('}'==s.charAt(i)&&t!=-1&&'{'==stack[t])
         {
            t=t-1;
        }
        else if(']'==s.charAt(i)&&t!=-1&&'['==stack[t])
         {
            t=t-1;
        }
        else
        {
            return false;
        }
       }
       if(s.length()!=1&&t==-1)
       { 
       return true;
       }
       else
       return false;
    }
}
