import argparse

from data_toolbox.analyzer import DataAnalyzer
from data_toolbox.reporter import generate_markdown


def main():
    parser = argparse.ArgumentParser(description="数据工具箱CLI")
    subparsers = parser.add_subparsers(dest="command")

    # stats 子命名
    start_parser = subparsers.add_parser("start", help="显示统计信息")
    start_parser.add_argument("file", help="数据文件路径")
    start_parser.add_argument("--column", "-c", help="指定列")

    # clean 子命令
    clean_parser = subparsers.add_parser("clean", help="清洗数据")
    clean_parser.add_argument("file", help="数据文件路径")
    clean_parser.add_argument("--output", "-o", required=True, help="输出文件路径")

    # report 子命令
    report_parser = subparsers.add_parser("report", help="生成分析报告")
    report_parser.add_argument("file", help="数据文件路径")

    args = parser.parse_args()
    try:
        if args.command == "start":
            analyzer = DataAnalyzer(args.file)
            print(analyzer.stats(args.column) if args.column else analyzer.summary())
        elif args.command == "clean":
            analyzer = DataAnalyzer(args.file)
            analyzer.clean()
            analyzer.save(args.output)
            print(f"清洗完成，保存{args.output}")
        elif args.command == "report":
            analyzer = DataAnalyzer(args.file)
            print(generate_markdown(analyzer))
    except FileNotFoundError:
        print(f"错误：文件{args.file}不存在")
        exit(1)
    except Exception as e:
        print(f"错误：{e}")
        exit(1)


if __name__ == "__main__":
    main()
