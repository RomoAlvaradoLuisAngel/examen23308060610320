from examen23308060610320.src.models.UserModel import UsuarioModel
from examen23308060610320.src.models.schemasModel import UsuarioNuevo, UsuarioLogin
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_usuario(self, nombre, apellido, email, password):
        try:
            #validar datos con el schema
            nuevo_usuario=UsuarioNuevo(nombre=nombre, apellido=apellido, email=email, password=password)
            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario creado correctamente"
        except ValidationError as e:
            #retorna el primer error de validacion encotrado
            return False, e.errors()[0]['msg']
    
    def login(self, email, password):
            try:
                usuario_login = UsuarioLogin(email=email, password=password)
                usuario_encontrado = self.model.iniciar_sesion(usuario_login)
                if usuario_encontrado: 
                    return usuario_encontrado, "Inicio de sesión exitoso"
                else: 
                    return None, "Correo o contraseña incorrectos"
                    
            except Exception as e:
                print("ERROR EN LOGIN:", e)
                return None, f"Error: {str(e)}"