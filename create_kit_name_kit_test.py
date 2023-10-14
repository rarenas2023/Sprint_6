import data#se importa el archivo data
import sender_stand_request#se importa el archivo sender
#se declara una funcion que realizará la asignacion del nombre del kit

def get_kit_body(name):
    current_body = data.kit_body.copy()#se realiza una copia para no alterar los datos
    current_body["name"] = name#se asigna el nuevo nombre que se le envia en la funcion
    return current_body#regresa el nuevo nombre del kit

def positive_assert(name_body):
    new_name_kit = get_kit_body(name_body)#se asigna el nuevo valor para el nombre del kit
    kit_response = sender_stand_request.post_new_client_kit(new_name_kit)#se crea el kit con el nuevo valor
    assert kit_response.status_code == 201#Se valida que el estatus de la respuesta sea 201
    assert kit_response.json()["name"]==name_body#Valida que el nombre que trae el json sea igual al enviado

def negative_assert_code_400(name_body):#funcion de prueba negativa,  recibe el nombre  del kit
    new_name_kit = get_kit_body(name_body)#se asigna el nuevo valor para el nombre del kit
    kit_response = sender_stand_request.post_new_client_kit(new_name_kit)#se crea el kit con el nuevo valor
    assert kit_response.status_code == 400#Se valida que el estatus de la respuesta sea 401
    assert kit_response.json()["name"]==name_body#Valida que el  nombre del json recibido  sea igual al parametro enviado

def test_use_kit_name_1_character_case1():
    positive_assert("number_of_character_is_1")#Petición a la función positive_assert con valores Validos, con un caracter

def test_use_kit_name_supports_511_characters_case2():
    positive_assert(data.kit_body["number_of_characters_is_511"]["name"])#Valida que acepte 511 caracteres,petición positiva

def test_use_kit_name_number_of_characters_is_less_than_the_allowed_case3():
    negative_assert_code_400(data.kit_body["number_of_character_is_less"]["name"])#petición a la función negative_assert_code_400 con valores no válidos

def tests_use_kit_name_exceeds_the_maximum_number_of_characters_512_case4():
    negative_assert_code_400(data.kit_body["number_of_characters_512"]["name"])#petición a la función negative_assert_code_400 con valores no válidos

def test_use_kit_name_supports_special_characters_case5():
    positive_assert(data.kit_body["character_are_special"]["name"])#petición a la función negative_assert_code_400 con valores no válidos

def test_use_kit_name_supports_spaces_are_allowed_case6():
    positive_assert(data.kit_body["spaces_are_allowed"]["name"])#petición a la función   positive_assert con valor válido

def test_use_kit_name_supports_numbers_case7():
    positive_assert(data.kit_body["supports_numbers"]["name"])#petición a la función positive_assert con valor no válido

def test_use_kid_name_Theparameter_is_not_passed_in_the_request_case8():
    negative_assert_code_400(data.kit_body["parameter_is_not_passed_in_the_request"])#petición a la función Negative_assert_code_400 con valor no válido

def test_use_kid_name_The_parameter_different_has_been_passed_case9():
    negative_assert_code_400(data.kit_body["The_parameter_different_has_been_passed"]["name"])#petición a la función Negative_assert_code_400 con valor no válido

