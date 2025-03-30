import emoji

# Lista de emojis disponíveis
emojis_disponiveis = {
    ':grinning_face:': emoji.emojize(':grinning_face:'),
    ':thumbs_up:': emoji.emojize(':thumbs_up:'),
    ':red_heart:': emoji.emojize(':red_heart:'),
    ':winking_face:': emoji.emojize(':winking_face:'),
    ':thinking_face:': emoji.emojize(':thinking_face:')
}

# Exibindo a lista de emojis
print("Lista de emojis disponíveis:")
for codigo, simbolo in emojis_disponiveis.items():
    print(f"{codigo} -> {simbolo}")

# Solicitar uma frase codificada ao usuário
frase_codificada = input("\nDigite uma frase utilizando os códigos de emoji (exemplo: ':grinning_face:'):\n")

# Decodificando a frase para emojis
frase_emojizada = emoji.emojize(frase_codificada)

# Exibindo a frase com emojis
print(f"\nFrase emojizada: {frase_emojizada}")
