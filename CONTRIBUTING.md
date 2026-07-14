# 贡献指南

欢迎贡献！请先阅读本文了解流程。

## 开发环境

```bash
git clone https://github.com/panzhaohu666/data-toolbox-cli.git
cd data-toolbox-cli
pip install -e ".[dev]"
```

## 开发流程

1. **Fork** 本仓库并创建特性分支
   ```bash
   git checkout -b feature/your-feature
   ```

2. **编写代码**，确保：
   - 类型注解完整（通过 `mypy --strict`）
   - 遵循现有代码风格（`ruff` 会自动检查）
   - 为新功能添加测试

3. **本地验证**
   ```bash
   make lint    # ruff 代码检查
   make test    # 运行测试
   make mypy    # 类型检查
   ```

4. **提交** 并推送到你的 fork
   ```bash
   git commit -m "feat: 简短描述"
   git push origin feature/your-feature
   ```

5. **创建 Pull Request** 到 `main` 分支

## Commit 规范

使用 [Conventional Commits](https://www.conventionalcommits.org/)：

```
feat: 新功能
fix:  修复 bug
docs: 文档变更
test: 测试相关
refactor: 重构
chore: 工程化（CI、构建等）
```

## 代码风格

- Python 3.8+ 语法
- 严格类型注解（mypy strict 模式）
- 250 行以内每个模块
- 公共 API 必须有 docstring

## 测试

- 单元测试覆盖核心逻辑
- CLI 集成测试覆盖命令行交互
- 新功能必须包含测试

```bash
pytest -v --cov=src/data_toolbox
```

## 需要帮助？

打开 Issue 提问，我们会尽快回复。
