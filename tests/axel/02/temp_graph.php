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
   while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
      $array_string_temperature = $array_string_temperature . $row['temperature'] .",";
   }

   $array_string_temperature = trim($array_string_temperature, ",");

   $db->close();



require_once('jpgraph/jpgraph.php');
require_once('jpgraph/jpgraph_line.php');
 //  data
$ydata = explode(',', $array_string_temperature);
// Create the graph. These two calls are always required
$graph = new Graph(800,600);
$graph->SetScale('textlin');
$graph->title->SetFont(FF_FONT2);
$graph->title->Set("Temperature data last 24 hours");
$graph->xaxis->title->Set("Temperature data last 24h");
$graph->yaxis->SetFont(FF_FONT2);
$graph->xaxis->Hide();
// Create the linear plot
$lineplot=new LinePlot($ydata);
$lineplot->SetColor('blue');

// Add the plot to the graph
$graph->Add($lineplot);

// Display the graph
$graph->StrokeCSIM("temp_graph.php");
// $graph->Stroke();

?>

