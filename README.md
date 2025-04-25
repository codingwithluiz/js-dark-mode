# Alternador de Modo Escuro ☀️🌙

Um sistema completo de alternância entre temas claro e escuro com persistência de preferências.

## ✨ Funcionalidades

- **Alternância instantânea** entre temas claro/escuro
- **Memorização** da preferência (localStorage)
- **Transições suaves** entre os modos
- **Totalmente personalizável** via CSS
- **Design responsivo** para todos dispositivos
- **Botão acessível** com emojis intuitivos
- **Prevenção de Flicker** (script inline no HTML)

## 🗂️ Estrutura de Arquivos

```
js-dark-mode/
├── index.html        # Página principal com script de prevenção
├── style.css         # Estilos com variáveis CSS para os temas
└── darkmode.js       # Lógica completa do modo escuro
```

## 🚀 Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/codingwithluiz/js-dark-mode.git
   cd js-dark-mode
   ```

2. Abra `index.html` no navegador

3. Clique no botão 🌙/☀️ no canto superior direito para alternar

## 🎨 Personalização

### Cores (edite no `style.css`)
```css
:root {
  --base-color: white;          /* Fundo claro */
  --text-color: #111528;        /* Texto claro */
  --accent-color: #0071ff;      /* Cor de destaque */
}

:root.darkmode {
  --base-color: #070b1d;        /* Fundo escuro */
  --text-color: #ffffff;        /* Texto escuro */
}
```

### Botão (estilos no `style.css`)
```css
#theme-switch {
  width: 60px;                 /* Tamanho */
  height: 60px;
  top: 30px;                   /* Posição */
  right: 30px;
}
```

## ⚙️ Funcionamento Técnico

1. **Prevenção de Flicker**: Script inline no HTML carrega primeiro
2. **Inicialização**: Verifica localStorage ao carregar
3. **Alternância**: Troca classes e atualiza localStorage
4. **Estilização**: Variáveis CSS dinâmicas controlam os temas

## 🌐 Compatibilidade

| Navegador       | Suporte |
| --------------- | ------- |
| Chrome          | ✅       |
| Firefox         | ✅       |
| Safari          | ✅       |
| Edge            | ✅       |
| Mobile Browsers | ✅       |

## 📄 Licença

MIT License - Livre para uso e modificação



