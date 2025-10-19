"""Application Configuration Module"""
from pydantic import ConfigDict
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings and configuration"""
    
    # Application settings
    app_name: str = "Notification Backend"
    app_version: str = "0.1.0"
    debug: bool = False
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000
    
    # SMTP settings (Mailgun configuration)
    smtp_host: Optional[str] = None
    smtp_port: int = 587
    smtp_username: Optional[str] = None
    smtp_password: Optional[str] = None
    smtp_use_tls: bool = True
    
    # Email settings
    email_from: str = "notification@neudiagnostics.dadames.tech"
    email_from_name: str = "neudiagnostics"
    
    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=False
    )


# Create a global settings instance
settings = Settings()
