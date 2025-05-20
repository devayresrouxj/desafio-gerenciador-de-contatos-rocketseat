from rich.console import Console
from tabulate import tabulate
from typing import List, Dict, Any

console = Console()

def validate_fields(name: str, phone: str, email: str) -> bool:
  """
  Valida os campos obrigatórios.

  Se algum campo for vazio retorna False caso contrario True.

  Args:
    name (str): Nome do contato.
    phone (str): Número de telefone do contato.
    email (str): Endereço de e-mail do contato.

  Returns:
    bool
  """
  return bool(name.strip() and phone.strip() and email.strip())

def add_contact(contacts: List[Dict[str, Any]], name: str, phone: str, email: str, favorite: bool = False) -> None:
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
  if not validate_fields(name, phone, email):
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

def tabulate_contacts(contacts: List[Dict[str, Any]]) -> None:
  """
    Exibe uma lista de contatos formatada em tabela no terminal.

    A função recebe uma lista de dicionários representando contatos e os formata
    usando a biblioteca `tabulate` para exibição no terminal. Cada contato é numerado 
    com um ID incremental (começando de 1), e o campo "favorite" é exibido com uma marca 
    de verificação (✓) se verdadeiro.

    Args:
      contacts (List[Dict[str, Any]]): Lista de contatos, onde cada contato é um dicionário
      com as chaves: "name", "phone", "email" e "favorite".

    Returns:
      None
  """
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

def show_contacts(contacts: List[Dict[str, Any]]) -> None:
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

  tabulate_contacts(contacts)
  return

def update_contact(contacts: List[Dict[str, Any]], id: int, name: str, phone: str, email: str, favorite: bool) -> None:
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
  if not validate_fields(name, phone, email):
    console.print(f"\n[bold yellow]⚠️ Todos os campos são obrigatórios![/bold yellow]\n")
    return

  contacts[id]["name"] = name
  contacts[id]["phone"] = phone
  contacts[id]["email"] = email
  contacts[id]["favorite"] = favorite

  console.print(f"\n[bold green]✅ Contato atualizado com sucesso![/bold green]\n")
  return

def toggle_favorite(contacts: List[Dict[str, Any]], id: int) -> None:
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

def show_favorites_contacts(contacts: List[Dict[str, Any]]) -> None:
  """
  Exibe os contatos marcados como favoritos.

  Args:
    contacts (List[Dict[str, Any]]): Lista onde os contatos são armazenados.

  Returns:
    None
  """
  favorites = [contact for contact in contacts if contact["favorite"] == True]

  tabulate_contacts(favorites)
  return

def delete_contact(contacts: List[Dict[str, Any]], id: int) -> None:
  """
  Deleta um contato específico.

  Args:
    contacts (List[Dict[str, Any]]): Lista onde os contatos são armazenados.
    id (int): ID do contato a ser editado.

  Returns:
    None
  """
  del contacts[id]
  console.print(f"\n[bold green]✅ Contato excluido![/bold green]\n")
  return