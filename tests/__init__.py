import os
import subprocess
import sys
import unittest
from importlib import import_module
from pathlib import Path


目录 = Path(__file__).resolve().parent.parent


def 运行(脚本: str, 输入: str) -> str:
    命令 = [sys.executable, "-S", "-B", str(目录 / 脚本)]
    if 配置 := os.environ.get("COVERAGE_PROCESS_START"):
        命令 = [sys.executable, "-B", "-m", "coverage", "run", "--rcfile", 配置, str(目录 / 脚本)]
    return subprocess.run(
        命令,
        input=输入,
        text=True,
        capture_output=True,
        check=True,
        cwd=目录,
        timeout=5,
    ).stdout


def load_tests(加载器: unittest.TestLoader, 测试: unittest.TestSuite, 模式: str | None) -> unittest.TestSuite:
    return unittest.TestSuite(
        加载器.loadTestsFromModule(import_module(f"{__name__}.{文件.stem}"))
        for 文件 in sorted(Path(__file__).parent.glob("*.py"))
        if 文件.stem != "__init__"
    )
