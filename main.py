from contacts import add_contact, show_contacts, update_contact, toggle_favorite, show_favorites_contacts, delete_contact
from questionary import select, text, confirm, Choice
from rich.console import Console

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
      show_contacts(contacts)

      contact_id = int(text("Digite o ID do contato que você deseja atualizar").ask())
      contact_index = contact_id - 1

      if contact_id > len(contacts):
        console.print(f"\n[bold yellow]⚠️ Nenhum contato encontrado com este ID![/bold yellow]\n")
        continue
      
      name = text("Qual o nome do contato?", default=contacts[contact_index]["name"]).ask()
      phone = text("Qual o telefone do contato?", default=contacts[contact_index]["phone"]).ask()
      email = text("Qual o e-mail do contato?", default=contacts[contact_index]["email"]).ask()
      favorite = confirm("É um contato favorito?", default=contacts[contact_index]["favorite"]).ask()

      update_contact(contacts, contact_index, name, phone, email, favorite)
    
    elif option == 4:
      show_contacts(contacts)

      contact_id = int(text("Digite o ID do contato que você deseja atualizar").ask())
      contact_index = contact_id - 1

      if contact_id > len(contacts):
        console.print(f"\n[bold yellow]⚠️ Nenhum contato encontrado com este ID![/bold yellow]\n")
        continue

      toggle_favorite(contacts, contact_index)

    elif option == 5:
      show_favorites_contacts(contacts)

    elif option == 6:
      show_contacts(contacts)

      contact_id = int(text("Digite o ID do contato que você deseja deletar").ask())
      contact_index = contact_id - 1

      if contact_id > len(contacts):
        console.print(f"\n[bold yellow]⚠️ Nenhum contato encontrado com este ID![/bold yellow]\n")
        continue

      delete_contact(contacts, contact_id)

    
if __name__ == "__main__":
  main()