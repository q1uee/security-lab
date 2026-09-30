from collections.abc import Callable
from pathlib import Path


class BatchFileProcessor:
    def __init__(self, root_dir: str | Path):  #:str|Path注解  str类型或者Path类型
        self.root_dir = Path(root_dir)
        if not self.root_dir.is_dir():
            # raise 是【抛出错误】（制造异常）；try/except 是【捕获、处理别人抛出来的异常】（接住异常）。
            raise NotADirectoryError(f"目录不存在或者不是文件夹:{self.root_dir}")

    def find_files(self, pattern: str = "*.log", recursive: bool = True) -> list[Path]:
        # : str：类型注解，告诉 IDE/ruff：pattern 参数应该是字符串，不是注释。
        # = "*.log"：参数默认值。
        """
        查找符合通配符规则的文件
        :param pattern: glob匹配规则，例如 *.log
        :param recursive: 是否递归子目录
        :return: Path对象列表
        """
        if recursive:
            file_iter = self.root_dir.rglob(pattern)
        else:
            file_iter = self.root_dir.glob(pattern)

        return [fp for fp in file_iter if fp.is_file()]

    def run(
        self, pattern: str, handler: Callable[[Path], None], recursive: bool = True
    ):
        # Callable：代表可调用对象，简单说就是一个函数（也可以是实现了__call__的类实例）。
        # Callable[[Path], None]
        # 方括号里第一部分 [Path]：这个函数接收的参数列表
        # → 意思：handler 函数必须接收1 个参数，类型是 Path 对象
        # 逗号后面 None：这个函数的返回值类型
        # → 意思：handler 函数不返回任何有效数据（return None，或者不写 return）
        """
        批量遍历筛选文件，对每个文件执行handler处理函数
        :param pattern: 文件匹配规则
        :param handler: 处理单个文件的回调函数，入参是Path对象
        :param recursive: 是否递归扫描子目录
        """
        file_list = self.find_files(pattern, recursive)
        for fp in file_list:
            try:
                handler(fp)
            except Exception as e:
                print(f"[警告]处理文件失败{fp},err:{e}")


if __name__ == "__main__":
    processor = BatchFileProcessor(root_dir="./logs")

    def process_log_file(file_path: Path):
        print(f"正在处理文件:{file_path}")
        content = file_path.read_text(encoding="utf-8")
        lines = content.splitlines()

    processor.run(pattern="*.log", handler=process_log_file, recursive=True)
