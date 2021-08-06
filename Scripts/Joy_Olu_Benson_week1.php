@@ -1,33 +0,0 @@
<?php
    
 $P= "Name"; $Q= " E-mail"; $R="Slack Username";
 define("Biostack", "Medicinal Chemistry");
 define("Twitter Handle", "@JAD_BENSON");
 $U="Hamming Distance";
 $Name= "Joy"; $Slack_Username="@Benson";
        $userNames = ["Joy Olu-Benson",];
      $userMails = ["joyolubenson@yahoo.com",];
    $userSlkname = ["@Benson",];
 $bioStack = ["Medicinal Chemistry",];
    $twitHandle = ["@JAD_BENSON",];
 $hamLength =[strlen("@JAD_BENSON")-strlen("@Benson"),];
 //Basically I have defined, arrayed all inputs and evaluted hamming lenth
 //Next is to define the table to fit data
 
 echo"<table width=1500 cellpadding=1 cellspacing=0 border=1>
<tr>
  <th>".$P."</th><th>".$Q."</th><th>".$R."</th> <th>Biostack</th><th>Twitter Handle</th><th>Hamminglength</th>
</tr>
 <tr>
    <td>".$userNames[0]."</td>
                <td>".$userMails[0]."</td>
             <td>".$userSlkname[0]."</td>
           <td>".$bioStack[0]."</td>
        <td>".$twitHandle[0]."</td>
    <td>".$hamLength[0]."</td>    
 </tr>
  
    </table>";

 
?>