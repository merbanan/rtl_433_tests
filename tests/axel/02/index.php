<html>
<body>
<center>
<br />
<?php

   class MyDB extends SQLite3
   {
      function __construct()
      {
         $this->open('/home/pi/Scripts/rtl_433/build/src/temperature.db');
      }
   }

  function getLocaltime($utc_time)
  {
    $utc_date = DateTime::createFromFormat(
                'Y-m-d G:i:s', 
                $utc_time, 
                new DateTimeZone('UTC')
    );

    $local_date = $utc_date;
    $local_date->setTimeZone(new DateTimeZone('Europe/Helsinki'));

    $timestamp_string = $local_date->format('Y-m-d G:i:s'); 
    return $timestamp_string;
  }


   $db = new MyDB();
   if(!$db){
      echo $db->lastErrorMsg();
   } else {
      // echo "Opened database successfully\n";
   }

   $sql =<<<EOF
      SELECT * from temp order by id desc limit 1;
EOF;

   $ret = $db->query($sql);
   while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
      echo getLocaltime($row['timestamp']) ." : " . round($row['temperature'],1) . "&deg;C";
   }
   // echo "Operation done successfully\n";
   $db->close();

?>
<br />
<br />
<img src="temp_graph.php?_jpg_csimd=1" />
</center>
</body>
</html>

