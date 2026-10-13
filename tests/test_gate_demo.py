import os
import tempfile


def test_polluter_chdir():
    # 复刻 mdutils 历史 bug 模式（IDoFT 记录 8 条 victim 的元凶）：
    # chdir 进临时目录，上下文退出时目录被删 —— 进程 CWD 悬空。
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)


def test_victim_needs_cwd():
    # 受害者：CWD 悬空后，相对路径操作应挂（单独跑时正常）。
    with open("demo_relative.md", "w") as fh:
        fh.write("demo")
