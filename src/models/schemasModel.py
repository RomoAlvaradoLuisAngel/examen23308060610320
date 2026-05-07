from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time, datetime

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str=Field(min_length=8)   
    
class UsuarioSchema(UsuarioLogin):
    nombre: str = Field(min_length=8, max_length=100) 
    

class TareaSchema(BaseModel):
    titulo: str = Field(min_length=1, max_length=200)
    descripcion: Optional[str] = None
    prioridad: str = "media"
    clasificacion: str = "personal"
    
class UsuarioNuevo(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    apellido: str = Field(min_length=3, max_length=100)    
    email: EmailStr      
    password: str = Field(min_length=8)  
    telefono: Optional[str] = Field(None, max_length=15, min_length=10)
    
    activo: bool = True
    fecha_registro: datetime= Field(default_factory=datetime.now)
    ultimo_acceso:  datetime= Field(default_factory=datetime.now)

