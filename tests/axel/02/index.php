<html>
<<<<<<< HEAD
<head>
<meta http-equiv="cache-control" content="max-age=0" />
<meta http-equiv="cache-control" content="no-cache" />
<meta http-equiv="expires" content="0" />
<meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
<meta http-equiv="pragma" content="no-cache" />
</head>
=======
>>>>>>> upstream/master
<body>
<center>
<br />
<?php

<<<<<<< HEAD
//include 'index.php';

=======
>>>>>>> upstream/master
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
<<<<<<< HEAD
                'Y-m-d H:i:s', 
=======
                'Y-m-d G:i:s', 
>>>>>>> upstream/master
                $utc_time, 
                new DateTimeZone('UTC')
    );

    $local_date = $utc_date;
    $local_date->setTimeZone(new DateTimeZone('Europe/Helsinki'));

<<<<<<< HEAD
    $timestamp_string = $local_date->format('l jS \of F Y H:i'); 
=======
    $timestamp_string = $local_date->format('Y-m-d G:i:s'); 
>>>>>>> upstream/master
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
<<<<<<< HEAD
=======
<br />
>>>>>>> upstream/master
<img src="temp_graph.php?_jpg_csimd=1" />
</center>
</body>
</html>

