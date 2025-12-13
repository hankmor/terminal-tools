# Terminal Tools 终端工具列表

本文档收录了各类优秀的终端工具，按功能分类整理。

## 📝 目录

- [编辑器](#编辑器)
- [开发工具](#开发工具)
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

---

## 阅读工具

### [newsboat](https://github.com/newsboat/newsboat)

终端 RSS 订阅阅读器，轻松管理和阅读订阅源。

**安装方式**：`brew install newsboat`

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

---

## 🎯 持续更新

本列表会持续更新，欢迎通过 Pull Request 贡献你喜欢的终端工具！

返回 [README](README.md)
