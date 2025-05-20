from app.contacts import add_contact, show_contacts, update_contact, toggle_favorite, show_favorites_contacts, delete_contact
from questionary import select, text, confirm, Choice
from rich.console import Console
from app.utils import ask_id

console = Console()

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

    elif option == 3:
      contact_index = ask_id(contacts)

      if contact_index is None:
        continue
      
      name = text("Qual o nome do contato?", default=contacts[contact_index]["name"]).ask()
      phone = text("Qual o telefone do contato?", default=contacts[contact_index]["phone"]).ask()
      email = text("Qual o e-mail do contato?", default=contacts[contact_index]["email"]).ask()
      favorite = confirm("É um contato favorito?", default=contacts[contact_index]["favorite"]).ask()

      update_contact(contacts, contact_index, name, phone, email, favorite)
    
    elif option == 4:
      contact_index = ask_id(contacts)

      if contact_index is None:
        continue

      toggle_favorite(contacts, contact_index)

    elif option == 5:
      show_favorites_contacts(contacts)

    elif option == 6:
      contact_index = ask_id(contacts)

      if contact_index is None:
        continue

      delete_contact(contacts, contact_index)

    
if __name__ == "__main__":
  main()