from contacts import add_contact, show_contacts
from questionary import select, text, confirm, Choice

contacts = []

def main() -> None:
  """
  Executa o menu principal da aplicação de contatos.

  Mostra um menu interativo em loop, permitindo ao usuário
  escolher entre várias operações como adicionar, visualizar,
  editar e apagar contatos. O loop continua até o usuário
  selecionar a opção "Sair".
  """
  while True:
    option = select(
      "O que você deseja fazer?",
        choices=[
          Choice("Adicionar um contato", value=1),
          Choice("Visualizar contatos", value=2),
          Choice("Editar um contato", value=3),
          Choice("Gerenciar favoritos", value=4),
          Choice("Ver favoritos", value=5),
          Choice("Apagar um contato", value=6),
          Choice("Sair", value=0)
        ]
      ).ask()
    
    if option == 0:
      break

    elif option == 1:
      name = text("Qual o nome do contato?").ask()
      phone = text("Qual o telefone do contato?").ask()
      email = text("Qual o e-mail do contato?").ask()
      favorite = confirm("É um contato favorito?").ask()

      add_contact(contacts, name, phone, email, favorite)

    elif option == 2:
      show_contacts(contacts)

if __name__ == "__main__":
  main()