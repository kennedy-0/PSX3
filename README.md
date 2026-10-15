# 🎮 PSX Virtual Controller

Conversor de joystick físico para controle virtual Xbox 360, desenvolvido em Python.

## 📌 Sobre o projeto

O PSX Virtual Controller utiliza Pygame para detectar os comandos de um joystick físico e vgamepad para reproduzi-los em um controle virtual compatível com Xbox 360.

## ⚙️ Tecnologias

- Python
- Pygame
- vgamepad
- ViGEmBus (Windows)

## 🚀 Funcionalidades

- Detecção de joystick conectado.
- Leitura de botões pressionados e liberados.
- Mapeamento de botões para o controle Xbox 360.
- Suporte ao direcional digital (D-Pad).
- Monitoramento dos eixos do joystick.
- Terminal com cores ANSI.

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/kennedy-0/psx-virtual-controller.git
cd psx-virtual-controller
```

Crie e ative o ambiente virtual no Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```
## ▶️ Execução

```bash
python src/main.py
```

Conecte seu joystick antes de iniciar o programa.

## 🧠 Funcionamento

1. O Pygame detecta o joystick físico.
2. Os eventos dos botões são capturados.
3. Os comandos são associados aos botões virtuais.
4. O vgamepad atualiza o estado do controle Xbox 360.

## 🔮 Melhorias futuras

- Mapeamento dos analógicos.
- Configuração personalizada dos botões.
- Interface gráfica.
- Suporte a múltiplos joysticks.

## 👨‍💻 Autor

**Daniel Kennedy | Cyber Wanderer**

GitHub: [@kennedy-0](https://github.com/kennedy-0)

## 📄 Licença

Este projeto está disponível sob a licença MIT, quando acompanhado de um arquivo `LICENSE` correspondente.
