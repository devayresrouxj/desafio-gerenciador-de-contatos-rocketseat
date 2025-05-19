from rich.console import Console

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
