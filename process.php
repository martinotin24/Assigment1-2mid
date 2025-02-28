<!DOCTYPE html>
<html>
<head>
    <title>Processing Data</title>
</head>
<body>
    <h2>Results:</h2>
    <?php
        echo "<h2>Debugging Information</h2>";

        // Obtener parámetros de entrada
        $query_string = http_build_query($_GET);
        echo "<p>Query String: " . htmlspecialchars($query_string) . "</p>";

        // Verificar si el script Python existe
        $python_script = "/var/www/html/data_management.py";
        if (!file_exists($python_script)) {
            echo "<p style='color: red;'>Error: El script de Python no existe.</p>";
            exit;
        }

        // Pasar valores como variable de entorno para evitar problemas con `cgi.FieldStorage()`
        putenv("QUERY_STRING=" . $query_string);

        // Ejecutar el script de Python
        $command = "python3 " . escapeshellarg($python_script) . " 2>&1";
        echo "<p>Executing: <code>$command</code></p>";

        // Capturar la salida y mostrarla en la página
        $output = shell_exec($command);

        echo "<h2>Results:</h2>";
        if ($output) {
            echo "<pre>$output</pre>";
        } else {
            echo "<p style='color: red;'>Error: No se recibió salida del script Python.</p>";
        }
    ?>
</body>
</html>
