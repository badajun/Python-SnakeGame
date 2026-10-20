# Python 贪吃蛇

使用 Python 和 Pygame 编写的小游戏，适合初学者阅读和修改。

## 安装与运行（Windows）

1. 安装 Python 3（推荐 3.12），安装时勾选 **Add python.exe to PATH**。
2. 下载本仓库的 ZIP 并解压，或使用 Git 克隆仓库。
3. 在包含 `snake_game.py` 的文件夹打开 PowerShell，依次运行：

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install pygame==2.6.1
.\.venv\Scripts\python.exe snake_game.py
```

直接调用虚拟环境中的 Python，无需激活虚拟环境。运行时应出现游戏菜单窗口。
如果没有 `py` 命令，可以尝试用 `python` 替换第一条命令中的 `py`。

在 macOS / Linux 桌面环境中：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install pygame==2.6.1
.venv/bin/python snake_game.py
```

## 玩法与按键

| 按键 | 功能 |
| --- | --- |
| 1 / 2 / 3 | 在开始菜单选择简单 / 普通 / 困难 |
| Enter | 开始游戏，默认普通难度 |
| 方向键 | 改变移动方向，不能直接掉头 |
| 空格 | 暂停或继续游戏 |
| Esc | 返回开始菜单 |
| C | 游戏结束后返回菜单，再按 Enter 重新开始 |
| Q / 关闭窗口 | 退出游戏 |

简单、普通、困难分别每秒移动 5、8、12 格。蛇开始后自动向右移动；
吃到红色食物增加一分并增长一格，碰墙或碰到身体则结束。
暂停期间蛇和分数保持不变。填满棋盘即可获胜。
菜单使用英文，避免依赖系统中文字体。

## 阅读代码

- `DIFFICULTIES`：三种难度的移动速度。
- `new_food()`：在空格子中随机生成食物。
- `move_snake()`：计算移动、吃食物和碰撞，不负责画图。
- `main()`：处理菜单、键盘输入、暂停和画面绘制。
- `state`：记录当前是菜单、游戏中、暂停还是结束。

想练习使用 Codex，可以尝试要求它解释一个函数、调整颜色，或者增加最高分记录，
每次只改一个小功能并运行验证。

## 检查与云环境限制

语法检查：

```powershell
.\.venv\Scripts\python.exe -m py_compile snake_game.py
```

无图形桌面的云环境可以使用 SDL 的 dummy 驱动进行自动化逻辑与绘制检查，
但不会出现可操作的窗口。无窗口检查不能证明真实窗口、实际键盘输入、字体显示及
不同难度的操作手感正常，这些需要在 Windows 等桌面环境中实际试玩。
