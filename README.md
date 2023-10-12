# Sprint6,Proyecto: Creación de autotests
## Urban Grocers 
Para este proyecto, se tiene una lista de comprobación en el cual se automatizan las pruebas para la creación de un kit, realizando petciones de tipos POST  a la Api.

El proyecto va acompañado de los archivos: 
- 1.-sender_stand_request.py contienen las funciones 
Contiene 3 funciones principales 
--post_new_user(body) --Crea un usuario 
--get_new_user_token()---obtiene el token y da formato el encabezado
- 2.-create_kit_name_kit_test.py--Aqui se realiza la lista de comprobación de las pruebas positivas y negativas
- 3 -data.py Contiene -  los datos en formato json, que son usados en las funciones del punto1
- 4 -configuration.py--Contiene las rutas de los endpoint para consumir las apis

Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
Ejecuta todas las pruebas con el comando pytest desde el archivo create_kit_name_kit_test.py
.
# Lista de comprobación para la generación del Kit

|Descripcion de la lista de comprobación | Valor esperado|Valor recibido|Estatus|
|------ |------|----|----|
|Prueba 1.- permite ingresar el nombre del kit con  1 carecter) |Código de respuesta — 201 El campo "name" en el cuerpo de respuesta coincide con el campo "name" en el cuerpo de solicitud| Código  201|Aprobado|
|Prueba 2.- permite ingresar 511 caracteres caracteres permitidos |Código de respuesta — 201 El campo "name" en el cuerpo de respuesta coincide con el campo "name" en el cuerpo de solicitud|Código 201|Aprobado|
| Prueba 3.-, el número de caracteres es menor a la cantidad permitida (0): kit_body = { "name": "" } | Código de respuesta — 400|Código 201|Fallido|
| Prueba 4.-El número de caracteres es mayor a la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será el siguiente” } |Código de respuesta — 400|Código 201|fallido| 
| Pruebas 5.-Se permiten caracteres especiales: kit_body = { "name": ""№%@"," } |Código de respuesta — 201 El campo "name" en el cuerpo de respuesta coincide con el campo "name" en el cuerpo de solicitud  |Código 201|Aprobado|
|Prueba 6.- Se permiten espacios: kit_body = { "name": " A Aaa " } |Código de respuesta — 201 El campo "name" en el cuerpo de respuesta coincide con el campo "name" en el cuerpo de solicitud|Código201|Aprobado|
|Prueba 7.- Se permiten números: kit_body = { "name": "123" } |Código de respuesta — 201 El campo "name" en el cuerpo de respuesta coincide con el campo "name" en el cuerpo de solicitud|Código201|Aprobado|
|Prueba 8.- El parámetro no se pasa en la solicitud: kit_body = { } |Código de respuesta — 400|Error código de error 500|Fallido|
|Prueba 9.- Se ha pasado un parámetro diferente (número): kit_body = { "name": 123 }|Código de respuesta — 400|Código201|Fallido|

# Resumen de los resultados obtenidos
Las pruebas 1,2,5,6,7, los resultados es esperados son correctos con base al estatus del esperado  vs el valor recibido.

Se identifica bugs en las pruebas 3, 4, 9 el estatus de respuesta regresa 201, versus el esperado un código 400

Para la prueba 8, regresa el siguiente error:
"(test_use_kid_name_Theparameter_is_not_passed_in_the_request_case8)
def test_use_kid_name_Theparameter_is_not_passed_in_the_request_case8():
>       negative_assert_code_400()#petición a la función Negative_assert_code_400 con valor no válido
E       TypeError: negative_assert_code_400() missing 1 required positional argument: 'name_body'"
