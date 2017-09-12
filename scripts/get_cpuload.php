#!/usr/bin/php

<?php

$output_uptime = exec("uptime"); // get cpuload avarage 1-5-15
$output_uptime = explode(",", $output_uptime);

$cpu_15m = array_pop($output_uptime);
$cpu_05m = array_pop($output_uptime);
$cpu_01m = array_pop($output_uptime);

echo $cpu_01m", "$cpu_05m", "$$cpu_01m";

?>
