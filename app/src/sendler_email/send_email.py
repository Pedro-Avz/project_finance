import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def enviar_email(usuario, senha, destinatario, assunto, arquivos):
    """
    Envia e-mail com arquivos anexados.
    
    :params usuario: E-mail do remetente.
    :params senha: Senha do e-mail do remetente.
    :params destinatario: E-mail do destinatário.
    :params assunto: Assunto do e-mail.
    :params arquivos: Lista de arquivos para anexar.
    :return: Mensagem indicando se o e-mail foi enviado com sucesso ou não.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = usuario
        msg['To'] = destinatario
        msg['Subject'] = assunto
        
        # anexar os  arquivos para o email
        for arquivo in arquivos:
            if os.path.isfile(arquivo): 
                part = MIMEBase('application', 'octet-stream')
                with open(arquivo, 'rb') as f:
                    part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(arquivo)}')
                msg.attach(part)
            else:
                return f"Erro: O arquivo {arquivo} não foi encontrado."
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(usuario, senha)
        server.sendmail(usuario, destinatario, msg.as_string())
        server.quit()
        return "email enviado com sucesso!"
    
    except smtplib.SMTPAuthenticationError:
        return "Erro de autenticação: Verifique o e-mail e a senha."
    except Exception as e:
        return f"Ocorreu um erro ao enviar e-mail: {str(e)}"
