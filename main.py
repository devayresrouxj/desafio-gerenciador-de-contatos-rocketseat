from questionary import select, Choice

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

if __name__ == "__main__":
  main()