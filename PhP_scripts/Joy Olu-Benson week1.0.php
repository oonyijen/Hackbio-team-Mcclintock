<?php
    
 $P= "Name"; $Q= " E-mail"; $R="Slack Username";
 define("Biostack", "Medicinal Chemistry");
 define("Twitter Handle", "@BENSON");
 $U="Hamming Distance";
 $Name= "Joy"; $Slack_Username="@Benson,";
        $userNames = ["Joy Olu-Benson",];
      $userMails = ["joyolubenson@yahoo.com",];
    $userSlkname = ["@Benson",];
 $bioStack = ["Medicinal Chemistry",];
    $twitHandle = ["@JAD_BENSON",];
 $hamLength =[strlen("@BENSON")-strlen("@Benson"),];
 //Basically I have defined, arrayed all inputs and evaluted hamming lenth indirectly by manipulating string lengths
 //Next is to define the table
 
echo "$userNames[0],$userMails[0],$userSlkname[0],$bioStack[0],$twitHandle[0], $hamLength[0]";

?>
