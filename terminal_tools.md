# Terminal Tools 终端工具列表

本文档收录了各类优秀的终端工具，按功能分类整理。

## 📝 目录

- [编辑器](#编辑器)
- [终端模拟器](#终端模拟器)
- [开发工具](#开发工具)
- [AI 工具](#ai-工具)
- [文件管理](#文件管理)
- [系统工具](#系统工具)
- [网络工具](#网络工具)
- [数据库工具](#数据库工具)
- [图片处理](#图片处理)
- [阅读工具](#阅读工具)
- [TUI 开发库](#tui-开发库)
- [其他实用工具](#其他实用工具)

---

## 编辑器

### [Vim](https://www.vim.org/)

经典的文本编辑器，强大且高效。

**安装方式**：通常系统自带，或 `brew install vim`

### [Neovim](https://github.com/neovim/neovim)

超强大的现代化 Vim 编辑器，支持异步插件、内置 LSP、Lua 配置等。

**安装方式**：`brew install neovim`

### [LazyVim](https://github.com/LazyVim/LazyVim)

Neovim 的现代化配置框架，开箱即用，功能丰富。

**安装方式**：参考官方文档

### [LunarVim](https://github.com/LunarVim/LunarVim)

基于 Neovim 的 IDE 级配置，提供完整的开发环境。

**安装方式**：参考官方文档

---

## 终端模拟器

### [WezTerm](https://github.com/wez/wezterm)

🖥️ GPU 加速的跨平台终端模拟器和复用器，功能强大且高度可配置。

**支持系统**：macOS、Linux、Windows、FreeBSD

### [iTerm2](https://github.com/gnachman/iTerm2)

🍎 macOS 上最强大的终端模拟器，提供丰富的功能和集成。

**支持系统**：macOS

### [Alacritty](https://github.com/alacritty/alacritty)

⚡ 基于 OpenGL 的极速终端模拟器，注重性能和简洁。

**支持系统**：macOS、Linux、Windows、BSD

### [Kitty](https://github.com/kovidgoyal/kitty)

🐱 快速、功能丰富的 GPU 加速终端模拟器。

**支持系统**：macOS、Linux

### [Windows Terminal](https://github.com/microsoft/terminal)

🪟 微软官方现代化终端应用，支持多标签和丰富的自定义选项。

**支持系统**：Windows

### [Hyper](https://github.com/vercel/hyper)

✨ 基于 Electron 的美观可扩展终端，使用 Web 技术构建。

**支持系统**：macOS、Linux、Windows

### [Tabby](https://github.com/Eugeny/tabby)

🎯 高度可定制的跨平台终端，支持 SSH、串口等多种连接。

**支持系统**：macOS、Linux、Windows

### [Rio](https://github.com/raphamorim/rio)

🦀 使用 Rust 和 WebGPU 构建的现代化终端模拟器。

**支持系统**：macOS、Linux、Windows

---

## 开发工具

### [tmux](https://github.com/tmux/tmux)

终端复用器，支持会话管理和窗口分割。

**安装方式**：`brew install tmux`

### [Lazygit](https://github.com/jesseduffield/lazygit)

终端 Git 管理工具，提供直观的 TUI 界面。

**安装方式**：`brew install lazygit`

### [Lazydocker](https://github.com/jesseduffield/lazydocker)

终端 Docker 管理工具，轻松管理容器和镜像。

**安装方式**：`brew install lazydocker`

### [Lazynpm](https://github.com/jesseduffield/lazynpm)

终端 NPM 管理工具，简化包管理操作。

**安装方式**：`npm install -g lazynpm`

### [httplab](https://github.com/qustavo/httplab)

交互式终端网络请求工具，用于测试和调试 HTTP 请求。

**安装方式**：`brew install httplab`

### [gonzo](https://github.com/control-theory/gonzo)

Go 语言开发的 TUI 日志管理工具。

**安装方式**：参考官方文档

### [ripgrep](https://github.com/BurntSushi/ripgrep)

极快的代码搜索工具，`grep` 的现代替代品。

**安装方式**：`brew install ripgrep`

### [fzf](https://github.com/junegunn/fzf)

命令行模糊查找工具，可与其他工具集成。

**安装方式**：`brew install fzf`

### [fd](https://github.com/sharkdp/fd)

简单快速的 `find` 替代品。

**安装方式**：`brew install fd`

### [ag (The Silver Searcher)](https://github.com/ggreer/the_silver_searcher)

快速的代码搜索工具。

**安装方式**：`brew install the_silver_searcher`

---

## AI 工具

### [Claude Code](https://github.com/anthropics/claude-code)

🤖 Anthropic 官方 Claude 命令行工具，可在终端直接与 Claude 对话和编写代码。

**安装方式**：`npm install -g @anthropic-ai/claude-code`  
**使用说明**：需要 Claude Pro 或 Max 订阅

### [OpenAI Codex CLI](https://github.com/openai/codex)

💡 OpenAI 官方编码助手，支持在终端中进行代码编辑和执行。

**安装方式**：`npm i -g @openai/codex`  
**使用说明**：需要 ChatGPT Plus/Pro 订阅或 API Key

### [GitHub Copilot CLI](https://github.com/github/copilot-cli)

✨ GitHub Copilot 的终端版本，提供 AI 辅助的命令行建议。

**安装方式**：`npm install -g @github/github-copilot-cli`  
**使用说明**：需要 GitHub Copilot 订阅

### [aichat](https://github.com/sigoden/aichat)

🚀 多合一 AI 聊天终端工具，支持 OpenAI、Claude、Gemini 等 20+ AI 模型。

**安装方式**：`brew install aichat`

### [mods](https://github.com/charmbracelet/mods)

🎨 由 Charm 开发的 AI 终端工具，支持多种 LLM，界面美观。

**安装方式**：`brew install mods`

### [shell_gpt](https://github.com/TheR1D/shell_gpt)

⚡ 使用 AI 生成和执行 Shell 命令，提高终端效率。

**安装方式**：`pip install shell-gpt`

### [llm](https://github.com/simonw/llm)

🛠️ Simon Willison 开发的 LLM 命令行工具，支持多个模型和丰富的插件系统。

**安装方式**：`pip install llm` 或 `brew install llm`

### [fabric](https://github.com/danielmiessler/fabric)

🧩 开源 AI 模式框架，提供 300+ 预定义 AI 提示模板。

**安装方式**：`brew install fabric`

### [chatgpt-cli](https://github.com/kardolus/chatgpt-cli)

� 功能强大的 ChatGPT 终端客户端，支持会话管理。

**安装方式**：`brew install chatgpt-cli` 或参考 GitHub 安装说明

### [OpenCode](https://github.com/anomalyco/opencode)

🤖 终端原生 AI 编程助手，支持自然语言交互、多模型架构，可直接在终端中修改代码。

**安装方式**：`curl -fsSL https://opencode.ai/install | bash`

---

## 文件管理

### [Yazi](https://github.com/sxyazi/yazi)

使用 Rust 编写的简单易用、功能强大的终端文件管理器。

**安装方式**：`brew install yazi`

### [Ranger](https://github.com/ranger/ranger)

基于 Vim 键位的终端文件管理器，功能丰富。

**安装方式**：`brew install ranger`

### [superfile](https://github.com/yorukot/superfile)

现代化的终端文件管理器，界面美观。

**安装方式**：参考官方文档

### [lsd](https://github.com/lsd-rs/lsd)

现代化的 `ls` 替代品，支持图标和颜色。

**安装方式**：`brew install lsd`

### [exa](https://github.com/ogham/exa)

现代化的 `ls` 替代品，功能丰富。

**安装方式**：`brew install exa`

---

## 系统工具

### [BTOP](https://github.com/aristocratos/btop)

💻 终极系统资源监控工具，支持 CPU、GPU、内存、磁盘和网络使用情况的详细展示。

**安装方式**：`brew install btop`

### [htop](https://github.com/htop-dev/htop)

交互式进程查看器，比 `top` 更友好。

**安装方式**：`brew install htop`

### [Neofetch](https://github.com/dylanaraps/neofetch)

🎨 炫酷展示系统信息的工具，适合分享电脑配置截图。

**安装方式**：`brew install neofetch`

### [Axle](https://github.com/varletjs/axle)

🚀 提升下载速度的轻量级工具，通过多连接下载大幅提高速度。

**安装方式**：参考官方文档

### [tldr](https://github.com/tldr-pages/tldr)

替代 man 的命令提示工具，提供简洁实用的命令示例。

**安装方式**：`brew install tldr`

### [duf](https://github.com/muesli/duf)

替代 df 的磁盘管理工具，界面友好。

**安装方式**：`brew install duf`

### [bat](https://github.com/sharkdp/bat)

替代 cat 的查看工具，支持语法高亮和 Git 集成。

**安装方式**：`brew install bat`

### [zoxide](https://github.com/ajeetdsouza/zoxide)

替代 cd 的智能目录跳转工具，记住你常用的目录。

**安装方式**：`brew install zoxide`

---

## 网络工具

### [curl](https://curl.se/)

强大的数据传输工具。

**安装方式**：通常系统自带

### [httpie](https://github.com/httpie/httpie)

用户友好的 HTTP 客户端。

**安装方式**：`brew install httpie`

### Speed Test

⚡ 直接在终端测试网络速度，快速获取下载和上传速度。

**安装方式**：`brew install speedtest-cli`

---

## 数据库工具

### [mycli](https://github.com/dbcli/mycli)

MySQL 的终端客户端，支持自动补全和语法高亮。

**安装方式**：`brew install mycli`

### [gobang](https://github.com/TaKO8Ki/gobang)

跨平台的终端数据库管理工具，支持多种数据库。

**安装方式**：`brew install gobang`

### [lazysql](https://github.com/jorgerojas26/lazysql)

终端 SQL 数据库管理工具，简单易用。

**安装方式**：参考官方文档

---

## 图片处理

### imgcat

终端渲染并展示图片。

**安装方式**：通常随 iTerm2 提供

### [chafa](https://github.com/hpjansson/chafa)

命令行图片处理工具，将图片转换为终端可显示的字符画。

**安装方式**：`brew install chafa`

### [ImageMagick](https://imagemagick.org/)

强大的图片处理工具集，支持格式转换、编辑等。

**安装方式**：`brew install imagemagick`

### [diagram](https://github.com/esimov/diagram)

将 ASCII 字符画转换为手绘图表。

**安装方式**：参考官方文档

### [gifski](https://github.com/ImageOptim/gifski)

🌈 高质量 GIF 编码器，基于 Pngquant，可创建画质极佳的 GIF 动图。

**安装方式**：`brew install gifski`
**CLI安装**: `cargo install gifski`

---

## 阅读工具

### [newsboat](https://github.com/newsboat/newsboat)

终端 RSS 订阅阅读器，轻松管理和阅读订阅源。

**安装方式**：`brew install newsboat`

### [glow](https://github.com/charmbracelet/glow)

💅 终端 Markdown 阅读器，支持丰富的主题和样式。

**安装方式**：`brew install glow`

---

## TUI 开发库

### [Bubble Tea](https://github.com/charmbracelet/bubbletea)

Golang 最流行、强大的 TUI 框架，基于 Elm 架构。

**安装方式**：`go get github.com/charmbracelet/bubbletea`

### [gocui](https://github.com/jroimartin/gocui)

基于 Golang 开发的终端用户接口库，用于开发终端应用程序。

**安装方式**：`go get github.com/jroimartin/gocui`

---

## 其他实用工具

### [cointop](https://github.com/cointop-sh/cointop)

终端加密货币查看工具，实时追踪加密货币价格。

**安装方式**：`brew install cointop`

### [vhs](https://github.com/charmbracelet/vhs)

📼 编写脚本生成终端 GIF 演示，将终端操作录制为高质量 GIF。

**安装方式**：`brew install vhs`

### [jq](https://github.com/jqlang/jq)

命令行 JSON 处理器。

**安装方式**：`brew install jq`

### [delta](https://github.com/dandavison/delta)

Git 和 diff 输出的语法高亮工具。

**安装方式**：`brew install git-delta`

### [Starship](https://github.com/starship/starship)

快速、可定制的跨 Shell 提示符。

**安装方式**：`brew install starship`

### [Zsh](https://www.zsh.org/)

功能强大的 Shell，支持丰富的插件和主题。

**安装方式**：`brew install zsh`

### [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh)

Zsh 配置管理框架，提供大量插件和主题。

**安装方式**：`sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`

### [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)

Zsh 自动补全插件，提供智能的命令补全建议。

**安装方式**：`git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`

---

## 🎯 持续更新

本列表会持续更新，欢迎通过 Pull Request 贡献你喜欢的终端工具！

返回 [README](README.md)
