import bcrypt
from .databaseModel import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()
        
    def registrar(self, usuario_data):
        #encriptar constarseña
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data.password.encode('utf-8'), salt)
        
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuario (nombre, apellido, email, password, activo) VALUES (%s, %s, %s, %s, %s)",
                (usuario_data.nombre, usuario_data.apellido, usuario_data.email, hashed_pw.decode('utf-8'), 1)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
        
    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE email=%s", (email,))
        user = cursor.fetchone()
        conn.close()
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return user
        return None
    
    def iniciar_sesion(self, usuario_data):
        conn=None
        cursor=None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query= "SELECT * FROM usuario WHERE email=%s"
            cursor.execute(query, (usuario_data.email,))
            usuario_encontrado = cursor.fetchone()
            
            if usuario_encontrado:
                pw_usuario = usuario_data.password.encode('utf-8')
                pw_base_datos = usuario_encontrado['password'].encode('utf-8')
                
                if bcrypt.checkpw(pw_usuario, pw_base_datos):
                    return usuario_encontrado
                return None
            
        except Exception as err:
            print(f"Error en la base de datos: {err}")
            return False
        finally:
            if cursor: cursor.close()
            if conn: conn.close()
            
            