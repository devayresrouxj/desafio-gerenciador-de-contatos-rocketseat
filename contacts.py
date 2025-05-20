from rich.console import Console
from tabulate import tabulate

console = Console()

def add_contact(contacts: list, name: str, phone: str, email: str, favorite: bool = False) -> None:
  """
  Adiciona um novo contato à lista de contatos.

  Valida se os campos obrigatórios (nome, telefone e e-mail) foram preenchidos.
  Exibe mensagens de erro ou sucesso no terminal utilizando a biblioteca Rich.

  Args:
      contacts (List[Dict[str, Any]]): Lista onde os contatos são armazenados.
      name (str): Nome do contato.
      phone (str): Número de telefone do contato.
      email (str): Endereço de e-mail do contato.
      favorite (bool, opcional): Indica se o contato é favorito. Padrão é False.

  Returns:
      None
  """
  if not name.strip() or not phone.strip() or not email.strip():
    console.print(f"\n[bold yellow]⚠️ Todos os campos são obrigatórios![/bold yellow]\n")
    return

  contact = {
    "name": name,
    "phone": phone,
    "email": email,
    "favorite": favorite
  }
  contacts.append(contact)
  console.print(f"\n[bold green]✅ Contato '{name}' adicionado com sucesso![/bold green]\n")
  return

def show_contacts(contacts: list) -> None:
  """
  Exibe a lista de contatos.

  Args:
    contacts (List[Dict[str, Any]]): Lista onde os contatos são armazenados.

  Returns:
    None
  """
  if not contacts:
    console.print(f"\n[bold yellow]⚠️ A lista de contatos está vazia![/bold yellow]\n")
    return

  contacts_formatted = []

  for idx, contact in enumerate(contacts, start=1):
    contact_formated = {
      "id": idx,
      "name": contact["name"],
      "phone": contact["phone"],
      "email": contact["email"],
      "favorite": "✓" if contact["favorite"] else ""
    }
    
    contacts_formatted.append(contact_formated)  
  
  colalign = ["left"] * len(contacts_formatted[0])

  print(tabulate(contacts_formatted, headers="keys", tablefmt="grid", colalign=colalign))
  return

def update_contact(contacts: list, id: int, name: str, phone: str, email: str, favorite: bool) -> None:
  """
  Atualiza um contato da lista de contatos.

  Valida se os campos obrigatórios (nome, telefone e e-mail) foram preenchidos.
  Exibe mensagens de erro ou sucesso no terminal utilizando a biblioteca Rich.

  Args:
      contacts (List[Dict[str, Any]]): Lista onde os contatos são armazenados.
      id (int): ID do contato a ser editado.
      name (str): Nome do contato.
      phone (str): Número de telefone do contato.
      email (str): Endereço de e-mail do contato.
      favorite (bool, opcional): Indica se o contato é favorito. Padrão é False.

  Returns:
      None
  """
  if not name.strip() or not phone.strip() or not email.strip():
    console.print(f"\n[bold yellow]⚠️ Todos os campos são obrigatórios![/bold yellow]\n")
    return

  contacts[id]["name"] = name
  contacts[id]["phone"] = phone
  contacts[id]["email"] = email
  contacts[id]["favorite"] = favorite

  console.print(f"\n[bold green]✅ Contato atualizado com sucesso![/bold green]\n")
  return

def toggle_favorite(contacts: list, id: int) -> None:
  """
  Marca ou Desmarca um contato como favorito.

  Se o contato já estiver marcado ele será desmarcado, se estiver desmarcado
  ele será marcado.

  Args:
      contacts (List[Dict[str, Any]]): Lista onde os contatos são armazenados.
      id (int): ID do contato a ser editado.

  Returns:
      None
  """
  contacts[id]["favorite"] = False if contacts[id]["favorite"] else True

  message = f"\n[bold green]✅ Contato favoritado![/bold green]\n" if contacts[id]["favorite"] else f"\n[bold yellow]⛔️ Contato desfavoritado![/bold yellow]\n"
  console.print(message)
  return

def show_favorites_contacts(contacts: list) -> None:
  """
  Exibe os contatos marcados como favoritos.

  Args:
    contacts (List[Dict[str, Any]]): Lista onde os contatos são armazenados.

  Returns:
    None
  """
  favorites = [contact for contact in contacts if contact["favorite"] == True]

  contacts_formatted = []

  for idx, contact in enumerate(favorites, start=1):
    contact_formated = {
      "id": idx,
      "name": contact["name"],
      "phone": contact["phone"],
      "email": contact["email"],
      "favorite": "✓" if contact["favorite"] else ""
    }
    
    contacts_formatted.append(contact_formated)  

  colalign = ["left"] * len(favorites[0])

  print(tabulate(contacts_formatted, headers="keys", tablefmt="grid", colalign=colalign))
  return