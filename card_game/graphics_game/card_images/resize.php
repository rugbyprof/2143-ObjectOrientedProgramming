<?php

$path = "./large/";
$dir = scandir($path);

array_shift($dir);
array_shift($dir);

// foreach($dir as $file){

//     $path_parts = pathinfo($file);
//     $ext = $path_parts['extension'];
//     $name = $path_parts['filename'];

//     $input = "{$path}{$file}";
//     $output = "./medium/{$name}.gif";
        
//     echo $output."\n";
//     exec("convert -resize 250x $input $output");
//     $output = "./small/{$name}.gif";
//     echo $output."\n";
//     exec("convert -resize 150x $input $output");
//     $output = "./xsmall/{$name}.gif";
//     echo $output."\n";
//     exec("convert -resize 100x $input $output");
//     $output = "./xxsmall/{$name}.gif";
//     echo $output."\n";
//     exec("convert -resize 75x $input $output");    
// }


exec("convert -resize 76x110! back_black.jpg ./xxsmall/back_black.gif"); 
exec("convert -resize 101x146! back_black.jpg ./xsmall/back_black.gif");
exec("convert -resize 151x219! back_black.jpg ./small/back_black.gif");
exec("convert -resize 251x364! back_black.jpg ./medium/back_black.gif");
//exec("convert -resize 500x back_black.jpg ./large/back_black.gif"); 

exec("convert -resize 76x110! back_red.png ./xxsmall/back_red.gif"); 
exec("convert -resize 101x146! back_red.png ./xsmall/back_red.gif");
exec("convert -resize 151x219! back_red.png ./small/back_red.gif");
exec("convert -resize 251xx364! back_red.png ./medium/back_red.gif");
//exec("convert -resize 500x back_red.png ./large/back_red.gif"); 