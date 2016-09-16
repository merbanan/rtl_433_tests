<?php

class MyDB extends SQLite3
   {
      function __construct()
      {
         $this->open('/home/pi/Scripts/rtl_433/build/src/temperature.db');
      }
   }

   $db = new MyDB();
   if(!$db){
      echo $db->lastErrorMsg();
   } else {
      // echo "Opened database successfully\n";
   }

   $sql =<<<EOF
      SELECT * from temp order by id desc limit 288;
EOF;

   $ret = $db->query($sql);
   $array_string_temperature = "";
   $array_string_timestamp = "";
   while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
     $array_string_temperature[] = $row["temperature"];
     $time_string = date('Y-m-d H:i', strtotime(getLocaltime($row["timestamp"])));
     $array_string_timestamp[] = strtotime($time_string);
   }

   $db->close();

$ydata = array_reverse($array_string_temperature);
$xdata = array_reverse($array_string_timestamp);

 function getLocaltime($utc_time)
  {
    $utc_date = DateTime::createFromFormat(
                'Y-m-d H:i:s', 
                $utc_time, 
                new DateTimeZone('UTC')
    );

    $local_date = $utc_date;
    $local_date->setTimeZone(new DateTimeZone('Europe/Helsinki'));

    $timestamp_string = $local_date->format('Y-m-d H:i:s'); 
    return $timestamp_string;
  }

require_once('jpgraph/jpgraph.php');
require_once('jpgraph/jpgraph_line.php');
require_once('jpgraph/jpgraph_date.php');

// Create the graph. These two calls are always required
$graph = new Graph(800,600);
$graph->SetScale('datlin');
$graph->xaxis->scale->SetTimeAlign(HOURADJ_1);
$graph->xaxis->scale->SetDateFormat('H:i');
$graph->xaxis->SetLabelAngle(90);
$graph->xgrid->Show(true);

// Create the linear plot
$lineplot=new LinePlot($ydata,$xdata);
$lineplot->SetColor('blue');

// Add the plot to the graph
$graph->Add($lineplot);

// Display the graph
$graph->StrokeCSIM("temp_graph.php");

?>

