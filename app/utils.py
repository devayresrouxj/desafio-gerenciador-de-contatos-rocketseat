from questionary import text
from rich.console import Console
from app.contacts import show_contacts
from typing import Optional
from typing import List, Dict, Any

console = Console()

def ask_id(contacts: List[Dict[str, Any]]) -> Optional[int] :
  """
    Solicita ao usuário o ID de um contato a ser atualizado e retorna o índice correspondente.

    Exibe a lista de contatos disponíveis e solicita que o usuário insira um ID.
    O ID informado é convertido em um índice de lista (subtraindo 1).
    Caso a entrada seja inválida (não numérica ou fora do intervalo da lista de contatos),
    a função exibe uma mensagem de erro e retorna None.

    Args:
      contacts (List[Dict[str, Any]]): Lista onde os contatos são armazenados.

    Returns:
      Optional[int]: O índice do contato (baseado em zero), ou None se a entrada for inválida.
  """
  show_contacts(contacts)

  try:
    contact_id = int(text("Digite o ID do contato que você deseja atualizar").ask())
  except ValueError:
    console.print(f"\n[bold red]❌ Entrada inválida! Digite um número válido.[/bold red]\n")
    return None

  contact_index = contact_id - 1

  if contact_id < 1 or contact_id > len(contacts):
    console.print(f"\n[bold yellow]⚠️ Nenhum contato encontrado com este ID![/bold yellow]\n")
    return None
  
  return contact_index
