#🧾 Nota Metodológica

#Fuentes

Los datos utilizados en esta aplicación provienen del graficador y descargador de series del Banco de la República de Colombia (Suameca). 
suameca.banrep.gov.co

#Periodo exacto

Las series cubren los años 2010 a 2024.

#Frecuencia

Los datos tienen una frecuencia anual, es decir, se registra un valor por año para cada variable.

#Transformaciones realizadas

-Todos los valores fueron limpiados para asegurar que los nombres de las columnas no tengan espacios extras ni caracteres no deseados, que cumplieran con el tipo de dato requerido (Float).
- De la columna de fecha (día/mes/año), se transformó para extraer solo el año. En caso de que ya existiera una columna con el año (ANIO), se verificó que esté en formato numérico.
- Los valores de las variables que estaban almacenados como texto (por ejemplo números con coma decimal) se convirtieron a formato numérico.

#Descripción de la aplicación
En esta aplicación llamada Pulso Económico, el usuario encontrará lo siguiente:
- Un filtro interactivo (caja de selección) para escoger una o varias de las variables económicas disponibles: PIB, Desempleo e Inflación.
- Un control deslizante (slider) que permite seleccionar el rango de años del periodo de interés entre 2010 y 2024.
- Una gráfica dinámica que se actualiza automáticamente de acuerdo con las variables y el rango de años seleccionados. Cada opción seleccionada se muestra como una línea distinta en la gráfica, facilitando la comparación visual entre variables.
- Interactividad adicional: al pasar el cursor sobre la gráfica se muestran datos de fecha, valor y nombre de la variable (tooltip), para mayor claridad.

#Supuestos
- Los gráficos reflejan los datos tal como los presenta la fuente, sin modificaciones sustanciales más allá de las transformaciones técnicas mencionadas.
- No se alteran los datos originales (no se realizan estimaciones ni interpolaciones), solo se extrae el valor más reciente del dato mensual de desempleo para cada año, de modo que todas las series se muestran con periodicidad anual. Se asume que ese último valor mensual es representativo del año completo para los propósitos de comparación con las otras variables que ya tienen frecuencia anual.

#🖥️ Link App ->
https://proyec-1.streamlit.app/


