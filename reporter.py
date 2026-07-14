def generate_markdown(analyzer) -> str:
    """生成Markdown格式的数据分析报告"""
    summary = analyzer.summary()
    report = f"#数据分析报告\n\n"
    report += f"##数据概况\n\n"
    report += f"- 行数：{len(analyzer.data)}\n"
    report += f"- 列数：{len(analyzer.data[0]) if analyzer.data else 0}\n"
    report += f"- 数据来源: {analyzer.fileopen}\n\n"
    report += f"##各列概况\n\n"
    report += f"| 列名 | 总数 | 缺失值 | 缺失率 | 样例 |\n"
    report += f"|------|------|------|------|------|\n"
    for col, info in summary.items():
        sample_str = ','.join(str(v) for v in info['sample_values'][:2])
        report += f"| {col} | {info['total']} | {info['missing']} | {info['missing_pct']} | {sample_str} |\n"

    # 统计可用数值列的统计信息
    report += f"\n##数据统计\n\n"
    for col in summary.keys():
        try:
            stats = analyzer.stats(col)
            report += f"###{col}\n"
            report += f"- 均值：{stats['mean']:.2f}\n"
            report += f"- 最小值：{stats['min']:.2f}\n"
            report += f"- 最大值：{stats['max']:.2f}\n"
            report += f"- 中位值：{stats['median']:.2f}\n"
            report += f"- 有效数据量：{stats['count']}\n"
        except ValueError:
            pass
    return report
