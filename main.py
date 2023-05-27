from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def getNomeEmail():
    nomes = []
    emails = []
    dados = []

    with open('email.csv', 'r', encoding='utf8') as arquivo:
        for info in arquivo:
            dados.append(info.split())
        print(dados)
    
    for item in dados:
        nomes.append(item[0].replace(',',''))
        emails.append(item[1])

    return(nomes, emails)


def getTemplate():
    with open('template.txt', 'r', encoding='utf8') as arquivo:
        template = arquivo.read()
        return Template(template)

def conect(nomes, emails, template):
    s = smtplib.SMTP(host='meu host', port='minha porta')
    s.starttls()
    s.login('seu email','sua senha')

    for nome, email in zip(nomes, emails):
        msg = MIMEMultipart
        mensagem = template.substitute(nome_pessoa = nome.title())

# configuração setup
        msg['from'] = 'seu email'
        msg['to'] = email
        msg['Subject'] = 'mensagem qualquer no titulo'

        msg.attach(MIMEText(mensagem, 'plain'))
        
        s.send_message(msg)

# conect(getNomeEmail()[0], getNomeEmail()[1], getTemplate())