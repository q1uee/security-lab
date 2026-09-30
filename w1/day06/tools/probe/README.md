项目采用 uv 进行项目管理与虚拟环境隔离。在 security-lab 仓库内使用 uv init 创建 tools/probe 子项目，添加 --vcs none 避免嵌套 Git 仓库。虚拟环境实现项目依赖隔离，区分本机全局包与项目声明依赖；项目依赖统一写入 pyproject.toml，使用 uv add 添加依赖，uv run 在项目隔离环境运行程序，uv sync 用于环境同步复现。代码规范工具 ruff 通过 uv tool 全局安装，不属于项目业务依赖。

uv add requests
在当前项目，把 requests 添加到项目依赖，写入 pyproject.toml，并安装到项目虚拟环境。
uv run xxx.py
使用项目虚拟环境里的 Python执行脚本。自动激活环境，不用手动 source venv/bin/activate。
uv sync
读取 pyproject.toml，自动安装 / 更新 / 删除依赖，把虚拟环境依赖和配置文件保持同步。
别人拉取仓库后，执行 uv sync 就能一键还原完全一致依赖。


uv init tools/probe --app --vcs none
tools/probe：在现有 git 仓库内部创建子项目目录，不要在外层新建独立 git
--app：标记这是应用程序项目，不是 Python 库，自动生成可执行入口配置
--vcs none：重点，不生成子项目内部的 .git，避免嵌套 git 仓库（一个仓库套另一个 git 会出问题